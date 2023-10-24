import json
import requests

pdf_file = open('./CC_HW1.pdf', 'rb')
data = {"name": "fazel", "lastName": "koozegar"}

requests.post(
    'http://192.168.1.33:5000/api/test',
    data= {'json_payload': json.dumps(data)},
    files={'pdf_file' : ('file.pdf', pdf_file, 'application/pdf'),}
)

