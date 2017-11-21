import networkx as nx
import json
from networkx.readwrite import json_graph
import sys


sys.path.append("..newsapi")
from newsapi import newsapi


if __name__ == 'main':
    newsJson = getNewsUrl()
    for article in newsJson['articles']:
        print article['url']

