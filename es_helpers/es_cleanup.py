#!/usr/bin/env python

import requests
import datetime
import sys
import es_config

elasticsearch_url = "http://%s:%d" % (es_config.elasticsearch_host, es_config.elasticsearch_port)

def delete():
    """Deletes logs older than a specified number of days."""

    if len(sys.argv) != 2:
        usage()

    try:
        numDays = int(sys.argv[1])
    except:
        usage()

    if numDays <= 0:
        print "Error! numDays must be greater than 0."
        sys.exit(2)

    cutoff = datetime.datetime.now() - datetime.timedelta(days=numDays)

    r = requests.get('%s/@bro-meta/index/_search?size=10000' % elasticsearch_url)
    for index in r.json['hits']['hits']:
        end_timestamp = datetime.datetime.fromtimestamp(index['_source']['end'])
        index_name = index['_source']['name']

        if end_timestamp < cutoff:
            r = requests.delete('%s/%s' % (elasticsearch_url, index_name))
            if r.status_code != 200:
                print "Warning! Deleting index %s resulted in status code %d. %s" % (index_name, r.status_code, r.json['error'])      
            if r.status_code == 200 or r.status_code == 404:
                print "Deleting %s." % index['_id']
                r = requests.delete('%s/@bro-meta/index/%s' % (elasticsearch_url, index['_id']))
                if r.status_code != 200:
                    print "Warning! Deleting index metadata %s resulted in status code %d. %s" % (index_name, r.status_code, r.json['error'])

def usage():
    print """ %s
--  
    Usage:   
             %s numDays
    Args:    
             numDays - Indexes that end before $currentTime - numDays days ago will be deleted.
    Example: 
             %s 7 - Delete all indexes that end before this time a week ago.
    """ % (sys.argv[0], sys.argv[0], sys.argv[0])

    sys.exit(1)


if __name__ == "__main__":
    delete()
