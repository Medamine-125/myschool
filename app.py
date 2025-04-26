from flask import Flask



app = Flask(__name__)

#creating the first route
@app.route("/")
def index():
    return f'Homepage'

if __name__ == "__main__":
    app.run(debug=True)

