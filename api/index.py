# --- imports ---#
import requests
import json
import fonction


#--- code ---#

url= "https://jsonplaceholder.typicode.com/todos/1"
users = [1,3,5]
#for user in users:
    #url= "https://jsonplaceholder.typicode.com/todos/"+ str(user)



apiResult=fonction.getApi(url)
print(json.dumps(apiResult))
print(fonction.verifyUrl(url))