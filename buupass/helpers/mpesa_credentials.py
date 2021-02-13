import os
import environ
from dotenv import load_dotenv
import requests
import json
from requests.auth import HTTPBasicAuth
from datetime import datetime
import base64

load_dotenv()


class MpesaC2bCredential:
    consumer_key = "qJEEgPZR0AZYoTukaxAuX5tkEAWXZF5S"
    consumer_secret = "4TauT5pKMPRik8n7"
    api_URL = 'https://api.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'


class MpesaC2bAccessToken:
    r = requests.get(MpesaC2bCredential.api_URL,
                     auth=HTTPBasicAuth(MpesaC2bCredential.consumer_key, MpesaC2bCredential.consumer_secret))
    mpesa_access_token = json.loads(r.text)
    validated_mpesa_access_token = mpesa_access_token['access_token']


class MpesaB2cCredential:
    consumer_key = "UEyvljGCyHQAwegIUvNsrCkIgwuwmz62"
    consumer_secret = "LEnbXHUlfXn1siBF"
    api_URL = 'https://api.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'


class MpesaB2cAccessToken:
    r = requests.get(MpesaB2cCredential.api_URL,
                     auth=HTTPBasicAuth(MpesaB2cCredential.consumer_key, MpesaB2cCredential.consumer_secret))
    mpesa_access_token = json.loads(r.text)
    validated_mpesa_access_token = mpesa_access_token['access_token']


class LipanaMpesaPassword:
    lipa_time = datetime.now().strftime('%Y%m%d%H%M%S')
    Business_short_code = "674890"
    passkey = "912cefd1af43a5203af5a48d3d6375533394d52876ae4a416799a89603cadffb"
    data_to_encode = Business_short_code + passkey + lipa_time
    online_password = base64.b64encode(data_to_encode.encode())
    decode_password = online_password.decode('utf-8')
