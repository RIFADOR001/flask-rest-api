import requests

BASE = "http://127.0.0.1:5000/"

data = [{"likes":i, "name": "Tim "+str(i), "views":1000*i} for i in range(1, 10)]

response = requests.put(BASE + "video/1", json={"likes": 10, "name": "10", "views": 11})
# response = requests.put(BASE + "video/1", json={"likes": 10, "name": "10", "views": 11}, headers={"Content-Type":"application/json"})
# response = requests.put(BASE + "video/1", json={"likes": 10}, headers={"Content-Type":"application/json"})
for i in range(len(data)):
	response = requests.put(BASE + "video/" + str(i), json=data[i])
	print(response.json())
# try:
#     print(response.json())
# except Exception as e:
#     print(f'caught {type(e)}: ' + e)

input()
for i in range(len(data)):
	response = requests.get(BASE + "video/" + str(i))
	print(response.json())

# response = requests.get(BASE + "video/1")
# print(response.json())

response = requests.delete(BASE + "video/5")
print(response)
for i in range(len(data)):
	response = requests.get(BASE + "video/" + str(i))
	print(response.json())
# try:
#     print(response.json())
# except Exception as e:
#     print(f'caught {type(e)}: ' + e)

