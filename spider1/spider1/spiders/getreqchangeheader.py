import requests

url = "http://172.18.58.80/snow/"
r=requests.get(url)
print(r.text)


# Display an "OK" return status code
print("Status code:")
print("\t *", r.status_code)

# Display the website header
h=requests.head(url)
print("header:")
print("**********")
for x in h.headers:
    print("\t",x,":",h.headers[x])
print("**********")


# Modify the Header user-agent to display "Mobile"
headers = {
    'User-Agent' : 'Mobile'
}
url2 = 'http://172.18.58.80/snow/'
rh = requests.get(url2, headers=headers)
print(rh.text)
