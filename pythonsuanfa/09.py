"""
模拟Linux用户登录。
> 验证账号和密码，若失败则延迟三秒输出错误信息。
"""
import time

d = {'work': "1234", 'abc': "666"}
user = input('请输入账户\n')
pwd = input('请输入密码\n')
if user not in d:
    print('账户输入错误')
elif d['work'] != pwd:
    time.sleep(3)
    print('密码输入错误')
else:
    print('欢迎登陆linux系统')
