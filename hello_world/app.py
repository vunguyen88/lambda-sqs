import json
import boto3
from twilio.rest import Client# import requests


def lambda_handler(event, context):
    secret_name = "todo-eks-twillio"
    region_name = "us-east-2"

    account_sid = ""
    auth_token  = ""

    # Create a Secrets Manager client
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )

    get_secret_value_response = client.get_secret_value(
        SecretId=secret_name
    )
    secret_strings = json.loads(get_secret_value_response['SecretString'])

    twilio_acc_sid = secret_strings['todo-eks-twillio-account-sid']
    twilio_auth_token = secret_strings['todo-eks-twillio-auth-token']

    print("todo_eks_twillio_acc ", twilio_acc_sid)
    print("twillio_auth_token ", twilio_auth_token)

    # client = Client(account_sid, auth_token)

    # message = client.messages.create(
    #     to   ="+14074935333",
    #     from_="+14073781169",
    #     body="Hello from Python!")

    # print(message.sid)

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": f"Success",
            # "location": ip.text.replace("\n", "")
        }),
    }
