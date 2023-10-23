import requests
from utils.base import BASE_DATA as bd

api_key = bd["IMAGGA_API_KEY"]
api_secret = bd["IMAGGA_API_SECRET"]




def image_has_face(image_path):
    print(image_path, "is being checked")
    response = requests.post(
        'https://api.imagga.com/v2/faces/detections',
        auth=(api_key, api_secret),
        files={'image': open(image_path, 'rb')}, 
        params={"return_face_id":1}
        )
    response = response.json()
    print(response)
    if response["status"]["type"] == "success":
        print('booyeah')
        print('facID: ',  response["result"]["faces"][0]["face_id"])
        return response["result"]["faces"][0]["face_id"]
    else:
        return None
    
def image_similarity(face_id, second_face_id):
    print('ids', face_id, second_face_id)
    response = requests.get(
    'https://api.imagga.com/v2/faces/similarity?face_id=%s&second_face_id=%s' % (face_id, second_face_id),
    auth=(api_key, api_secret))
    response = response.json()
    print(response)

    if response["status"]["type"] == "success":
        return response["result"]["score"] > 80
