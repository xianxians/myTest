from elasticsearch import Elasticsearch

if __name__ == '__main__':
    es = Elasticsearch(['10.1.11.152'], http_auth=('admin', 'Admin@123'), port=9200, timeout=50000)
    print(es.index(index="p1", doc_type="doc", id=2, body={"name": "test"}))

