import pika, os


def publish_data(data, url_path):
# Access the CLODUAMQP_URL environment variable and parse it (fallback to localhost)
    # url = os.environ.get('CLOUDAMQP_URL', url_path)
    # params = pika.URLParameters(url)
    # connection = pika.BlockingConnection(params)
    # channel = connection.channel() # start a channel
    # channel.queue_declare(queue='ccass1') # Declare a queue
    # channel.basic_publish(exchange='',
    #                     routing_key='ccass1',
    #                     body=data)

    # print(f" [x] Sent {data}")
    # connection.close()

    connection_parameters = pika.ConnectionParameters(
    host='services.irn1.chabokan.net',
    port=60560,  # Default AMQPS port
    virtual_host='/',
    credentials=pika.PlainCredentials('patricia', 'M5oDa0NsJZQ5zAkJ'),
    )

    # Establish the connection
    connection = pika.BlockingConnection(connection_parameters)

    # Create a channel and perform your publishing operations
    channel = connection.channel()
    channel.queue_declare(queue='ccass1')
    channel.basic_publish(exchange='',
                        routing_key='ccass1',
                         body=data)
    # ...

    # Don't forget to close the connection when you're done
    connection.close()