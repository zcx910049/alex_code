# 定义任务函数
from celery import task
from django.conf import settings
from django.core.mail import send_mail
import time

@task
def send_register_success_mail(username,password,email):
    """给用户的注册邮箱发送邮件"""
    # 发送邮件给用户保存到用户的注册邮箱
    message = '<h1>欢迎您成为天天生鲜的注册会员</h1>请记好你的注册信息:<br/>用户名:' + username + '<br/>密码' + password
    send_mail('欢迎信息', '', settings.EMAIL_FROM, [email], html_message=message)
    time.sleep(5)
