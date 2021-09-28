from flask import Flask

app = Flask(__name__)
@app.route('/', methods=['GET'])
# Function that would be executed when the above URL is hit.
def welcome():
    print("Docker,heroku demo program is successful!")

if __name__ == "__main__":
    app.run()