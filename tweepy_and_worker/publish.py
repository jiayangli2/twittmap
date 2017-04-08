import boto3

client = boto3.client('sns', region_name='us-east-2')
response = client.publish(
    TopicArn='arn:aws:sns:us-east-2:851980283070:twittmap',
    Message='heyheyyouyou',
    Subject='Message from worker'
)

