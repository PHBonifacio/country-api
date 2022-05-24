import json
from typing import Counter
from unicodedata import name
from urllib import response

import requests

URL_ALL =  "https://restcountries.com/v2/all"
URL_NAME = "https://restcountries.com/v3.1/name"
URL_CODE = "https://restcountries.com/v3.1/alpha"
URL_CURR = "https://restcountries.com/v3.1/currency"
URL_LANG = "https://restcountries.com/v3.1/lang"
URL_REGI = "https://restcountries.com/v3.1/region"
URL_CALL = "https://restcountries.com/v2/callingcode"

def GetURLRequest(url):
    try:
        result = requests.get(url)

        if 200 == result.status_code:
            return result.text
    except Exception as e:
        print(e)

def ParseURLRequest(request_text):
    try:
        return json.loads(request_text)
    except Exception as e:
        print(e)

def GetAllCountries():
    request = GetURLRequest(URL_ALL)
    if request:
        return ParseURLRequest(request)

def GetAllCountriesCount():
    return len(GetAllCountries())

def GetCountryByName(name, fullName):
    if fullName:
        reqTxt = "{}/{}?fullText=true".format(URL_NAME, name)
    else:
        reqTxt = "{}/{}".format(URL_NAME, name)

    request = GetURLRequest(reqTxt)
    if request:
        return ParseURLRequest(request)

def GetCountryByCode(code):
    request = GetURLRequest("{}/{}".format(URL_CODE, code))
    if request:
        return ParseURLRequest(request)

def GetCountryByCurrency(currency):
    request = GetURLRequest("{}/{}".format(URL_CURR, currency))
    if request:
        return ParseURLRequest(request)

def GetCountryByLanguage(lang):
    request = GetURLRequest("{}/{}".format(URL_LANG, lang))
    if request:
        return ParseURLRequest(request)

def GetCountryByRegion(region):
    request = GetURLRequest("{}/{}".format(URL_REGI, region))
    if request:
        return ParseURLRequest(request)

def GetCountryByCallingCode(code):
    request = GetURLRequest("{}/{}".format(URL_CALL, code))
    if request:
        return ParseURLRequest(request)

def GetCountriesInfo(countrieslist, info):
    info_list = []
    for country in countrieslist:
        info_list.append(country[info])
    
    return info_list

def GetCountriesInfoTuple(countrieslist, info):
    info_list = None
    if countrieslist:
        info_list = []
        for country in countrieslist:
            try:
                if country[info]:
                    info_list.append((country["name"], country[info]))
            except Exception as e:
                print(e)
                print("{} dont have the info: {}".format(country["name"], info))
    
    return info_list

def GetCountryPopulation(name, full):
    if name:
        rst = GetCountriesInfoTuple(GetCountryByName(name, full), 'population')
        if rst:
            result = []
            for item in rst:
                result.append((item[0]['common'], item[1]))
            return result
    else:
        return GetCountriesInfoTuple(GetAllCountries(), 'population')

def GetCountriesNamesList(name, full):
    if name:
        rst =  GetCountriesInfo(GetCountryByName(name, full), 'name')
        if rst:
            names = []
            for item in rst:
                names.append(item['common'])
            return names
    else:
        return GetCountriesInfo(GetAllCountries(), 'name')

def GetCountriesCurrency(name, full):
    if name:
        rst =  GetCountriesInfoTuple(GetCountryByName(name, full), 'currencies')
        if rst:
            result = []
            for item in rst:
                for curr in item[1]:
                    result.append((item[0]['common'], (curr, item[1][curr]['name'], item[1][curr]['symbol'])))
            return result
    else:
        return GetCountriesInfoTuple(GetAllCountries(), 'currencies')
