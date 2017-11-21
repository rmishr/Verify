
import requests
import json

url = ('https://newsapi.org/v2/everything?'
        'q=fraternity+AND+hazing+AND+penn&'
        'from=2017-19-11&'
        'sortBy=popularity&'
        'apiKey=68a04853b1a1497a99e93ac2a0425936')

#response = requests.get(url)

def getNewsUrl():
    newsJson = json.loads(open("mockResponse.json").read())
    return newsJson


if __name__ ==  '__main__':
    newsJson = getNewsUrl()
    for article in newsJson['articles']:
        print article['url']