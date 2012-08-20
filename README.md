ElasticSearch Helpers
=====================

Prerequisites
-------------

These sripts only work with Bro if you're using the new [ElasticSearch Logging](http://git.bro-ids.org/bro.git/blob/HEAD:/doc/logging-elasticsearch.rst) plugin.

Please refer to that documentation for getting ElasticSearch setup, and receiving logs.

It's also *highly* recommended to review the [ElasticSearch configuration tips](https://github.com/grigorescu/Brownian/wiki/ElasticSearch-Configuration).

Requirements
------------

* Python version 2.6 or 2.7.

Virtualenv Setup
----------------

It is advised to run these scripts in a [virtualenv](http://www.virtualenv.org/en/latest/index.html) - an isolated Python environment with its own set of libraries.
This will prevent system upgrades from modifying the globally installed libraries and potentially breaking the scripts.

**Note**: These scripts can be safely installed in your [Brownian](https://www.github.com/grigorescu/Brownian) virtualenv.

1. Download the latest [virtualenv.py](https://raw.github.com/pypa/virtualenv/master/virtualenv.py).
+ Create and switch to your environment:

```bash
$ python ./virtualenv.py es_helpers
$ cd es_helpers
$ source ./bin/activate
```

Installation
------------

```bash
$ pip install git+https://github.com/grigorescu/es_helpers.git
```

Command hooks are installed in the ``bin`` directory of your virtualenv.

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

**Configuration**: To set the ES server and port, edit the settings at the top of the file, which is located in lib/python2.X/site-packages/es_helpers.

Issues
------

If you see something that's broken, or something that you'd like added, please create an issue.

As always, fork, patch, and push away!
