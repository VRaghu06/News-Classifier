
import os, requests
from fastapi import FastAPI
from transformers import pipeline

api = FastAPI()

api_key = os.getenv("RAPIDAPI_KEY")

url = "https://real-time-news-data.p.rapidapi.com/search"

@api.get("/")
def default():
    return{"message":"choose between regular news and classified-news"}

@api.get("/news/{query}")
def give_data(query:str , limit:int = 5):

    querystring = {
        "query":query,
        "limit": limit,
        "country": "IN",
        "lang": "en"
    }

    headers = {
    "x-rapidapi-key":api_key,
    "x-rapidapi_host":"real-time-news-data.p.rapidapi.com"
    }

    response=requests.get(url,headers=headers,params=querystring)

    output = response.json()

    final={}


    for i in range(len(output.get("data"))):
        title = output.get("data")[i].get("title")
        string = f"title {i+1}"# example: title 3
        final[string] = title
    
    return final#return the final dict


classifier = pipeline("zero-shot-classification" , model="facebook/bart-large-mnli")

@api.get("/classified-news/{query}")
def classify(query:str , limit:int = 5):

    querystring = {
        "query":query,
        "limit": limit,
        "country": "IN",
        "lang": "en"
    }

    headers = {
    "x-rapidapi-key":api_key,
    "x-rapidapi_host":"real-time-news-data.p.rapidapi.com"
    }

    response=requests.get(url,headers=headers,params=querystring)

    output = response.json() 

    # now that we got the data the first step is to mold it into an array of strings that hold both the title and snippet

    output_arr = output.get("data") #holds as many elems as the limit specifies, each elem is an dict
    string_arr : list[str] = []
    for i in range(len(output_arr)):
        title = output_arr[i].get("title")
        snippet = output_arr[i].get("snippet")
        string_arr.append(title + " " + snippet)
    
    # so our string_arr now holds the array of strings that can be passed to our classifier

    labels = ["politics" , "technology" , "sports" , "business" , "entertainment"]

    results = classifier(string_arr , labels , batch_size = limit)# you could just do print results and call it a day, but imma go full sicko mode and flex on yall mfs

    final_output = []# we gon append each object into this list

    for result in results:
        new_dict = {
            "text" : result["sequence"],
            "category" : result['labels'][0],
            "confidence" : result['scores'][0],
        }

        final_output.append(new_dict)

    return final_output









