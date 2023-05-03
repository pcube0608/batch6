import requests

response = requests.get('https://reqres.in/api/users?page=2')

print(response.text)

res = requests.get('https://reqres.in/api/users/2')
print(res.text)

user_detail = {'name':'Minaj','job':'automation expert'}

resp = requests.post("https://reqres.in/api/users",json=user_detail)
print(resp.status_code)
print(resp.text)

ressp = requests.get("https://reqres.in/api/users/506")
print(ressp.status_code)
print(ressp.text)