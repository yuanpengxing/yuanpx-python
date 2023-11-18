# -*- coding: UTF-8 -*-
# author: yuanpx

from utils.jjmeter import JMeterUtil
from utils.jjmeter.JMeterTree import *


def generateJMeterScript(savefile, copyAscURLBash, timer=0, jsr223Post=''):
    with open(savefile, 'w', encoding='utf-8') as wf:
        text = TestPlanStart + HashTreeStart + ResultTree + AggerateReport + ThreadGroup + HashTreeStart
        requests_info = JMeterUtil.requests_info(copyAscURLBash)
        for request in requests_info:
            headerManager = JMeterUtil.getHeaderManager(request)
            httpSampler = JMeterUtil.getSampler(request)
            if timer:
                text += JMeterUtil.getConstantThroughput(timer)
            text += httpSampler
            text += HashTreeStart
            text += headerManager
            text += HashTree
            if jsr223Post:
                text += JMeterUtil.getJSR223Post(jsr223Post)
            text += HashTreeEnd
        text += HashTreeEnd + HashTreeEnd + TestPlanEnd
        wf.write(JMeterUtil.xmlformat(text))


if __name__ == '__main__':
    generateJMeterScript('d:/testa.jmx', 'CopyAscURLBash.txt')
