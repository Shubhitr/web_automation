import json
import requests


headers = {
            'accept': '*/*',
            'accept-language': 'en',
            'content-language': 'en',
            'content-type': 'application/json',
            'origin': 'https://d1wj41cizynvll.cloudfront.net',
            'priority': 'u=1, i',
            'referer': 'https://d1wj41cizynvll.cloudfront.net/',
            'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Linux"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'cross-site',
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
        }

base_url = "https://1l7gz3lxqg.execute-api.us-east-1.amazonaws.com/"
user, password = ("superadminqa@citadel.com","Citadel@123" )
login_endpoint = "qa/login"
get_endpoint = f"qa/fetch_emps_in_division?limit=10&skip=0"

payload = {'email': user, 'password': password, 'access': "web"}
print(type(payload))

# Serializing the payload
print(json.dumps(payload))

response = requests.post(url=base_url+login_endpoint, headers=headers, data=json.dumps(payload))

# Deserializing the response
# deserialized_response = json.loads(response.text)
deserialized_response = response.json()
# print(deserialized_response)
headers["authorization"] = f"Bearer {deserialized_response.get('AuthenticationResult').get('AccessToken')}"
# print(headers)
#
# # Dump
# with open("response.json", 'w') as f:
#     json.dump(response.json(), f, indent=4)
#
# with open("response.json", 'r') as f:
#     print(type(json.loads(f.read())))
