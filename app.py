from flask import Flask



app = Flask(__name__)

#creating the first route
@app.route("/")
def index():
    return "Salut mes amis !"

if __name__ == "__main__":
    app.run(debug=True)

