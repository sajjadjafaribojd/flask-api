from flask import Flask,request,jsonify

app=Flask(__name__)

def error_result(status,message):
    results={}
    results["error"]={}
    results["error"]["status"]=status
    results["error"]['message']=message
    return jsonify(results)

@app.route('/api/v1/getdomain',methods=['GET'])
def getdomain():
    try:
        domain = request.values["domain"]
        status = request.values["status"]
        ouput= {"domain":domain,"status":status}
        return jsonify(ouput)
    except Exception as e:
        return error_result("fail","insert error%s"%e) 
        

if __name__ == '__main__':
   #app.run(debug = True) #defualt port: 5000
   app.run(debug=True,host="127.0.0.1",port=5000)