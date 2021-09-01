import requests
import json


def get_data():
   all_apts = []
   with open("apt_list", "r") as apts:
      while True:
         line = apts.readline()
         if not line:
            break
         all_apts.append(line)
   # for i in range(len(all_apts)):
   req = "https://otx.alienvault.com/api/v1/search/pulses?limit=100&page=1&sort=modified&q={}".format(all_apts[2])
   print(req)
   headers = {"X-OTX-API-KEY":""}  # WRITE YOUR API KEY TO HERE
   response = requests.get(req, headers=headers).json()
   # response = requests.get("https://otx.alienvault.com/api/v1/pulses/subscribed?page=1", headers=headers).json()
   # /api/v1/pulses/{pulse_id}/subscribe

   return response

print(get_data())

# # apt_name = 
# all_apts = []
# count = 0
# with open("apt_list", "r") as apts:
#    while True:
#       count = count + 1
#       line = apts.readline()
#       if not line:
#          break
#       all_apts.append(line)
# print(str(all_apts[1]))

# # print(get_data())


def filter_by_name():
   headers = {"X-OTX-API-KEY":"6de1b0d2b11f4e2a09f499aafad89cecc2d571fff44b7b83a80808c7633ac1be"}
   a = get_data()
   # print(a)
   for i in range(len(a["results"])):
      name = a["results"][i]["name"]
      id = a["results"][i]["id"]
      if "ioc" in name or "IOC" in name:
         print(name,id)
         choose = input("Do you wanna follow it? (y/n) : ")
         if choose == "y":
            req = "https://otx.alienvault.com/api/v1/pulses/{}/subscribe".format(id)
            print(req)
            requests.get(req, headers=headers)
         elif choose == "n":
            continue
      # print(name)
# filter_by_name()

# def data_to_file():
#     with open("search.json",'w') as data_file:
#        data_file.write(json.dumps(get_data()))

# data_to_file()