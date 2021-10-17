from typing import Text
import json
from flask import Flask,request,jsonify
import requests 
from numpy import datetime_data
from werkzeug.exceptions import MethodNotAllowed
app = Flask(__name__)
atm_stores = [{"address":{"street":"Molenstraat","housenumber":"50","postalcode":"7241 AE","city":"Lochem","geoLocation":{"lat":"52.162328","lng":"6.417507"}},"distance":0,"openingHours":[{"dayOfWeek":2,"hours":[{"hourFrom":"08:00","hourTo":"18:30"}]},{"dayOfWeek":3,"hours":[{"hourFrom":"08:00","hourTo":"18:30"}]},{"dayOfWeek":4,"hours":[{"hourFrom":"08:00","hourTo":"18:30"}]},{"dayOfWeek":5,"hours":[{"hourFrom":"08:00","hourTo":"18:30"}]},{"dayOfWeek":6,"hours":[{"hourFrom":"08:00","hourTo":"18:30"}]},{"dayOfWeek":7,"hours":[{"hourFrom":"08:00","hourTo":"17:00"}]},{"dayOfWeek":1,"hours":[]}],"functionality":"Geld storten en opnemen","type":"GELDMAAT"}]
atm_list = []

# single time fetch from api
# r  = requests.get('https://www.ing.nl/api/locator/atms/')
# data = r.content[5:]
# # print(data)
# print(r.status_code)
# print(r.ok)
with open ('demo_data.json','r') as f:
    atm_list = json.load(f)
print(type(atm_list))
# print(dir(r))
# print(help(r))
# print(r.text)

# data = request.get_json('https://www.ing.nl/api/locator/atms/')
# print(data)
@app.route('/')
def sample_app():
    return jsonify({'message':'we are developing api'})
    

@app.route('/ing_atm/<string:atm_name>')
def get_list_ing_atm(atm_name):
    for stores in atm_list:
        print(stores['address']['city'])
    return jsonify({'message':'store not found'})
    
# app.run(port= 5000)
# @app.route('/ing_atm',Methods = ['POST'])
# def create_ing_atm():
#     pass

# @app.route('/',methods= ['PUT'])
# def delete_ing_atm():
#     pass

# @app.route('/')
# def update_ing_atm():
#     pass
app.run(port=5000)