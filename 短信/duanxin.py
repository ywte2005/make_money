"""
@Author  : 亚博
@Time    : 2021/9/26 9:54 上午
@introduction ：
    1. 
"""
import time
import requests

from 短信.decrypt_param import de_lenovo, de_baidu

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36"
}


class Duanxin:
    def __init__(self, iphone):
        self.iphone = iphone

    # 联想
    def lenovo(self):
        """
        联想登录
        https://support.lenovo.com.cn/lenovo/wsi/Modules/DriverDownLoadServer.aspx
        :return:发送状态
        """
        data = de_lenovo()
        post_url = f"https://passport.lenovo.com.cn/wauthen2/ajaxSendVC2?msidsn={self.iphone}"
        response = requests.post(post_url, headers=headers, data=data).json()
        if response["resultCode"] == "1":
            return "联想成功"
        else:
            return "联想失败"

    # 新东方
    def new_east(self):
        """
        新东方登录
        http://login.koolearn.com/sso/m/toLogin.do?next_page=http%3A%2F%2Fm.koolearn.com
        :return:
        """
        data = {
            "mobile": self.iphone,
            "imageCode": "",
            "countryCode": "86",
            "country": "CN"
        }
        post_url = "http://login.koolearn.com/sso/m/m-sendRegisterMessage.do"
        response = requests.post(post_url, headers=headers, data=data).json()
        if response["status"] == 0:
            return "新东方成功"
        else:
            return "新东方失败"

    # 图怪兽
    def tu_ps(self):
        """
        图怪兽
        https://818ps.com/?route_id=16326265382201&route=1,&after_route=1
        :return:
        """
        get_url = f"https://818ps.com/site-api/send-tel-login-code?num={self.iphone}&codeImg=undefined"
        response = requests.post(get_url, headers=headers).json()
        if response["stat"] == 1:
            return response["msg"]
        else:
            return response["msg"]

    # 首汽约车
    def zhuanche(self):
        """
            首汽约车
            https://monline.01zhuanche.com/website/enterprise/register.html
            :return:
        """
        data = {
            "phone": "+86" + self.iphone,
            "accessSource": "CR"
        }
        post_url = "https://gw-passenger-wap.01zhuanche.com/gw-passenger-wap/zhuanche-passenger/sms/sendAuthenticationCode"
        response = requests.post(post_url, headers=headers, data=data).json()
        if response["code"] == 0:
            return "首约汽车成功"
        else:
            return "首约汽车失败"

    # 简单学习网
    def jd_learn(self):
        """
                简单学习网
                https://www.jd100.com/login?fromurl=https://www.jd100.com/
                :return:
            """
        get_url = f"https://jdapi.jd100.com/uc/v1/getSMSCode?account={self.iphone}&sign_type=1&use_type=1"
        response = requests.get(get_url, headers=headers).json()
        if response["message"] == "Success":
            return "简单学习网成功"
        else:
            return "简单学习网失败"

    # 百度加盟星
    def jm_baidu(self):
        """
        # 百度加盟星
        https://jiameng.baidu.com/project/13956680752?from=aladdin&ofr=qid%3A17799330586231067713%3Bsrcid%3A5861%3Bq%3A%E7%99%BE%E5%BA%A6%E5%8A%A0%E7%9B%9F%E6%98%9F%3Bsid%3A34651_34447_34068_31253_34654_34524_34585_34106_26350_34731_34427_34691_34677
        :return:
        """
        random, token = de_baidu()
        timestamps = str(time.time()).split(".")[0]
        response = requests.get(
            f"https://jiameng.baidu.com/portal/com/captcha?ajax=1&accessid=1312813949D0&device=pc&ctoken={token}&random={random}&timestamps={timestamps}&phone={self.iphone}&guid=13956680752").json()
        if response["msg"] == "Success":
            return "百度加盟星成功"
        else:
            return "百度加盟星失败"

    # 国美金融
    def zhuanche(self):
        """
            国美金融
            https://login.gome.com.cn/login?orginURI=http%3A%2F%2Fmyhome.gome.com.cn%2Fmember%2FmyOrder%3Fintcmp%3Djr-public01004
            :return:
        """
        data = {
            "phoneNum": self.iphone,
            "captcha": "",
            "isVoice": "false"
        }
        post_url = "https://login.gome.com.cn/doSendSMS.no"
        response = requests.post(post_url, headers=headers, data=data).json()
        return response["message"]

    # 快递100
    def kd_100(self):
        """
            快递100
            https://sso.kuaidi100.com/pcweb/view/registerpage
            :return:
        """
        data = {
            "name": self.iphone
        }
        post_url = "https://sso.kuaidi100.com/pcweb/sms/registersendsms"
        response = requests.post(post_url, headers=headers, data=data).json()
        return "快递100" + response["message"]

    def rong_cat(self):
        r = 'client=rcat_pc'
        v = str(int(time.time()))
        sign = r + v + "52WT3+Mxm5+7S4PQ4v8qj+uFW5LJ"
        data = {
            "user_phone": self.iphone,
            "Sign": sign
        }
        post_url = "https://api.rongcat.com/sms/login?client=rcat_pc"
        response = requests.post(post_url, headers=headers, data=data).json()
        return "容猫" + response["message"]




if __name__ == '__main__':
    pass
