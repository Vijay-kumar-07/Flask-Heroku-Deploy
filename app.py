from flask import Flask

app = Flask(__name__)

@app.route('/')
def test():
    return "Testing Phase"

@app.route('/home')
def home():
    return "Testing Phase in Home PAGE"

if __name__ == "__main__":
    app.run(debug=True)