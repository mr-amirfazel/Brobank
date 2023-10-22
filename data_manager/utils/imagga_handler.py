import requests
from base import BASE_DATA as bd

api_key = bd["IMAGGA_API_KEY"]
api_secret = bd["IMAGGA_API_SECRET"]




def image_has_face(image_path):
    response = requests.post(
        'https://api.imagga.com/v2/faces/detections',
        auth=(api_key, api_secret),
        files={'image': open(image_path, 'rb')})
    response = response.json()

    if response.status.type == "sucess":
        return response.result.faces[0]["face_id"]
    else:
        return None
    
def image_similarity(face_id, second_face_id):
    response = requests.get(
    'https://api.imagga.com/v2/faces/similarity?face_id=%s&second_face_id=%s' % (face_id, second_face_id),
    auth=(api_key, api_secret))
    response = response.json()

    if response.status.type == "sucess":
        return response.result.score > 80
