import json

import datetime

from pki_tools import Name, Certificate, Validity, RSAKeyPair, SHA512


def lambda_handler(event, context):
    name = Name(cn=["Cert CN"])

    validity = Validity(
        not_before=datetime.datetime.today() - datetime.timedelta(days=1),
        not_after=datetime.datetime.today() + datetime.timedelta(days=1),
    )

    cert = Certificate(
        subject=name,
        issuer=name,
        validity=validity,
    )

    cert.sign(RSAKeyPair.generate(), SHA512)

    print(cert)


    # try:
    #     ip = requests.get("http://checkip.amazonaws.com/")
    # except requests.RequestException as e:
    #     # Send some context about this error to Lambda Logs
    #     print(e)

    #     raise e

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world",
            # "location": ip.text.replace("\n", "")
        }),
    }
