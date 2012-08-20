ElasticSearch Helpers
=====================

es_cleanup.py
-------------

Deletes indices older than a specified number of days.

```    
    Usage:   
             es_cleanup.py numDays
    Args:    
             numDays - Indexes that end before $currentTime - numDays days ago will be deleted.
    Example: 
             es_cleanup.py 7 - Delete all indexes that end before this time a week ago.
```

**Configuration**: To set the ES server and port, edit the settings at the top of the file.
