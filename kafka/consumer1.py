from kafka import KafkaConsumer

def start_consumer():
    kafkaConsumer = KafkaConsumer('dw_metric_model', bootstrap_servers='10.1.56.187:9192')
    for msg in kafkaConsumer:
        # print('接收到的信息为：',msg)
        print("转换后的value：", msg.value.decode())


if __name__ == '__main__':
    start_consumer()
