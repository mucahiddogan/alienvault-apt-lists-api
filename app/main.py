from fastapi import FastAPI, Request
# from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
# from flask import Flask,render_template
import os
import requests
import json
import pandas as pd
from urllib3 import request 
from datetime import datetime
import numpy
import uvicorn


app = FastAPI()
templates = Jinja2Templates(directory="app/templates")
app.mount("/static", StaticFiles(directory="app/static"), name="static")


def get_data():
    headers = {"X-OTX-API-KEY":""} # WRITE YOUR API KEY TO HERE
    response = requests.get("https://otx.alienvault.com/api/v1/pulses/subscribed?limit=10000", headers=headers).json()
    return response


@app.get("/")
async def home(request: Request):
    a = get_data()
    total_ioc = 0
    ioc_list = []
    last = 1
    for i in range(len(a)-3):
        iocs= a["results"][i]["indicators"]
        for j in range(len(iocs)):
            date = datetime.strptime(str(iocs[j]["created"].split("T")[0]), '%Y-%m-%d')
            today = datetime(2021,3,3)
            # today = datetime.now()
            if date > today:
                ioc_list.extend([[iocs[j]["id"], a["results"][i]["name"]]])
                last = last + i
            else:
                break
        total_ioc= total_ioc + j
    ioc_list.append([(total_ioc+1)])
    del ioc_list[0:-3]
    return templates.TemplateResponse("home.html", {"request": request, "list": ioc_list})

@app.get("/show_json")
def show_json():
    return get_data()

def data_to_file():
    with open("data.json",'w',encoding = 'utf-8') as data_file:
       data_file.write(json.dumps(get_data(), indent=3, sort_keys=True))


@app.get("/list_todays_ioc")
def list_todays_ioc():
    a = get_data()
    total_ioc = 0
    ioc_list = []
    last = 1
    for i in range(len(a["results"])):
        iocs= a["results"][i]["indicators"]
        for j in range(len(iocs)):
            date = datetime.strptime(str(iocs[j]["created"].split("T")[0]), '%Y-%m-%d')
            today = datetime(2021,3,3)
            # today = datetime.now()
            if date > today:
                # print(j, "Today_released IOC's ID: ", iocs[j]["id"])
                # print("Today released IOC's group name: ", a["results"][i]["name"])
                ioc_list.extend([[iocs[j]["id"], a["results"][i]["name"]]])
                last = last + i
            else:
                break

        total_ioc= total_ioc + j
        
    # print("Total released: ", (total_ioc+1))
    ioc_list.append([(total_ioc+1),last])
    # return render_template("list_todays_ioc.html", list = ioc_list)
    return ioc_list


@app.get("/top_five_apt")
def top_five_apt():
    a = get_data()
    count = []
    array_to_send = []
    for i in range(len(a["results"])):
        iocs = a["results"][i]["indicators"]
        count.extend([[len(iocs), a["results"][i]["name"]]])
    
    sorted_apt = pd.DataFrame(count).sort_values(by=0,ascending = False).to_numpy()
    for i in range(5):
        # print(i+1,". apt grubu: ", sorted_apt[i][1], "\t\tYayinlanan toplam IOC: ", sorted_apt[i][0])
        array_to_send.extend([[(i+1),sorted_apt[i][1], sorted_apt[i][0]]])
    # return render_template("top_five_apt.html", list=array_to_send)
    return array_to_send



@app.get("/list_all_apt_names")
def list_all_apt_names():
    a = get_data()
    data = []
    for i in range(len(a["results"])):
        # print(a["results"][i]["name"])
        data.extend([a["results"][i]["name"]])
    # return render_template("list_all_apt_names.html", list=data)
    return data


@app.get("/list_apt_and_ioc_infos")
def list_apt_and_ioc_infos():
    a = get_data()
    array_to_send = []
    for i in range(len(a["results"])):
        print(i)
        iocs= a["results"][i]["indicators"]
        # print("Description: ", a["results"][i]["description"])
        # print("APT Group ID: ", a["results"][i]["id"])
        
        for j in range(len(iocs)):
            # print("APT Group: ", a["results"][i]["name"])
            # print("Description: ", a["results"][i]["description"])
            # print("APT Group ID: ", a["results"][i]["id"])
            # print("IOC ID: ", iocs[j]["id"])
            # print("Created at: ", iocs[j]["created"])
            # print("Source: ", a["results"][i]["author_name"])
            # print("Indicator Address: ", iocs[j]["indicator"])
            # print("Title: ", iocs[j]["title"])
            # print("Type(or hash): ", iocs[j]["type"])
            array_to_send.extend([[a["results"][i]["name"],a["results"][i]["description"],a["results"][i]["id"],iocs[j]["id"], iocs[j]["created"], a["results"][i]["author_name"],
            iocs[j]["indicator"], iocs[j]["title"], iocs[j]["type"]]])
        # print(array_to_send)
        # print("\n")
    # print(array_to_send)
    # return render_template("list_apt_and_ioc_infos.html", list=array_to_send)
    return array_to_send

@app.get("/list_only_iocs")
def list_only_iocs():
    a = get_data()
    list = []
    for i in range(len(a["results"])):
        iocs= a["results"][i]["indicators"]

        for j in range(len(iocs)):
            # print("IOC ID: ", iocs[j]["id"])
            # print("APT Group: ", a["results"][i]["name"])
            # print("j: ",j , "\n")
            list.extend([[iocs[j]["id"], a["results"][i]["name"]]])
        # print(list)
        pa = pd.DataFrame(list)
        print(pa)
    # return render_template("list_only_iocs.html", list=list)
    return list
