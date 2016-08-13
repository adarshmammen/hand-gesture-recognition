
from clarifai.rest import ApiClient, Image
import requests, json
from pprint import pprint
li = []


api = ApiClient(base_url='https://api2-prod.clarifai.com', client_id='dT-yEmi9i5y_ORbOKuANxQAG-SGkncTeL-VfSJxd' , client_secret='DmUMWV_NdE-CeyQYveYAcfWgF4YEta7VWpqijrw7')

img1 = Image(file_obj=open('/Users/adarsh/Desktop/AI_hacks/hand1.jpg'), labels=['hand_yes'])
img2 = Image('/Users/adarsh/Desktop/AI_hacks/hand2.jpg', labels=['hand_yes'])
img3 = Image('/Users/adarsh/Desktop/AI_hacks/hand3.jpg', labels=['hand_yes'])

r = api.predictConcepts([img1])

tags = r['outputs'][0]['data']['tags']


for ele in tags:
	li.append(ele['concept']['name'])

print li





