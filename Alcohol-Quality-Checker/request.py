import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'sulfate':0.52, 'Alcohole Level':10})

print(r.json())

