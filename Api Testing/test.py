from flask import Flask , request , jsonify

app = Flask(__name__)

@app.route('/Nikko',methods=['GET' , 'POST'])              
def test():
    if(request.method == 'POST'):
        a = request.json['num1']
        b = request.json['num2']
        result = a+b
        return jsonify(str(result))

@app.route('/abc/nick',methods=['POST'])
def test1():
    if(request.method == 'POST'):
        a = request.json['num3']
        b = request.json['num4']
        result = a+b
        return jsonify(str(result))

@app.route('/abcd',methods=['POST'])
def test2():
    if(request.method == 'POST'):
        a = request.json['nikhil']
        b = request.json['patre']
        result = a+b
        return jsonify(str(result))

@app.route('/abc',methods=['POST'])
def test3():
    if(request.method == 'POST'):
        a = request.json['num5']
        b = request.json['num6']
        result = a+b
        return jsonify(str(result))

if __name__ == '__main__':
    app.run()

