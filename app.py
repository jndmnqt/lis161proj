from flask import Flask, render_template
from data import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/plantae/<plant_type>')
def plantae(plant_type):
    plant_list = plants[plant_type]
    return render_template('plantae.html',plant_type_template=plant_type,plants_template=plant_list)

@app.route('/plantae/<plant_type>/<int:plant_id>')
def plant(plant_type,plant_id):
    plant_details=plants[plant_type][plant_id]
    return render_template('plant.html',plant_details=plant_details)
 
if __name__ == "__main__":
    app.run(debug=True)