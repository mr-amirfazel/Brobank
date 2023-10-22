import pika, os

# Access the CLODUAMQP_URL environment variable and parse it (fallback to localhost)
url = os.environ.get('CLOUDAMQP_URL', 'amqps://seuumisc:rKJKzpOFICHQ8384CAhDDvLMrrMH_l3w@shark.rmq.cloudamqp.com/seuumisc')
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)
channel = connection.channel() # start a channel
channel.queue_declare(queue='hello') # Declare a queue
def callback(ch, method, properties, body):
  print(" [x] Received " + str(body))

channel.basic_consume('hello',
                      callback,
                      auto_ack=True)

print(' [*] Waiting for messages:')
# while True:
try:
  channel.start_consuming()
except Exception as e:
  connection.close()
  
connection.close()