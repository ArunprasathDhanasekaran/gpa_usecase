import json
from flask import Flask ,request, request_started,render_template
import pickle
app=Flask(__name__)
print(__name__,__file__)

@app.route("/usecase_name",methods=["GET"])
def usecase():
    return("this is test usecase")

#this is to test git

@app.route("/predict_gpa",methods=["POST"])
def predict():
    request_data= request.json["sat_score"]
    with open("C:/Users/selva/Downloads/GAP_Prediction.pkl", 'rb') as file:  
        load_model = pickle.load(file)
    gpa_result=load_model.predict([[request_data]])[0][0]
    return json.dumps({"gpa+grade":gpa_result})


@app.route("/home",methods=["GET"])
def home():
    return render_template("index.html")

@app.route('/handel_data',methods=["POST"])
def handel_data():
    student_name=request.form.get("student_name")
    sat_score=float(request.form.get("sat_score"))
    with open("C:/Users/selva/Downloads/GAP_Prediction.pkl", 'rb') as file:  
        load_model = pickle.load(file)
    gpa_result=load_model.predict([[sat_score]])[0][0]
    return render_template("predict.html",gpa_result=gpa_result,student_name=student_name)

if __name__ == "__main__":
    app.run(port="8091") 


    