from elasticsearch import Elasticsearch

es = Elasticsearch(['https://search-twitter-demo-uubcfb66kimawtv5q6pnh4kgxu.us-west-2.es.amazonaws.com:443'])

tmap= {
    "mappings": {
        "tweet":{
            "properties":{
                "text":{
                    "type":"string"
                },
                "sentiment":{
                    "type":"string"
                },
                "geo_location":{
                    "type":"geo_point"
                }
            }
        }
    }
}

es.indices.create(index="tmsg", body=tmap, ignore = 400)
