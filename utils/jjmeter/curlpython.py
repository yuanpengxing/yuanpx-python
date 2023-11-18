# -*- coding: UTF-8 -*-
import requests

headers = {
    'authority': 'www.douyin.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'bd-ticket-guard-client-data': 'eyJ0c19zaWduIjoidHMuMS5mYzVjYTljMTVmYWM3NmY5ZDIwNGFiMGY3NjBkZjk1NWU2Y2NiNTFjMTU4NWJiOWU4MmUwYzZjNWYxMTA1ODZmYzRmYmU4N2QyMzE5Y2YwNTMxODYyNGNlZGExNDkxMWNhNDA2ZGVkYmViZWRkYjJlMzBmY2U4ZDRmYTAyNTc1ZCIsInJlcV9jb250ZW50IjoidGlja2V0LHBhdGgsdGltZXN0YW1wIiwicmVxX3NpZ24iOiJNRVFDSUJuYU5udnF1b0pmdEJmLzlYa0ovbHVhbTEvUjc1WU9PTjZJQUpGdWJjM1FBaUIyT0tRc0NlbUVsbk5OYmVKL0RLVVpobTJSa01nODhvN1FsOURkdHlMYWx3PT0iLCJ0aW1lc3RhbXAiOjE2OTk2NzY5NDB9',
    'bd-ticket-guard-iteration-version': '1',
    'bd-ticket-guard-ree-public-key': 'BNX4glErZrJIRuZC7TJUL+ZC3MEhr6xUtApA/JCx/GRYiIKBi5RhLIwf8JRePT0AefD8h2qACvdImJ2cWDiP/KY=',
    'bd-ticket-guard-version': '2',
    'bd-ticket-guard-web-version': '1',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'cookie': 'ttwid=1%7Cg4KF41fihjekNryQEXmvpG1fYDsb5obmfDFscVZiSJc%7C1699141987%7C03768fe320decae9dbf492f2dc9ffc21daafb7413669d0a31842ea6a81a39262; passport_csrf_token=2e03eca908f9a8b96dc4ba8af17487e8; passport_csrf_token_default=2e03eca908f9a8b96dc4ba8af17487e8; FORCE_LOGIN=%7B%22videoConsumedRemainSeconds%22%3A180%2C%22isForcePopClose%22%3A1%7D; s_v_web_id=verify_lokp9sjt_zPMuDGXl_U5hb_4W0w_BaNf_gtYsUNRg3nxw; volume_info=%7B%22isUserMute%22%3Afalse%2C%22isMute%22%3Afalse%2C%22volume%22%3A0.5%7D; ttcid=dcfb3a197fc24a0fb4a4dabc9f05fb8233; n_mh=7MDEc7m1-J8ip_SKgJhJcC0r2OZItK8fz5Fy-cm9eQA; sso_uid_tt=4facb43f71a3baf59f956a5e725e6550; sso_uid_tt_ss=4facb43f71a3baf59f956a5e725e6550; toutiao_sso_user=06b6afa51db329b23b0f73ca91a8e336; toutiao_sso_user_ss=06b6afa51db329b23b0f73ca91a8e336; passport_assist_user=CjzXzwR7CLB5mI-ULjhhsi8k0OVvWESxVP9w6v-XP7wqJxqI5G1obod5ucHqm9SiA42qzt9jfkZwOvjTV3saSgo8bTnjACekNr8xaJVFRI_P1MpthIKSLrsdjcxVKwknK5EdDW6Td0m_k_rzUy-mKFn35BLMUGsK0cIU56swEJ25wA0Yia_WVCABIgED8roAUw%3D%3D; sid_ucp_sso_v1=1.0.0-KGY5OWM1Y2M5ZTQ2MWM2MzBlNTM4OGE0MTU1NTNjZTNhOWRiYzcxYWQKHQj05KCv7QIQkbObqgYY7zEgDDDG_7HXBTgGQPQHGgJscSIgMDZiNmFmYTUxZGIzMjliMjNiMGY3M2NhOTFhOGUzMzY; ssid_ucp_sso_v1=1.0.0-KGY5OWM1Y2M5ZTQ2MWM2MzBlNTM4OGE0MTU1NTNjZTNhOWRiYzcxYWQKHQj05KCv7QIQkbObqgYY7zEgDDDG_7HXBTgGQPQHGgJscSIgMDZiNmFmYTUxZGIzMjliMjNiMGY3M2NhOTFhOGUzMzY; passport_auth_status=7bc7f3021424839b1a120a1c2c2d5616%2C; passport_auth_status_ss=7bc7f3021424839b1a120a1c2c2d5616%2C; uid_tt=93c8d1338595b3fcc12cd6731c696164; uid_tt_ss=93c8d1338595b3fcc12cd6731c696164; sid_tt=56cd51d490ceff998424239c711e1ca7; sessionid=56cd51d490ceff998424239c711e1ca7; sessionid_ss=56cd51d490ceff998424239c711e1ca7; LOGIN_STATUS=1; store-region=cn-bj; store-region-src=uid; _bd_ticket_crypt_doamin=2; _bd_ticket_crypt_cookie=ec8559ce82439a2f048868c510b75292; __security_server_data_status=1; sid_guard=56cd51d490ceff998424239c711e1ca7%7C1699142050%7C5183986%7CWed%2C+03-Jan-2024+23%3A53%3A56+GMT; sid_ucp_v1=1.0.0-KGJmOGM3YzVmY2YyM2E1YWJmM2M4OWU2NGZkYWRjNWJjMjA1OTFhM2YKGQj05KCv7QIQorObqgYY7zEgDDgGQPQHSAQaAmxmIiA1NmNkNTFkNDkwY2VmZjk5ODQyNDIzOWM3MTFlMWNhNw; ssid_ucp_v1=1.0.0-KGJmOGM3YzVmY2YyM2E1YWJmM2M4OWU2NGZkYWRjNWJjMjA1OTFhM2YKGQj05KCv7QIQorObqgYY7zEgDDgGQPQHSAQaAmxmIiA1NmNkNTFkNDkwY2VmZjk5ODQyNDIzOWM3MTFlMWNhNw; publish_badge_show_info=%220%2C0%2C0%2C1699142052356%22; SEARCH_RESULT_LIST_TYPE=%22single%22; my_rd=2; download_guide=%223%2F20231105%2F0%22; pwa2=%220%7C0%7C2%7C0%22; FOLLOW_LIVE_POINT_INFO=%22MS4wLjABAAAAd3HQQ1ZlJ0P3zY7M8ZkYgh46GtLIxLxXy-CzWuNFkxQ%2F1699200000000%2F0%2F0%2F1699188995501%22; FOLLOW_RED_POINT_INFO=%221%22; douyin.com; device_web_cpu_core=4; device_web_memory_size=8; architecture=amd64; webcast_local_quality=null; strategyABtestKey=%221699667242.722%22; FOLLOW_NUMBER_YELLOW_POINT_INFO=%22MS4wLjABAAAAd3HQQ1ZlJ0P3zY7M8ZkYgh46GtLIxLxXy-CzWuNFkxQ%2F1699718400000%2F1699667264117%2F1699667242287%2F0%22; csrf_session_id=e364149a9c70961dbc853914f33c6c83; EnhanceDownloadGuide=%222_1699667737_0_0_0_0%22; VIDEO_FILTER_MEMO_SELECT=%7B%22expireTime%22%3A1700280009094%2C%22type%22%3A1%7D; __ac_nonce=0654efc5400c52de03c56; __ac_signature=_02B4Z6wo00f016shqywAAIDCgKvw6UDHjderAa-AAI-PUR9cup3BG3IzQkXp01oBnypeXuw0k2O9Xy4q-Wo5pHrshiJu.oXbHWD0EDg2G87xAqNBW.QxPCpPpW3uW3r0kElwQdOGBhZ1EwZ2d1; home_can_add_dy_2_desktop=%220%22; passport_fe_beating_status=true; stream_recommend_feed_params=%22%7B%5C%22cookie_enabled%5C%22%3Atrue%2C%5C%22screen_width%5C%22%3A1600%2C%5C%22screen_height%5C%22%3A900%2C%5C%22browser_online%5C%22%3Atrue%2C%5C%22cpu_core_num%5C%22%3A4%2C%5C%22device_memory%5C%22%3A8%2C%5C%22downlink%5C%22%3A10%2C%5C%22effective_type%5C%22%3A%5C%224g%5C%22%2C%5C%22round_trip_time%5C%22%3A100%7D%22; bd_ticket_guard_client_data=eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCTlg0Z2xFclpySklSdVpDN1RKVUwrWkMzTUVocjZ4VXRBcEEvSkN4L0dSWWlJS0JpNVJoTEl3ZjhKUmVQVDBBZWZEOGgycUFDdmRJbUoyY1dEaVAvS1k9IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJzaW9uIjoxfQ%3D%3D; msToken=QApfBfGSVjiZkkhQYyUMPAZ7l8EZsYy0O9LVHMynmDWDD-bh7OPI6V82jueo3B2sgr0eE3rky3OYENc7KhWh3wTcoavvenDnU_D9Xavq47CH4HZOhTbOmdRjAoTcmZYD; tt_scid=rI3bybiwjRU9F4l.w5wm5LrbuFkaQjUU2iYSeJ6C0P-6hp1GKtXI1h.6bL7nyY1Wf737; odin_tt=2d5281363c809b67bc27fffabe8e9c47ec699f9b1fe80446b7ff9591d0205c82c3b6f2a4b6516ee2ab8cea4ea0bf07a8; msToken=3aUSbr2lpc_x3C2j7QAsKoRjk7I_HGu2xGvvcXWIkxpR3uvVYvrJ3ITso4BqXKK6GjlM93BvY5OShql9zZJ2DPZ8PMmlddR-wnfBJCWNqPijQgmniwrzOo6Y3PN9yEl1; IsDouyinActive=true',
    'origin': 'https://www.douyin.com',
    'referer': 'https://www.douyin.com/user/MS4wLjABAAAAajqbzFnQ-qph8ZgkQGwqKto4USX-0tj5TyxK_xY9GW-E58M5FTZ5vqU7fnZSfQW7?is_search=0&list_name=follow&modal_id=7299807745413336347&nt=8',
    'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    'x-secsdk-csrf-token': '000100000001b7e5720e1324f5c99b541d40b37aa99ad31c41fd9c7a7cfa547fd220f42db5981796772935b3384e',
}

params = {
    'app_name': 'aweme',
    'device_platform': 'webapp',
    'aid': '6383',
    'channel': 'channel_pc_web',
    'pc_client_type': '1',
    'version_code': '170400',
    'version_name': '17.4.0',
    'cookie_enabled': 'true',
    'screen_width': '1600',
    'screen_height': '900',
    'browser_language': 'zh-CN',
    'browser_platform': 'Win32',
    'browser_name': 'Chrome',
    'browser_version': '119.0.0.0',
    'browser_online': 'true',
    'engine_name': 'Blink',
    'engine_version': '119.0.0.0',
    'os_name': 'Windows',
    'os_version': '10',
    'cpu_core_num': '4',
    'device_memory': '8',
    'platform': 'PC',
    'downlink': '10',
    'effective_type': '4g',
    'round_trip_time': '100',
    'webid': '7297759204038493736',
    'msToken': '3aUSbr2lpc_x3C2j7QAsKoRjk7I_HGu2xGvvcXWIkxpR3uvVYvrJ3ITso4BqXKK6GjlM93BvY5OShql9zZJ2DPZ8PMmlddR-wnfBJCWNqPijQgmniwrzOo6Y3PN9yEl1',
    'X-Bogus': 'DFSzswVLWAX3jXxXtFFZBTUClLH7',
}

data = {
    'aweme_id': '7299807745413336347',
    'comment_send_celltime': '9066',
    'comment_video_celltime': '1849',
    'text': '6666',
    'text_extra': '[]',
}


def do():
    response = requests.post('https://www.douyin.com/aweme/v1/web/comment/publish', params=params, headers=headers, data=data)
    return response.text
