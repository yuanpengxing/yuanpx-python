# -*- coding: UTF-8 -*-
# author: yuanpx

from urllib.parse import urlparse
import xml.dom.minidom
import os

from utils.curlconvert import CurlConvert
from utils.file import FileUtil
from utils.jjmeter import curlpython
from utils.str import StringUtil

LF = '\n'


def url_bash_copys(copyAscURLBash):
    # 获取单个CopyAscURLBash字符串数组
    boundright = '--compressed'
    boundleft = "curl 'http"
    copys = []
    StringUtil.match3(FileUtil.get_text(copyAscURLBash), boundleft, boundright, copys)
    return copys


def to_jmeter_style(obj):
    # 将字符串转换成jmeter格式的，防止一些特殊字符
    if isinstance(obj, dict):
        dt = {}
        for key, value in obj.items():
            var = value.replace('&', '&amp;').replace('"', '&quot;').replace("'", '&apos;').replace(
                '<', '&lt;').replace('>', '&gt;')
            dt[key] = var
        return dt
    elif isinstance(obj, str):
        var = obj.replace('&', '&amp;').replace('"', '&quot;').replace("'", '&apos;').replace('<', '&lt;').replace(
            '>', '&gt;')
        return var
    else:
        return None


def requests_info(copyAscURLBash):
    # 获取单个CopyAscURLBash请求信息数组
    copys = url_bash_copys(copyAscURLBash)
    requests_info = []
    for copy in copys:
        save = os.path.dirname(__file__) + '/curlpython.py'
        converter = CurlConvert.to_python(copy)
        CurlConvert.to_script(save, converter)

        headers = to_jmeter_style(getattr(curlpython, 'headers', None))
        data = to_jmeter_style(getattr(curlpython, 'data', None))
        params = to_jmeter_style(getattr(curlpython, 'params', None))
        url, method = CurlConvert.get_url_method(save)

        info = {
            'url': to_jmeter_style(url),
            'headers': headers,
            'method': method,
            'data': data,
            'params': params
        }
        requests_info.append(info)
    return requests_info


def getSampler(request):
    headers, url, method, data = request['headers'], request['url'], request['method'], request['data']
    params = request['params']
    uri = urlparse(url)
    protocol, hostname, port, path, query = uri.scheme, uri.hostname, uri.port, uri.path, uri.query
    if params:
        for key, value in params.items():
            query += key + '=' + value + '&amp;'
        path = path + '?' + query
    else:
        if query:
            path = path + '?' + query
    if not port:
        port = ''
    httpSampler = '''
        <HTTPSamplerProxy guiclass="HttpTestSampleGui" testclass="HTTPSamplerProxy" testname="%s" enabled="true">
          <stringProp name="HTTPSampler.domain">%s</stringProp>
          <stringProp name="HTTPSampler.port">%s</stringProp>
          <stringProp name="HTTPSampler.protocol">%s</stringProp>
          <stringProp name="HTTPSampler.contentEncoding"></stringProp>
          <stringProp name="HTTPSampler.path">%s</stringProp>
          <stringProp name="HTTPSampler.method">%s</stringProp>
          <boolProp name="HTTPSampler.follow_redirects">true</boolProp>
          <boolProp name="HTTPSampler.auto_redirects">false</boolProp>
          <boolProp name="HTTPSampler.use_keepalive">true</boolProp>
          <boolProp name="HTTPSampler.DO_MULTIPART_POST">false</boolProp>
          <stringProp name="HTTPSampler.embedded_url_re"></stringProp>
          <stringProp name="HTTPSampler.connect_timeout"></stringProp>
          <stringProp name="HTTPSampler.response_timeout"></stringProp>
        </HTTPSamplerProxy>
    ''' % (path, hostname, port, protocol, path, method)
    return insert_before_line(httpSampler, getElementProp(data, headers), 'HTTPSampler.domain')


def getElementProp(body, headers):
    if not body:
        return '''
          <elementProp name="HTTPsampler.Arguments" elementType="Arguments" guiclass="HTTPArgumentsPanel" testclass="Arguments" testname="User Defined Variables" enabled="true">
            <collectionProp name="Arguments.arguments"/>
          </elementProp>
        '''
    else:
        if 'application/json' in headers['content-type']:
            return '''
              <boolProp name="HTTPSampler.postBodyRaw">true</boolProp>
              <elementProp name="HTTPsampler.Arguments" elementType="Arguments">
                <collectionProp name="Arguments.arguments">
                  <elementProp name="" elementType="HTTPArgument">
                    <boolProp name="HTTPArgument.always_encode">false</boolProp>
                    <stringProp name="Argument.value">%s</stringProp>
                    <stringProp name="Argument.metadata">=</stringProp>
                  </elementProp>
                </collectionProp>
              </elementProp>
            ''' % body
        else:
            s1 = '''
              <elementProp name="HTTPsampler.Arguments" elementType="Arguments" guiclass="HTTPArgumentsPanel" testclass="Arguments" testname="User Defined Variables" enabled="true">
                <collectionProp name="Arguments.arguments">
            '''
            for argname, argvaule in body.items():
                s1 += '''
                  <elementProp name="%s" elementType="HTTPArgument">
                    <boolProp name="HTTPArgument.always_encode">false</boolProp>
                    <stringProp name="Argument.value">%s</stringProp>
                    <stringProp name="Argument.metadata">=</stringProp>
                    <boolProp name="HTTPArgument.use_equals">true</boolProp>
                    <stringProp name="Argument.name">%s</stringProp>
                  </elementProp>
                ''' % (argname, argvaule, argname)
            s1 += '''
                </collectionProp>
              </elementProp>
            '''
            return s1


def getHeaderManager(request):
    s1 = '''
          <HeaderManager guiclass="HeaderPanel" testclass="HeaderManager" testname="HTTP Header Manager" enabled="true">
            <collectionProp name="HeaderManager.headers">
    '''
    for key, value in request['headers'].items():
        s1 += '''
              <elementProp name="" elementType="Header">
                <stringProp name="Header.name">%s</stringProp>
                <stringProp name="Header.value">%s</stringProp>
              </elementProp>
        ''' % (key, value)
    s1 += '''
            </collectionProp>
          </HeaderManager>
    '''
    return s1


def getConstantThroughput(timer):
    s = '''
        <ConstantThroughputTimer guiclass="TestBeanGUI" testclass="ConstantThroughputTimer" testname="Constant Throughput Timer" enabled="true">
          <intProp name="calcMode">0</intProp>
          <doubleProp>
            <name>throughput</name>
            <value>%d.0</value>
            <savedValue>0.0</savedValue>
          </doubleProp>
        </ConstantThroughputTimer>
        <hashTree/>
    ''' % timer
    return s


def getJSR223Post(jsr223Post):
    s = '''
          <JSR223PostProcessor guiclass="TestBeanGUI" testclass="JSR223PostProcessor" testname="JSR223 PostProcessor" enabled="true">
            <stringProp name="cacheKey">true</stringProp>
            <stringProp name="filename"></stringProp>
            <stringProp name="parameters"></stringProp>
            <stringProp name="script">%s</stringProp>
            <stringProp name="scriptLanguage">groovy</stringProp>
          </JSR223PostProcessor>
    ''' % jsr223Post
    return s


def insert_before_line(text, appendstr, pattern):
    split = text.split(LF)
    tx = ''
    for line in split:
        if pattern in line:
            tx += appendstr + LF
        tx += line + LF
    return tx


def trip_empty_line(text):
    splits = text.split(LF)
    tx = ''
    for line in splits:
        if line.strip():
            tx += line + LF
    return tx


def xmlformat(text):
    text = trip_empty_line(text)
    text = xml.dom.minidom.parseString(text)
    text = text.toprettyxml()
    text = trip_empty_line(text)
    return text
