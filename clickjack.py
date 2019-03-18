#To get a website's info...
import requests
domain = "https://www.hackthissite.org/"
request = requests.get(domain).headers

print(request)