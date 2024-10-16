# The Requests library in Python is one of the integral parts of Python for making HTTP requests to a specified URL



import requests as re

req = re.get("https://x.com/home")
print(req.text)