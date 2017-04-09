import socket
import sys
import json
from elasticsearch import Elasticsearch
import cPickle

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host=socket.gethostname();
port=8091;
s.bind((host, port))
s.listen(5)
es = Elasticsearch(['https://search-twitter-demo-uubcfb66kimawtv5q6pnh4kgxu.us-west-2.es.amazonaws.com:443'])

tmap= {
    "tmsg": {
   
     },

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
while True:
    clientSocket, clientAddr = s.accept()
    msg = clientSocket.recv(4096)
    clientSocket.close()
    check=msg.find('arn:aws:sns:us-east-2:851980283070:twittmap')
    print (check)
    print (msg)
    if check<0:
        continue    
    start=msg.find('\n  "Message"')
    start +=16
    mtemp=msg[start:]
    end = mtemp.find('",\n')
    rmsg = mtemp[0 : end]
    rmsg=rmsg.replace('\\"', '"')
    doc = json.loads(rmsg)
    doc['geo_location']['lon']=float(doc['geo_location']['lon'])
    doc['geo_location']['lat']=float(doc['geo_location']['lat'])
    res = es.index(index="tmsg", doc_type='tweet', body=doc)
    print "yeah!done"
    continue
