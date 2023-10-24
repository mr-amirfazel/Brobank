import pika, os

data = ""


def consume_data(do_after):
    global data
# Access the CLODUAMQP_URL environment variable and parse it (fallback to localhost)
    connection_parameters = pika.ConnectionParameters(
    host='services.irn1.chabokan.net',
    port=60560,  # Default AMQPS port
    virtual_host='/',
    credentials=pika.PlainCredentials('patricia', 'M5oDa0NsJZQ5zAkJ'),
    )

    # Establish the connection
    connection = pika.BlockingConnection(connection_parameters)
    channel = connection.channel() # start a channel
    channel.queue_declare(queue='ccass1') # Declare a queue
    def callback(ch, method, properties, body):
        global data
        print(" [x] Received " + str(body))
        data = (body).decode('utf-8')
        do_after(data)

    channel.basic_consume('ccass1',
                        callback,
                        auto_ack=True)

    print(' [*] Waiting for messages:')
    channel.start_consuming()
    connection.close()