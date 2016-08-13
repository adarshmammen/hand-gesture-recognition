from clarifai.rest import ApiClient, Image
import requests, json



api = ApiClient(base_url='https://api2-prod.clarifai.com', client_id='09-us71rZIxJ9uLSXir95tigu6NOVIN47HM5NYPM' , client_secret='33bPTgG00uYO81HoLqHpjMG-h2ExAw0Li_g45HDG')

#TEST SET
test_img1 = Image(file_obj=open('/Users/adarsh/Desktop/testAI/test_set1.jpg'))
test_img2 = Image(file_obj=open('/Users/adarsh/Desktop/testAI/test_set2.jpg'))

model_id = 'd17033d6038f4b43806a8965989b9862'

z = api.predictModel(model_id=model_id, objs=[test_img1])

print z['outputs'][0]['data']['tags']



