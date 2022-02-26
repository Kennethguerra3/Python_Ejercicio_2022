import request
url="http://api.fixer.io/latest?base=USD"
response = requests.post(url)
print response.json()
