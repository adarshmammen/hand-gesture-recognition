import os
from clarifai.rest import ApiClient, Image


api = ApiClient(base_url='https://api2-prod.clarifai.com', client_id='09-us71rZIxJ9uLSXir95tigu6NOVIN47HM5NYPM' , client_secret='33bPTgG00uYO81HoLqHpjMG-h2ExAw0Li_g45HDG')

s = '/Users/adarsh/Desktop/testAI/hand_open/'
label = 'hand_open'
li_hand_open = []
os.chdir('/Users/adarsh/Desktop/testAI/hand_open/')
for i in os.listdir(os.getcwd()):
	if i.endswith(".jpg"):
	    li_hand_open.append(Image(file_obj=open(s+i),labels=[label]))


s = '/Users/adarsh/Desktop/testAI/hand_closed/'
label = 'hand_closed'
li_hand_closed = []
os.chdir('/Users/adarsh/Desktop/testAI/hand_closed/')
for i in os.listdir(os.getcwd()):
	if i.endswith(".jpg"):
	    li_hand_closed.append(Image(file_obj=open(s+i),labels=[label]))



s = '/Users/adarsh/Desktop/testAI/hand_crossed/'
label = 'hand_crossed'
li_hand_crossed = []
os.chdir('/Users/adarsh/Desktop/testAI/hand_crossed/')
for i in os.listdir(os.getcwd()):
	if i.endswith(".jpg"):
	    li_hand_crossed.append(Image(file_obj=open(s+i),labels=[label]))


input_list = []
input_list.extend(li_hand_open)
input_list.extend(li_hand_closed)
input_list.extend(li_hand_crossed)


api.addInputs(input_list)


res = api.createModel(model_name='Gestures', concept_ids=['hand_open','hand_closed','hand_crossed'])

model_id = res['model']['id']

#### TRAINING MODEL 

api.trainModel(model_id=model_id)

print model_id
