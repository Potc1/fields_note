import requests
from datetime import datetime

import urllib.request
import time
import pandas as pd
import streamlit as st

from pr5 import Field
from pr5 import Processing
import json


URL = "https://script.google.com/macros/s/AKfycbw03GGQTg677UR5EThxoDB9mHqxeFygMBrW1KN2vII_ARuQ-WG1uG70ztodLW9mR71nlw/exec";

st_accept = "text/html" # говорим веб-серверу, 
                        # что хотим получить html
# имитируем подключение через браузер Mozilla на macOS
st_useragent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 12_3_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Safari/605.1.15"
# формируем хеш заголовков
headers = {
   "Accept": st_accept,
   "User-Agent": st_useragent
}

def try_request(url, headers):
    attemp = 1
    while attemp < 5:
        try:
            response = requests.get(url, headers)
            if response.status_code != 200:
                attemp += 1
                time.sleep(1)
                continue
            return response
        except ConnectionError as e:
            print(f'Error {e}')
            attemp += 1
            time.sleep(1)
    return ""


def reqCreateField(Field, profile):
    print(URL, Field.name)
    return try_request(f"{URL}?action=field&profile={profile}&name={Field.name}&area={Field.area}", headers=headers).text

def SetProcessing(Processing, profile, field_name):
    print(field_name)
    return try_request(F"{URL}?action=proccesing&profile={profile}&field_name={field_name}&name={Processing.name}&norma={Processing.norm_herbicide_of_once_are}&cost={Processing.cost_by_once_herb}&season={Processing.season}", headers).text

# пропуск для получения всех полей
def getField(name, profile):
    print(f"{URL}?action=getField&profile={profile}&name={name}")
    return try_request(f"{URL}?action=getField&profile={profile}&name={name}", headers).text 

def CreateReport(profile, season ,name, flag, url_folder):
    #print(f"{URL}?action=CreateReport&profile={profile}&season={season}&field_name={name}&flag={flag}")
    return try_request(f"{URL}?action=CreateReport&profile={profile}&season={season}&field_name={name}&flag={flag}&folder={url_folder}", headers).text;

def getSeason(profile):
    return try_request(f"{URL}?action=getSeason&profile={profile}", headers).text

def createSeason(profile, name, folderUrl):
    return try_request(f"{URL}?action=setSeasons&profile={profile}&season={name}&folder={folderUrl}", headers).text

def getReport(url_folder):
    return try_request(f"{URL}?action=getReportURL&folder={url_folder}", headers).text;
    
#print(CreateReport("5775480864", "djs", "True").text)
#print(SetProcessing(y, "5775480864", data.name))
#print(reqCreateField(data, "5775480864"))
#print(createSeason("5775480864", "2028"))
#print(CreateReport("5775480864", "2025","Поле№199", "False", '1qRN7IzmYIn3fJnuWRTj5bVpe9QJPepDw'))
#print(getField("", "user"))
#print(requests.get("https://drive.google.com/file/d/1YS6mXY66pRK54ybaac7Z8QNofLryq5TN/view?usp=sharing").text)
