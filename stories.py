from flask import jsonify, request
import json
import urllib.request
import json
import requests
import html

def send_stories():
    url_stories='https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty'
    try:
        response = requests.get(
            url=url_stories,
            headers={"Content-Type": "application/json"},
        )
        res_list =[]
        res_json_list = response.json()
        res_json_first = res_json_list[:10]
        for i in res_json_first:
             print(i)
             urltest=f'https://hacker-news.firebaseio.com/v0/item/{i}.json?print=pretty'
             print(urltest)
             res_json =  requests.get(
                url=f'https://hacker-news.firebaseio.com/v0/item/{i}.json?print=pretty',
                headers={"Content-Type": "application/json"}
                )
             print(res_json)
             print(type(res_json))

             js = res_json.json()
             res_list.append(js)
        print(res_list)
        return res_list
    except Exception as e:
            return jsonify({'error': 'Failed to send notification: {}'.format(str(e))}), 500
    
def send_comments(request_data):
        res_list =[]
        res_json_list = request_data
        res_json_first = res_json_list
        for i in res_json_first:
             print(i)
             urltest=f'https://hacker-news.firebaseio.com/v0/item/{i}.json?print=pretty'
             print(urltest)
             res_json =  requests.get(
                url=f'https://hacker-news.firebaseio.com/v0/item/{i}.json?print=pretty',
                headers={"Content-Type": "application/json"}
                )
             print(res_json)
             print(type(res_json))

             js = res_json.json()
             if "text" in js:
                text = html.unescape(js.get('text'))
                js['text']=text
                res_list.append(js)
        print(res_list)
        return res_list

def send_newstories():
    url_stories='https://hacker-news.firebaseio.com/v0/newstories.json?print=pretty'
    try:
        response = requests.get(
            url=url_stories,
            headers={"Content-Type": "application/json"},
        )
        res_list =[]
        res_json_list = response.json()
        res_json_first = res_json_list[:5]
        for i in res_json_first:
             print(i)
             res_json =  requests.get(
                url=f'https://hacker-news.firebaseio.com/v0/item/{i}.json?print=pretty',
                headers={"Content-Type": "application/json"}
                )
             js = res_json.json()
             res_list.append(js)
         
        print(res_list)
        return res_list
    except Exception as e:
            return jsonify({'error': 'Failed to send notification: {}'.format(str(e))}), 500