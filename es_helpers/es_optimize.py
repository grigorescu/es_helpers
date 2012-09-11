#!/usr/bin/env python

import requests
import datetime
import sys
import es_config

elasticsearch_url = "http://%s:%d" % (es_config.elasticsearch_host, es_config.elasticsearch_port)

def optimize():
    """Optimizes logs older than a specified number of hours into a single segment per shard."""

    if len(sys.argv) != 2:
        usage()

    try:
        numHours = int(sys.argv[1])
    except:
        usage()

    if numHours <= 0:
        print "Error! numHours must be greater than 0."
        sys.exit(2)

    cutoff = datetime.datetime.now() - datetime.timedelta(hours=numHours)

    r = requests.get('%s/@bro-meta/index/_search' % elasticsearch_url)
    for index in r.json['hits']['hits']:
        end_timestamp = datetime.datetime.fromtimestamp(index['_source']['end'])
        index_name = index['_source']['name']

        if end_timestamp < cutoff:
            r = requests.get('%s/%s/_optimize' % (elasticsearch_url, index_name), params={"max_num_segments": 1, "wait_for_merge": False})
            if r.status_code != 200:
                print "Warning! Optimizing index %s resulted in status code %d. %s" % (index_name, r.status_code, r.json['error'])      

def usage():
    print """ %s
--  
    Usage:   
             %s numHours
    Args:    
             numHours - Indexes that end before $currentTime - numHours hours ago will be deleted.
    Example: 
             %s 7 - Optimize all indexes that end before 7 hours ago.
    """ % (sys.argv[0], sys.argv[0], sys.argv[0])

    sys.exit(1)

if __name__ == "__main__":
    optimize()
