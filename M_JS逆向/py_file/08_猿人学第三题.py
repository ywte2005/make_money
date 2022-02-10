import requests
from collections import Counter


class MyHeaders(object):
    def items(self):
        return (('Host', 'match.yuanrenxue.com'),
                ('Pragma', 'no-cache'),
                ('Connection', 'keep-alive'),
                ('Accept', 'application/json, text/javascript, */*; q=0.01'),
                ('User-Agent', 'yuanrenxue.project'),
                ('X-Requested-With', 'XMLHttpRequest'),
                ('Referer', 'http://match.yuanrenxue.com/match/3'),
                ('Origin', 'http://match.yuanrenxue.com'),
                ('Cache-Control', 'no-cache'),
                ('Accept-Encoding', 'gzip, deflate'),
                ('Accept-Language', 'zh-CN,zh;q=0.9,en;q=0.8'),)


def get_json(page):
    logo_url = "https://match.yuanrenxue.com/jssm"
    api_url = "http://match.yuanrenxue.com/api/match/3?page={}".format(page)
    resp = requests.get(logo_url, headers=MyHeaders())
    response = requests.get(api_url, cookies=resp.cookies.get_dict(), headers=MyHeaders())
    return response.json()


if __name__ == '__main__':
    data_list = []
    for page in range(1, 6):
        json = get_json(page)
        data = json.get('data')
        for d in data:
            data_list.append(d['value'])

    top_1 = Counter(data_list).most_common(1)[0]
    print("出现频率最高的申请号：", top_1[0])
