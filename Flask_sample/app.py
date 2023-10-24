from flask import Flask,request,jsonify

app=Flask(__name__)

@app.route('/',methods=["GET"])

def home():
    return "Hello World"

@app.route('/home',methods=["POST"])

def index():
    data=request.json.get('data')
    return jsonify({'message':data})

if __name__=='__main__':
    app.run()