# --- imports ---#
import requests
import json


#--- code ---#

#for user in users:
    #url= "https://jsonplaceholder.typicode.com/todos/"+ str(user)

def getApi(url):
    isSuccess = False
    result ={}
    data ={}
    try:
        req = requests.get(url)
        if req.status_code == 200:
            #print(req.status_code)
            data = req.text
            isSuccess = True
            result["message"]="Donnée recuperee avec succes"
            #result["data"]="data"
        else:
            #print('impossible de recuperer les donnees')
            isSuccess= False
            result["message"]="impossible de recuperer les données"
    except:
        #print(404)
        isSuccess=False
        result["message"]="Url entrée n existe pas"
    result["data"]=data
    result["success"]= isSuccess
    return result

    
def verifyUrl(url):
    
    try:
        reponse = requests.get(url)
        
        return True
       
    except:
        return False