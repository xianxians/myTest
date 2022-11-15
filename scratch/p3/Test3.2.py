import requests

res = requests.get('https://www.xiaozhu.com/')
print(res.text)

url = 'https://m.xxxxx.com/xxxx/xxxx/common/api/user/smsLogin'
new_data = {
    "appCode": "1011",
    "mobile": "13711110000",
    "code": "1111"
}
new_haeders = {
    'appCode': '1011',
    'token': 'xxxxxxxxxxxxxxxxxxxxxxxxx',
    'groupId': '26'
}
res = requests.post(url, headers=new_haeders, json=new_data)
print(res.json())
