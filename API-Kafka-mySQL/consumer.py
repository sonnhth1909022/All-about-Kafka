from kafka import KafkaConsumer
from json import loads
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Baby1412/",
    database="kafkaMySQL"
)

consumer = KafkaConsumer(
    'retail_topic',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='my-group',
    value_deserializer=lambda x: loads(x.decode('utf-8')))

for message in consumer:
    message = message.value

    mycursor = mydb.cursor()
    sql = "INSERT INTO kafkaMySQL.retail_kafka (customer, product,quantity,amount) VALUES (%s, %s, %s, %s)"
    val = (message['Customer'], message['Product'], message['quantity'], message['amount'])
    mycursor.execute(sql, val)

    mydb.commit()

    print(mycursor.rowcount, "record inserted.")
