import numpy as np
import Flask, request, jsonify, render_template
import pickle
import os
 #app name
app = Flask(__name__) 
#load the saved model
def load_model(): 
    return pickle.load(open('iris_model.pkl', 'rb')) #home 
@app.route('/')
def home(): 
    return render_template('index.html]') 

@app.route('/predict]',methods=['POST]'])
def predict(): 
    return render_template('index.html') 
if __name__ == "__main__": 
    port=int(os.environ.get('PORT',5000))    
    app.run(port=port,debug=True,use_reloader=False)