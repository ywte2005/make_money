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
邮件发送脚本
"""
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr


class WBYiSmtp:
    def __init__(self):
        self.my_sender = "2117440168@qq.com"
        self.my_password = "fdoogxymiazbfajc"
        self.user = "l_inyue@163.com"

    def send_email(self, content):
        ret = True
        try:
            msg = MIMEText(content, "plain", "utf-8")
            msg["From"] = formataddr(["QQ账号", self.my_sender])
            msg["To"] = formataddr(["反馈信息", self.user])
            msg['Subject'] = "bbs监控信息"  # 邮件的主题，也可以说是标题
            server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
            server.login(self.my_sender, self.my_password)  # 括号中对应的是发件人邮箱账号、邮箱密码
            server.sendmail(self.my_sender, [self.user, ], msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
            server.quit()  # 关闭连接
        except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
            ret = False

        return ret


if __name__ == '__main__':

    ret = WBYiSmtp().send_email("这里是内容")
    if ret:
        print("邮件发送成功")
    else:
        print("邮件发送失败")
