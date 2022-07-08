"""
   ┌─┐       ┌─┐ + +
┌──┘ ┴───────┘ ┴──┐++
│                 │
│       ───       │++ + + +
███████───███████ │+
│                 │+
│       ─┴─       │
│                 │
└───┐         ┌───┘
    │         │
    │         │   + +
    │         │
    │         └──────────────┐
    │                        │
    │                        ├─┐
    │                        ┌─┘
    │                        │
    └─┐  ┐  ┌───────┬──┐  ┌──┘  + + + +
      │ ─┤ ─┤       │ ─┤ ─┤
      └──┴──┘       └──┴──┘  + + + +
             神兽保佑
            代码无BUG!
            
@Author  : 亚博
@Time    : 2022/3/25 10:09
@introduction ：
    1. 
"""
import re
import requests
import time


class KuGouMusic():
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"
        }
        self.music_list_url = "https://mac.kugou.com/v2/musicol/yueku/v1/rank/home/{}-{}.html"
        self.music_details_url = "https://wwwapi.kugou.com/yy/index.php?r=play/getdata&hash={}&dfid=1bnGZ40O8OmY2Js0Hv3vMZtI&appid=1014&mid=cec251c4d3056ace2f406925d9ac198b&album_id={}"

    def _send_request(self, url, response_type=0):
        response_ = requests.get(url, headers=self.headers,timeout=10)
        time.sleep(2)
        if response_type == 1:
            return response_.content
        elif response_type == 2:
            return response_.json()
        else:
            return response_.text

    def download_music(self, music_name, download_url):
        with open("./file/" + music_name + ".mp3", "wb") as f:
            music_content = self._send_request(download_url, 1)
            f.write(music_content)

    def parse_detail_info(self, json_data):
        return json_data["data"]['play_url']

    def parse_list_info(self, html_text):
        music_list = eval(re.findall('global.features = (.*?);', html_text, re.I | re.M)[0])
        for music_info in music_list:
            music_name = music_info['filename']
            # hash
            hash = music_info["hash"]
            # 专辑ID
            album_id = music_info["album_id"]
            details_url = self.music_details_url.format(hash, album_id)
            try:
                json_data = self._send_request(details_url, 2)
            except:
                continue
            download_url = self.parse_detail_info(json_data)
            self.download_music(music_name, download_url)
            print(music_name, "下载成功")

        return music_list

    def run(self):
        for id in ('42808',):
            for page in range(1, 5):
                print("当前ID:"+id+"页数："+str(page),)
                html_text = self._send_request(self.music_list_url.format(page, id))
                self.parse_list_info(html_text)


if __name__ == '__main__':
    kg = KuGouMusic()
    kg.run()
