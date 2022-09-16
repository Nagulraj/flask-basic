'''
Created on : sept 15 2022 
 
@author: Nagul

    
'''
# Import necessary modules


from flask import Flask,request, render_template


app = Flask(__name__)

@app.route('/',methods=['GET'])
def start():

    return render_template('index.html')

@app.route('/result',methods=['POST'])
def submit():
    first_name=request.form.get("fname")
    last_name=request.form.get("lname")
    result={
        "firstname" : first_name,
        "lastname"  : last_name
    }
    return render_template('result.html',result=result)


if __name__== "__main__":
    app.run(host="0.0.0.0", debug = True, port = 5000)