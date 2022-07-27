from elasticsearch import Elasticsearch

if __name__ == '__main__':
    es = Elasticsearch(['127.0.0.1:9200'])
    print(es.index(index="p1", doc_type="doc", id=2, body={"name": "济宁"}))

    query = {
        "query": {
            "match_all": {}
        },
        "size": 2
    }

    allDoc = es.search(index='shopping', body=query)
    items = allDoc['hits']['hits']
    print([i['_source'] for i in items])
