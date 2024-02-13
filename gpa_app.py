import json
from flask import Flask ,request, request_started
import pickle
app=Flask(__name__)
print(__name__,__file__)

@app.route("/usecase_name",methods=["GET"])
def usecase():
    return("this is test usecase")



@app.route("/predict_gpa",methods=["POST"])
def predict():
    request_data= request.json["sat_score"]
    with open("C:\\Users\\selva\\Downloads\\GAP_Prediction.pkl", 'rb') as file:  
        load_model = pickle.load(file)
    gpa_result=load_model.predict([[request_data]])[0][0]
    return json.dumps({"gpa+grade":gpa_result})

app.run(port="8090") 


    