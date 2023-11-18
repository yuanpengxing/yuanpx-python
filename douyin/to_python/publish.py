# -*- coding: UTF-8 -*-
import requests

headers = {
    'authority': 'www.douyin.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'bd-ticket-guard-client-data': 'eyJ0c19zaWduIjoidHMuMS4wNTUxODkwNjRhNTllNWY4YTg2MzJjZDZhMzkyYzI3YTIyZjZmMDU1NThmMmQxYmE1ODA5NDA4NWM4MmRmYzRkYzRmYmU4N2QyMzE5Y2YwNTMxODYyNGNlZGExNDkxMWNhNDA2ZGVkYmViZWRkYjJlMzBmY2U4ZDRmYTAyNTc1ZCIsInJlcV9jb250ZW50IjoidGlja2V0LHBhdGgsdGltZXN0YW1wIiwicmVxX3NpZ24iOiJNRVVDSVFDMTlZWDJhTGk4KzMzQmxkbDluWUoxcWV5VjBLZ2JoNVQzWXRuYkhucG9ud0lnSWt3aE5WTVBNejRvVFdTeDlyTjFkalQvWlppVldiNTByN3VWc2MxQ1l0az0iLCJ0aW1lc3RhbXAiOjE3MDAzMTE1Nzl9',
    'bd-ticket-guard-iteration-version': '1',
    'bd-ticket-guard-ree-public-key': 'BNX4glErZrJIRuZC7TJUL+ZC3MEhr6xUtApA/JCx/GRYiIKBi5RhLIwf8JRePT0AefD8h2qACvdImJ2cWDiP/KY=',
    'bd-ticket-guard-version': '2',
    'bd-ticket-guard-web-version': '1',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'cookie': 'ttwid=1%7Cg4KF41fihjekNryQEXmvpG1fYDsb5obmfDFscVZiSJc%7C1699141987%7C03768fe320decae9dbf492f2dc9ffc21daafb7413669d0a31842ea6a81a39262; passport_csrf_token=2e03eca908f9a8b96dc4ba8af17487e8; passport_csrf_token_default=2e03eca908f9a8b96dc4ba8af17487e8; s_v_web_id=verify_lokp9sjt_zPMuDGXl_U5hb_4W0w_BaNf_gtYsUNRg3nxw; n_mh=7MDEc7m1-J8ip_SKgJhJcC0r2OZItK8fz5Fy-cm9eQA; passport_auth_status=7bc7f3021424839b1a120a1c2c2d5616%2C; passport_auth_status_ss=7bc7f3021424839b1a120a1c2c2d5616%2C; store-region=cn-bj; store-region-src=uid; _bd_ticket_crypt_doamin=2; __security_server_data_status=1; my_rd=2; volume_info=%7B%22isUserMute%22%3Afalse%2C%22isMute%22%3Afalse%2C%22volume%22%3A0.5%7D; publish_badge_show_info=%220%2C0%2C0%2C1699773792954%22; download_guide=%223%2F20231112%2F0%22; d_ticket=08e5c69c98f803ccdcdbc3952f081d36a26e5; FORCE_LOGIN=%7B%22videoConsumedRemainSeconds%22%3A180%7D; passport_assist_user=CjzsQMMvCA04sS8VNeSnyVEFpeQ7IPfVlmIzynux8vKob7sJ5ip1kSVJzIqQeN8wmKQO2PMQrBLobOHy158aSgo8zXyc4vGH1WjPVkwdFXHwWXFxbDau3mtSRgplTg_qZBXwoTu_sApTVhq8NTkmebCTCLLEcFOeukSGsEuOELeNwQ0Yia_WVCABIgEDIoM5Pw%3D%3D; sso_uid_tt=658e8c214324722a547fa57d47226d39; sso_uid_tt_ss=658e8c214324722a547fa57d47226d39; toutiao_sso_user=c968e686ed79de7660d008aa458f62af; toutiao_sso_user_ss=c968e686ed79de7660d008aa458f62af; sid_ucp_sso_v1=1.0.0-KGQ5NGVlYTZmNzFjMzQ4ZmJlMmIwZWVlOTIyMDNjOWJiODdkNTUzMGMKHwj05KCv7QIQq6fCqgYY7zEgDDDG_7HXBTgFQPsHSAMaAmxxIiBjOTY4ZTY4NmVkNzlkZTc2NjBkMDA4YWE0NThmNjJhZg; ssid_ucp_sso_v1=1.0.0-KGQ5NGVlYTZmNzFjMzQ4ZmJlMmIwZWVlOTIyMDNjOWJiODdkNTUzMGMKHwj05KCv7QIQq6fCqgYY7zEgDDDG_7HXBTgFQPsHSAMaAmxxIiBjOTY4ZTY4NmVkNzlkZTc2NjBkMDA4YWE0NThmNjJhZg; uid_tt=3502fcefa0e924ecd8b1792293c9ff05; uid_tt_ss=3502fcefa0e924ecd8b1792293c9ff05; sid_tt=6c6900332dee80bc8e64023b0b7d137d; sessionid=6c6900332dee80bc8e64023b0b7d137d; sessionid_ss=6c6900332dee80bc8e64023b0b7d137d; FOLLOW_LIVE_POINT_INFO=%22MS4wLjABAAAAd3HQQ1ZlJ0P3zY7M8ZkYgh46GtLIxLxXy-CzWuNFkxQ%2F1699804800000%2F0%2F0%2F1699780104320%22; LOGIN_STATUS=1; _bd_ticket_crypt_cookie=69a3ea9ef4099137c17e2d52a39106cc; sid_guard=6c6900332dee80bc8e64023b0b7d137d%7C1699779506%7C5183997%7CThu%2C+11-Jan-2024+08%3A58%3A23+GMT; sid_ucp_v1=1.0.0-KDU4NDM0ZDNjNWJkM2VhNjIxNTExZTg1NWE5ZjNmZDMxM2Y0M2IyYWQKGQj05KCv7QIQsqfCqgYY7zEgDDgFQPsHSAQaAmhsIiA2YzY5MDAzMzJkZWU4MGJjOGU2NDAyM2IwYjdkMTM3ZA; ssid_ucp_v1=1.0.0-KDU4NDM0ZDNjNWJkM2VhNjIxNTExZTg1NWE5ZjNmZDMxM2Y0M2IyYWQKGQj05KCv7QIQsqfCqgYY7zEgDDgFQPsHSAQaAmhsIiA2YzY5MDAzMzJkZWU4MGJjOGU2NDAyM2IwYjdkMTM3ZA; strategyABtestKey=%221700295137.34%22; pwa2=%220%7C0%7C1%7C0%22; douyin.com; device_web_cpu_core=4; device_web_memory_size=8; architecture=amd64; webcast_local_quality=null; FOLLOW_NUMBER_YELLOW_POINT_INFO=%22MS4wLjABAAAAd3HQQ1ZlJ0P3zY7M8ZkYgh46GtLIxLxXy-CzWuNFkxQ%2F1700323200000%2F0%2F1700311513765%2F0%22; VIDEO_FILTER_MEMO_SELECT=%7B%22expireTime%22%3A1700916313789%2C%22type%22%3A1%7D; csrf_session_id=1fa38bd307370b84859c14be285ef961; __ac_nonce=06558b1da006b63639fda; stream_player_status_params=%22%7B%5C%22is_auto_play%5C%22%3A0%2C%5C%22is_full_screen%5C%22%3A0%2C%5C%22is_full_webscreen%5C%22%3A0%2C%5C%22is_mute%5C%22%3A0%2C%5C%22is_speed%5C%22%3A1%2C%5C%22is_visible%5C%22%3A0%7D%22; __ac_signature=_02B4Z6wo00f01qzFWygAAIDCLMehahOP62as5V-AAM52qItq0yemVdzp6x2XJKXaNdo04o1aadtdJZI76a2QiUMq8hkFQ8v7fxxtcPwbD8x4Bg9P7SJVDTAe3vXRUbq0.8Y7RELepvI6y.L2ed; stream_recommend_feed_params=%22%7B%5C%22cookie_enabled%5C%22%3Atrue%2C%5C%22screen_width%5C%22%3A1600%2C%5C%22screen_height%5C%22%3A900%2C%5C%22browser_online%5C%22%3Atrue%2C%5C%22cpu_core_num%5C%22%3A4%2C%5C%22device_memory%5C%22%3A8%2C%5C%22downlink%5C%22%3A10%2C%5C%22effective_type%5C%22%3A%5C%224g%5C%22%2C%5C%22round_trip_time%5C%22%3A50%7D%22; passport_fe_beating_status=true; home_can_add_dy_2_desktop=%221%22; bd_ticket_guard_client_data=eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCTlg0Z2xFclpySklSdVpDN1RKVUwrWkMzTUVocjZ4VXRBcEEvSkN4L0dSWWlJS0JpNVJoTEl3ZjhKUmVQVDBBZWZEOGgycUFDdmRJbUoyY1dEaVAvS1k9IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJzaW9uIjoxfQ%3D%3D; msToken=b5vbUxS80mb59jATLHDZ9gNHk1zoaGYuxKBBQe80b-C-gqt5ajP4xcq5rKN030ByV5qNW2Ax2bnQG3HnS4lV2g93Q1W0_2O-uhgSznREdWvJqRSQEozG4WJI9BObNrE=; msToken=IYQ_dAvP4dCG-kpjAsTSfw7o_Ltc8oJsYzwf9mL5Ox3xVrpb1YuzymvgZQT4ug05eYr9m6l4G55vPEgzRfrCxtoE691lTZ6VyOSDQHZzahor7D4JtSbGwPUMD34CFM8=; odin_tt=8e71fb183234421144fa350718328d5758da0fd1e1a2f862a6b49f2fa62b00364b23c23d2a088ad80c0fe5ded6c566d6; tt_scid=AwHnnGOKqA6ECO0XpT6zfv67J4KmlhO-HmdQDWOLIwD.5COBnMbiWeTAcUTd9ggf9168; IsDouyinActive=true',
    'origin': 'https://www.douyin.com',
    'referer': 'https://www.douyin.com/user/MS4wLjABAAAAgOeGnM3GZpZc1CfU7Mtl2deGwpjQyX0rq_5a_l-2SSI?is_search=0&list_name=follow&modal_id=7302666376626326793&nt=0',
    'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    'x-secsdk-csrf-token': '000100000001030853e55508a5e92ee10271fbbb911e95a3bf25abb3f9e88ae76fcfcae408471798b854cf02f641',
}

data = {
    'aweme_id': '7302666376626326793',
    'comment_send_celltime': '10127',
    'comment_video_celltime': '952',
    'text': '6666',
    'text_extra': '[]',
}


def do():
    response = requests.post(
        'https://www.douyin.com/aweme/v1/web/comment/publish?app_name=aweme&device_platform=webapp&aid=6383&channel=channel_pc_web&pc_client_type=1&version_code=170400&version_name=17.4.0&cookie_enabled=true&screen_width=1600&screen_height=900&browser_language=zh-CN&browser_platform=Win32&browser_name=Chrome&browser_version=119.0.0.0&browser_online=true&engine_name=Blink&engine_version=119.0.0.0&os_name=Windows&os_version=10&cpu_core_num=4&device_memory=8&platform=PC&downlink=10&effective_type=4g&round_trip_time=50&webid=7297759204038493736&msToken=IYQ_dAvP4dCG-kpjAsTSfw7o_Ltc8oJsYzwf9mL5Ox3xVrpb1YuzymvgZQT4ug05eYr9m6l4G55vPEgzRfrCxtoE691lTZ6VyOSDQHZzahor7D4JtSbGwPUMD34CFM8=&X-Bogus=DFSzswVLexyK-xxXtmJ9UM9WX7jW',
        headers=headers,
        data=data,
    )
    return response.text
