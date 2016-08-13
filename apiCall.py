from clarifai.rest import ApiClient, Image
import random, os,requests,json
from PIL import Image as img


api = ApiClient(base_url="https://api2-prod.clarifai.com",client_id = "2vanjQ-fz_heE5jkDE5Yl5Z-wdj5y5yZYbzan6Zn", client_secret = "ogCsS8AFUwiUOBNgGks4fS4H_8xZXkPUBLfrHE0I")


imgs = Image(file_obj = open('Chocoflow.jpg'))
#img = img.open("Chocoflow.jpg")
#img.rotate(45).show()

#api.predictConcept([img])
api.addInputs([imgs])
