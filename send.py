import pika, os

# Access the CLODUAMQP_URL environment variable and parse it (fallback to localhost)
url = os.environ.get('CLOUDAMQP_URL', 'amqps://seuumisc:rKJKzpOFICHQ8384CAhDDvLMrrMH_l3w@shark.rmq.cloudamqp.com/seuumisc')
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)
channel = connection.channel() # start a channel
channel.queue_declare(queue='hello') # Declare a queue
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello NNN!')
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello dear!')

print(" [x] Sent 'Hello World!'")
connection.close()