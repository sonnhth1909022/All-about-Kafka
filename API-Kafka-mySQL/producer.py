from kafka import KafkaProducer
from time import sleep
from json import dumps

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x:
                         dumps(x).encode('utf-8'))

fp = open("server.log", "r+")
for i in fp.readlines():
    temp = i.strip().split(' ')
    data = {'Customer': temp[0],
            'Product': temp[1],
            'quantity': temp[2],
            'amount': temp[3]}

    producer.send('retail_topic', value=data)
    sleep(5)