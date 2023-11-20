# -*- coding: UTF-8 -*-
import requests

headers = {
    'authority': 'www.douyin.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cookie': 'ttwid=1%7Cg4KF41fihjekNryQEXmvpG1fYDsb5obmfDFscVZiSJc%7C1699141987%7C03768fe320decae9dbf492f2dc9ffc21daafb7413669d0a31842ea6a81a39262; passport_csrf_token=2e03eca908f9a8b96dc4ba8af17487e8; passport_csrf_token_default=2e03eca908f9a8b96dc4ba8af17487e8; s_v_web_id=verify_lokp9sjt_zPMuDGXl_U5hb_4W0w_BaNf_gtYsUNRg3nxw; n_mh=7MDEc7m1-J8ip_SKgJhJcC0r2OZItK8fz5Fy-cm9eQA; passport_auth_status=7bc7f3021424839b1a120a1c2c2d5616%2C; passport_auth_status_ss=7bc7f3021424839b1a120a1c2c2d5616%2C; store-region=cn-bj; store-region-src=uid; _bd_ticket_crypt_doamin=2; __security_server_data_status=1; my_rd=2; d_ticket=08e5c69c98f803ccdcdbc3952f081d36a26e5; passport_assist_user=CjzsQMMvCA04sS8VNeSnyVEFpeQ7IPfVlmIzynux8vKob7sJ5ip1kSVJzIqQeN8wmKQO2PMQrBLobOHy158aSgo8zXyc4vGH1WjPVkwdFXHwWXFxbDau3mtSRgplTg_qZBXwoTu_sApTVhq8NTkmebCTCLLEcFOeukSGsEuOELeNwQ0Yia_WVCABIgEDIoM5Pw%3D%3D; sso_uid_tt=658e8c214324722a547fa57d47226d39; sso_uid_tt_ss=658e8c214324722a547fa57d47226d39; toutiao_sso_user=c968e686ed79de7660d008aa458f62af; toutiao_sso_user_ss=c968e686ed79de7660d008aa458f62af; sid_ucp_sso_v1=1.0.0-KGQ5NGVlYTZmNzFjMzQ4ZmJlMmIwZWVlOTIyMDNjOWJiODdkNTUzMGMKHwj05KCv7QIQq6fCqgYY7zEgDDDG_7HXBTgFQPsHSAMaAmxxIiBjOTY4ZTY4NmVkNzlkZTc2NjBkMDA4YWE0NThmNjJhZg; ssid_ucp_sso_v1=1.0.0-KGQ5NGVlYTZmNzFjMzQ4ZmJlMmIwZWVlOTIyMDNjOWJiODdkNTUzMGMKHwj05KCv7QIQq6fCqgYY7zEgDDDG_7HXBTgFQPsHSAMaAmxxIiBjOTY4ZTY4NmVkNzlkZTc2NjBkMDA4YWE0NThmNjJhZg; uid_tt=3502fcefa0e924ecd8b1792293c9ff05; uid_tt_ss=3502fcefa0e924ecd8b1792293c9ff05; sid_tt=6c6900332dee80bc8e64023b0b7d137d; sessionid=6c6900332dee80bc8e64023b0b7d137d; sessionid_ss=6c6900332dee80bc8e64023b0b7d137d; LOGIN_STATUS=1; _bd_ticket_crypt_cookie=69a3ea9ef4099137c17e2d52a39106cc; sid_guard=6c6900332dee80bc8e64023b0b7d137d%7C1699779506%7C5183997%7CThu%2C+11-Jan-2024+08%3A58%3A23+GMT; sid_ucp_v1=1.0.0-KDU4NDM0ZDNjNWJkM2VhNjIxNTExZTg1NWE5ZjNmZDMxM2Y0M2IyYWQKGQj05KCv7QIQsqfCqgYY7zEgDDgFQPsHSAQaAmhsIiA2YzY5MDAzMzJkZWU4MGJjOGU2NDAyM2IwYjdkMTM3ZA; ssid_ucp_v1=1.0.0-KDU4NDM0ZDNjNWJkM2VhNjIxNTExZTg1NWE5ZjNmZDMxM2Y0M2IyYWQKGQj05KCv7QIQsqfCqgYY7zEgDDgFQPsHSAQaAmhsIiA2YzY5MDAzMzJkZWU4MGJjOGU2NDAyM2IwYjdkMTM3ZA; EnhanceDownloadGuide=%221_1700311579_0_0_0_0%22; douyin.com; device_web_cpu_core=4; device_web_memory_size=8; architecture=amd64; webcast_local_quality=null; strategyABtestKey=%221700365400.767%22; csrf_session_id=1fa38bd307370b84859c14be285ef961; FOLLOW_LIVE_POINT_INFO=%22MS4wLjABAAAAd3HQQ1ZlJ0P3zY7M8ZkYgh46GtLIxLxXy-CzWuNFkxQ%2F1700409600000%2F0%2F0%2F1700366069412%22; __ac_signature=_02B4Z6wo00f019VV81QAAIDC.t-ok-6slcPVdffAAJAVJ7qVqfJOuWnnMxiUtY2.YlNdN8FKtSlGTUDCXIW3x1GOuaP2GHVioun9DMHJfzMAylyJE2npkG2ObQZWQ.h9rWfS8azviUW0G.Ip84; publish_badge_show_info=%220%2C0%2C0%2C1700393490274%22; VIDEO_FILTER_MEMO_SELECT=%7B%22expireTime%22%3A1700998290897%2C%22type%22%3A1%7D; volume_info=%7B%22isUserMute%22%3Afalse%2C%22isMute%22%3Afalse%2C%22volume%22%3A0.5%7D; stream_player_status_params=%22%7B%5C%22is_auto_play%5C%22%3A0%2C%5C%22is_full_screen%5C%22%3A0%2C%5C%22is_full_webscreen%5C%22%3A0%2C%5C%22is_mute%5C%22%3A0%2C%5C%22is_speed%5C%22%3A1%2C%5C%22is_visible%5C%22%3A0%7D%22; msToken=aNoluV6dctD5QshVPJUL72MeZNG0k5NaU1XFYoWCodeqqO6K6NQCCGeW7Y141ibzEWMsI9WExwchcPp5RipmQ0MhYq0dvWjKbnU9R8LcoS9AAZdH772ghVesi64PsvRg; tt_scid=Z11Epu0wV.2HFXo4v1HTEma9SzLIaiseWl0oAwpB3FX890tEcfS3w6D20LoIaAql1923; download_guide=%223%2F20231119%2F0%22; pwa2=%220%7C0%7C3%7C0%22; odin_tt=43304f6cd6a38564e64d7debed719ae16defa44cd6fe932bada164c2c4e3d6232b3dcc4f52e616e4405dc1e14f9a1797; msToken=mYCBqBgkRuLEonaA5pdQRcpvTNaXaCh21irvEHRDfK0oZpgnL3yFJ8ONl_WHnRFIQ2Sqo0anaJySgCTpxlh4xv7JMDx2X1cgbTVCHRjEMX35Srhbt4Lkhlqo1f1WDzbZ; passport_fe_beating_status=true; __ac_nonce=0655a08bf00609884b64; home_can_add_dy_2_desktop=%220%22; stream_recommend_feed_params=%22%7B%5C%22cookie_enabled%5C%22%3Atrue%2C%5C%22screen_width%5C%22%3A1600%2C%5C%22screen_height%5C%22%3A900%2C%5C%22browser_online%5C%22%3Atrue%2C%5C%22cpu_core_num%5C%22%3A4%2C%5C%22device_memory%5C%22%3A8%2C%5C%22downlink%5C%22%3A1.45%2C%5C%22effective_type%5C%22%3A%5C%223g%5C%22%2C%5C%22round_trip_time%5C%22%3A500%7D%22; IsDouyinActive=true; FOLLOW_NUMBER_YELLOW_POINT_INFO=%22MS4wLjABAAAAd3HQQ1ZlJ0P3zY7M8ZkYgh46GtLIxLxXy-CzWuNFkxQ%2F1700409600000%2F0%2F0%2F1700400531846%22; bd_ticket_guard_client_data=eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCTlg0Z2xFclpySklSdVpDN1RKVUwrWkMzTUVocjZ4VXRBcEEvSkN4L0dSWWlJS0JpNVJoTEl3ZjhKUmVQVDBBZWZEOGgycUFDdmRJbUoyY1dEaVAvS1k9IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJzaW9uIjoxfQ%3D%3D',
    'referer': 'https://www.douyin.com/user/MS4wLjABAAAAgOeGnM3GZpZc1CfU7Mtl2deGwpjQyX0rq_5a_l-2SSI?is_search=0&list_name=follow&nt=0',
    'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
}

params = {
    'device_platform': 'webapp',
    'aid': '6383',
    'channel': 'channel_pc_web',
    'sec_user_id': 'MS4wLjABAAAAgOeGnM3GZpZc1CfU7Mtl2deGwpjQyX0rq_5a_l-2SSI',
    'max_cursor': '0',
    'locate_query': 'false',
    'show_live_replay_strategy': '1',
    'need_time_list': '1',
    'time_list_query': '0',
    'whale_cut_token': '',
    'cut_version': '1',
    'count': '18',
    'publish_video_strategy_type': '2',
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
    'downlink': '1.45',
    'effective_type': '3g',
    'round_trip_time': '500',
    'webid': '7297759204038493736',
    'msToken': 'mYCBqBgkRuLEonaA5pdQRcpvTNaXaCh21irvEHRDfK0oZpgnL3yFJ8ONl_WHnRFIQ2Sqo0anaJySgCTpxlh4xv7JMDx2X1cgbTVCHRjEMX35Srhbt4Lkhlqo1f1WDzbZ',
    'X-Bogus': 'DFSzswVYWLXANCMrtma87GUClL9z',
}


def do():
    response = requests.get('https://www.douyin.com/aweme/v1/web/aweme/post/', params=params, headers=headers)
    return response.text
