import boto3


def create_queue(QueueName):
    # Get the service resource
    sqs = boto3.resource('sqs')
    # Create the queue. This returns an SQS.Queue instance
    queue = sqs.create_queue(QueueName=QueueName, Attributes={'DelaySeconds': '5'})
    # You can now access identifiers and attributes
    print(queue.url)
    print(queue.attributes.get('DelaySeconds'))
    return sqs, queue.url


def send_msg(QueueName, msg, sqs):
    # Get the service resource
    #sqs = boto3.resource('sqs')

    # Get the queue
    queue = sqs.get_queue_by_name(QueueName=QueueName)

    # Create a new message
    response = queue.send_message(MessageBody=msg)

    # The response is NOT a resource, but gives you a message ID and MD5
    print(response.get('MessageId'))
    print(response.get('MD5OfMessageBody'))

def process_msg(sqs, QueueName):
    # Get the service resource
    #sqs = boto3.resource('sqs')

    # Get the queue
    queue = sqs.get_queue_by_name(QueueName=QueueName)

    # Process messages by printing out body and optional author name
    for message in queue.receive_messages(MessageAttributeNames=['Author']):
        # Get the custom author message attribute if it was set
        author_text = ''
        if message.message_attributes is not None:
            author_name = message.message_attributes.get('Author').get('StringValue')
            if author_name:
                author_text = ' ({0})'.format(author_name)

        # Print out the body and author (if set)
        print('Hello, {0}!{1}'.format(message.body, author_text))

        # Let the queue know that the message is processed
        message.delete()



def main():
    sqs, queue_url=create_queue('TweetTrend2')
    send_msg('TweetTrend2', "hello!",sqs)

if __name__ == "__main__":
    # calling main function
    main()
