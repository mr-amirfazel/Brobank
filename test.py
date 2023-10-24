# import json
# import requests

# pdf_file = open('./CC_HW1.pdf', 'rb')
# data = {"name": "fazel", "lastName": "koozegar"}

# resp = requests.post(
#     'http://192.168.1.33:5000/api/test',
#     data= {'json_payload': json.dumps(data)},
#     files={'pdf_file' : ('file.pdf', pdf_file, 'application/pdf'),}
# )

# print(resp.status_code)
# print(resp.json()["message"])

bytes_data = b'14'
string_data = bytes_data.decode('utf-8')

print(bytes_data)
print(str(bytes_data))
print(string_data)