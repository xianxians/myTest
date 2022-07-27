# -* coding:utf8 *-
from pykafka import KafkaClient

host = '10.1.56.187:9192'
client = KafkaClient(hosts=host)
# 生产者
topicdocu = client.topics['my-topic']
producer = client.topics['my-test']

