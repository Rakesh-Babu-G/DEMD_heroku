from flask import Flask, render_template
from flasgger import Swagger

#WSGI
#app = Flask(__name__)
#Swagger(app)
#@app.route('/')
#def welcome():
    #return "Welcome to Flask intro class."
#    return render_template("index.html")
#@app.route('/name/<your_name>')
#def names(your_name):
#    return f"Welcome to Flask intro class, {your_name}!"
#@app.route('/checking_req', methods = ['POST', 'GET'])
#def get_req_parameters():
    #""" 
    #practicing swagger
    #---
    #- name: student name
    #in:query
    #type:string
    #required: true
    #- name:roll_no
    #in:query
    #type:number
    #required :true

    #"""
#    name = request.args.get("Student_name")
#    num = request.args.get("roll_no")
#    return f"Student name is {name} and roll_no is {num} in praxis"

#if __name__ == "__main__":
#    app.run(debug = True, host= "0.0.0.0", port=3400)

# Importing the required package
from flask import Flask, render_template, request
#import flasgger
from flasgger import Swagger

# Defining the name (will fetch from the actual file name)
app = Flask(__name__)
Swagger(app)

# Defingin the path or url attahced after the local ip
@app.route('/', methods=['GET'])
# Function that would be executed when the above URL is hit.
def welcome():
    return render_template("index.html")

# Defining second url
@app.route('/name/<your_name>')
# Function that should be executed when this URL is hit
def names(your_name):
    return f"Welcome to Praxis {your_name}"
# Defining using Swagger
@app.route('/checking_req',methods=['POST','GET'])
def get_req_parameters():
    """ Practicing Swagger
    ---
    parameters:
     - name: Student_name
       in: query
       type: string
       required: true
     - name: roll_no
       in: query
       type: number
       required: true
    responses:
       200:
            description: Result is

    """
    name = request.args.get("Student_name")
    roll_no = request.args.get("roll_no")
    return f"Student name is {name} and roll no is {roll_no} in Praxis"


if __name__ == "__main__":
    # Use debug only when required. With debug no need to stop the server every time.
    #app.run(debug=True)
    app.run()
    # Use Cntl+C to stop the server.
