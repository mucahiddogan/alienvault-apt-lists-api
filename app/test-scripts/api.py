import os
import requests
import json
import pandas as pd
from urllib3 import request 
from datetime import datetime
import numpy

# from pandas import json_normalize



def get_data():
    headers = {"X-OTX-API-KEY":""} # WRITE YOUR API KEY TO HERE
    response = requests.get("https://otx.alienvault.com/api/v1/pulses/subscribed?page=1", headers=headers).json()
    return response

# a = json.loads(get_data().data.decode("utf-8"))
# df = pd.json_normalize(get_data())
# print(df.head(10))
# with open("asd.txt",'w',encoding = 'utf-8') as data_file:
#     data_file.write(str(df.head(10)))

def data_to_file():
    with open("data.json",'w',encoding = 'utf-8') as data_file:
       data_file.write(json.dumps(get_data(), indent=3, sort_keys=True))
data_to_file()

# su_an_yaptigim_endpoint_bugunki_ioc_kac_farkli_apt_top_5_apt + tum_endpointleri_refactor_et
def list_todays_ioc():
    a = get_data()
    total_ioc = 0
    for i in range(len(a)-3):
        iocs= a["results"][i]["indicators"]
        for j in range(len(iocs)):
            # print("Created at: ", iocs[j]["created"])
            date = datetime.strptime(str(iocs[j]["created"].split("T")[0]), '%Y-%m-%d')
            today = datetime(2021,3,3)
            # today = datetime.now()
            if date > today:

                print(j, "Today_released IOC's ID: ", iocs[j]["id"])
                print("Today released IOC's group name: ", a["results"][i]["name"])
                # print("new")
            else:
                break

        total_ioc= total_ioc + j
    print("Total released: ", (total_ioc+1))
            # print(date)

def top_five_apt():
    a = get_data()
    count = []

    for i in range(len(a)-3):
        iocs = a["results"][i]["indicators"]
        count.extend([[len(iocs), a["results"][i]["name"]]])
    
    sorted_apt = pd.DataFrame(count).sort_values(by=0,ascending = False).to_numpy()
    
    # print(sorted_apt)
    for i in range(3):
        print(i+1,". apt grubu: ", sorted_apt[i][1], "\t\tYayinlanan toplam IOC: ", sorted_apt[i][0])
    # print(count)


def list_all_apt_names():
    a = get_data()
    # print(a["results"][i]["name"])
    for i in range(len(a)-3):
        print(a["results"][i]["name"])

def list_apt_and_ioc_infos():
    a = get_data()
    for i in range(len(a)-3):
        print(i)
        iocs= a["results"][i]["indicators"]
        # print("APT Group: ", a["results"][i]["name"])
        print("Description: ", a["results"][i]["description"])
        print("APT Group ID: ", a["results"][i]["id"])
        
        # print(a["results"][i]["indicators"]["id"])
        for j in range(len(iocs)):
            print("APT Group: ", a["results"][i]["name"])
            print("IOC ID: ", iocs[j]["id"])
            print("Created at: ", iocs[j]["created"])
            print("Source: ", a["results"][i]["author_name"])
            print("Indicator Address: ", iocs[j]["indicator"])
            print("Title: ", iocs[j]["title"])
            print("Type(or hash): ", iocs[j]["type"])
            print("j: ",j , "\n")
        print("\n")

def list_only_iocs():
    a = get_data()
    for i in range(len(a)-3):
        iocs= a["results"][i]["indicators"]

        for j in range(len(iocs)):
            print("IOC ID: ", iocs[j]["id"])
            print("APT Group: ", a["results"][i]["name"])
            print("j: ",j , "\n")

# data_to_file()
# su_an_yaptigim_endpoint_bugunki_ioc_kac_farkli_apt_top_5_apt + tum_endpointleri_refactor_et
# list_todays_ioc()
# list_todays_ioc()
# list_all_apt_names()
# top_five_apt()
# list_apt_and_ioc_infos()
# list_only_iocs()



# print(get_data()["results"])

    # bugün ki ioc sayıları
    # kaç farklı apt grubu release yapmış
    # günlük top 5 apt grubu

    # çektiğin tüm apt gruplarını listele

    # apt grupları - IOC eşlenmiş biçimde göster
  
    # tüm IOC leri listele
    # ioclere ait ip adress, kaynak (nereden alınmış bu veri), hash, hangi apt grubu, tarih

    # tüm iocleri listele

# class AptGroup(BaseModel):
#     name: str # direkt name
#     AuthorName: str # kaynak
#     special_id: str # apt grubu uniq idsi
#     description: str # description
#     last_modified: str # last_modified
#     iocs: str # iocler
