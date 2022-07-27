from elasticsearch import Elasticsearch

if __name__ == '__main__':
    es = Elasticsearch(['10.1.11.152'], http_auth=('admin', 'Admin@123'), port=9200, timeout=50000)

    query = {
        "query": {
            "match_all": {}
        },
        "size": 2
    }

    allDoc = es.search(index='dm_l_b_xd', body=query)
    items = allDoc['hits']['hits']
    print([i['_source'] for i in items])
