from django.dispatch import Signal, receiver
import email.message
import smtplib
from datetime import datetime

order_signal = Signal()

@receiver(order_signal)
def order_signal_callback(sender, **kwargs):
    try:
        msg=email.message.EmailMessage()
        msg["From"]="selltreeandseed@gmail.com"
        msg["To"]="selltreeandseed@gmail.com"
        msg["Subject"]="新訂單"+datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        msg.set_content(f'{kwargs["firstname"]},{kwargs["sex"]},{kwargs["producttype"]}:{kwargs["count"]},電話：{kwargs["tex"]},備註：{kwargs["ps"]}')
        server=smtplib.SMTP_SSL("smtp.gmail.com",465)
        server.login("selltreeandseed@gmail.com","dcvh jduu dpjs XXXX")
        server.send_message(msg)
        server.close()
    except:
        server.close()
        pass
    try:
        msg=email.message.EmailMessage()
        msg["From"]="selltreeandseed@gmail.com"
        msg["To"]=kwargs['mailaddress']
        msg["Subject"]="訂購成功通知"
        msg.set_content(f'我們已收到您於官網下訂{kwargs["producttype"]}:{kwargs["count"]},備註內容：{kwargs["ps"]}。我們會盡快與您電話聯繫，謝謝。')
        server=smtplib.SMTP_SSL("smtp.gmail.com",465)
        server.login("selltreeandseed@gmail.com","dcvh jduu dpjs XXXX")
        server.send_message(msg)
        server.close()
        return f'訂購成功,近期會有專人與您聯繫(已成功寄mail至{kwargs["mailaddress"]},如提供錯誤mail將無法送達)'
    except:
        server.close()
        pass


