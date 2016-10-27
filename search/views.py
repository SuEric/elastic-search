from django.shortcuts import render

from elasticsearch import Elasticsearch
import json
import requests

def index(request):

	
    es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

    r = requests.get('http://localhost:9200') 

    i = 1

    """
    while r.status_code == 200:
        r = requests.get('http://swapi.co/api/people/'+ str(i))
        es.index(index='sw', doc_type='people', id=i, body=json.loads(r.text))
        i=i+1
    """

    es.search(index="sw", body={
    	"query": {
    		"fuzzy_like_this_field" : {
    			"name" : {
    			"like_text": "jaba", 
    			"max_query_terms":5
    			}
    		}
    	}
    })

    context = {
        'simple_var': "helo",
    }

    return render(request, 'search/index.html', context)
