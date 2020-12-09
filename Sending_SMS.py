import requests

url = "https://www.fast2sms.com/dev/bulk"

querystring = {"authorization":"awYByzS5f8uKU0kM1WLcAO6jsvtgZPrR2mDJFeNn9dGCQolixhPSNu48rvn5FkX2qiLZUJ3pxMmRQG7a","sender_id":"FSTSMS","message":"This is test message from Vishal","language":"english","route":"p","numbers":"8208123899"}

headers = {
    'cache-control': "no-cache"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)