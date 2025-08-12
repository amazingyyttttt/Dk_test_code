# 需求：登录成功

# 导包
import requests

# 发送请求
url = "https://kdtx-test.itheima.net/api/login"
header_data = {
    "Content-Type": "application/json"
}
login_data = {
    "username": "admin",
    "password": "HM_2023_test",
    "code": "2",
    "uuid": "a2efdea715d5473488306ab6bf60e945"
}
# {username: "admin", password: "HM_2023_test", code: "2", uuid: "3a64ab6717f44f71af9c2d0af2c58168"}
response = requests.post(url=url, headers=header_data, json=login_data)

# 查看响应
print(response.status_code)
print(response.json())

