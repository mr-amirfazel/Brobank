import pika, os

data = ""


def consume_data(url_path):
    global data
# Access the CLODUAMQP_URL environment variable and parse it (fallback to localhost)
    url = os.environ.get('CLOUDAMQP_URL', url_path)
    params = pika.URLParameters(url)
    connection = pika.BlockingConnection(params)
    channel = connection.channel() # start a channel
    channel.queue_declare(queue='ccass1') # Declare a queue
    def callback(ch, method, properties, body):
        global data
        print(" [x] Received " + str(body))
        data = str(body)
        return str(body)

    channel.basic_consume('ccass1',
                        callback,
                        auto_ack=True)

    print(' [*] Waiting for messages:')
    channel.start_consuming()
    connection.close()
    return data