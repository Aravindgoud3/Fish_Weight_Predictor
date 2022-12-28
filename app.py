from flask import Flask, render_template, url_for, request
import joblib
import sklearn


app=Flask(__name__)
model=joblib.load(r"C:\Users\kalali aravindgoud\Desktop\Dataset\finalm1.joblib")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add',methods=['GET','POST'])
def add():
    if request.method=='POST':
        y1=float(request.form.get('y1'))
        y2=float(request.form.get('y2'))
        y3=float(request.form.get('y3'))
        y4=float(request.form.get('y4'))
        y5=float(request.form.get('y5'))
        y6=float(request.form.get('y6'))
        predict=model.predict([[y1,y2,y3,y4,y5,y6]])
        return render_template('output.html',predict=predict)
    return render_template('add.html')

if __name__=="__main__":
    app.run(debug=True)
