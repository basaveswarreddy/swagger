from flask import Flask,jsonify,request,render_template, request
from flask_swagger_ui import get_swaggerui_blueprint


app = Flask(__name__)

### swagger specific ###
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Seans-Python-Flask-REST-Boilerplate"
    }
)
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)
### end swagger specific ###


#app.register_blueprint(request_api.get_blueprint())

subnets = [{
    'location': 'Hyderabad',
    'list' :[{  'agg_subnets': '100',
                'no_subnets': '200',
                'subnet_size': '/24'}]

}]

@app.route('/')
def home():
  return render_template('index.html')

#post /subnet data: {name :}
@app.route('/subnet' , methods=['POST'])
def create_subnet():
  request_data = request.get_json()
  new_subnet = {
    'name':request_data['name'],
    'list':[]
  }
  subnets.append(new_subnet)
  return jsonify(new_subnet)
  #pass

#get /subnet/<name> data: {name :}
@app.route('/subnet/<string:name>')
def get_subnet(name):
  for subnet in subnets:
    if subnet['name'] == name:
          return jsonify(subnet)
  return jsonify ({'message': 'subnets not found'})
  #pass

#get /store
@app.route('/subnet')
def get_subnets():
  return jsonify({'subnets': subnets})
  #pass

#post /subnet/<name> data: {name :}
@app.route('/subnet/<string:name>/item' , methods=['POST'])
def create_free_in_subnet(name):
  request_data = request.get_json()
  for subnet in subnets:
    if subnet['name'] == name:
        new_free_subnet = {
            'name': request_data['name'],
            'list': request_data['list']
        }
        subnet['free subnets'].append(new_free_subnet)
        return jsonify(new_free_subnet)
  return jsonify ({'message' :'Subnets not found'})
  #pass

#get /subnet/<name>/item data: {name :}
@app.route('/store/<string:name>/item')
def get_free_subnets_in_subnet(name):
  for subnet in subnets:
    if subnet['name'] == name:
        return jsonify( {'free_subnets':subnet['free_subnets'] } )
  return jsonify ({'message':'Subnets not found'})

  #pass

app.run(port=5000)