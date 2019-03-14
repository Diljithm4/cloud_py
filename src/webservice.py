from flask import  *
import MySQLdb
con=MySQLdb.connect(host="localhost",port=3306,user="root",passwd="root",db="cloud")
cmd=con.cursor()
app=Flask(__name__)



@app.route('/registration',methods=['post'])
def registration():
  try:
    name=request.args.get('name')
    password=request.args.get('pass')
    phone=request.args.get('phone')
    email=request.args.get('email')

    cmd.execute("insert into login values(null,'" + name + "','" + password + "','" + phone + "','"+email+"')")
    con.commit()
    return jsonify({"task":"success"})
  except:
    return jsonify({"task": "failed"})

@app.route('/reset',methods=['post'])
def reset():
  try:
    name=request.args.get('name')
    mail=request.args.get('mail')
    phone=request.args.get('phone')
    cmd.execute("insert into login values(null,'" + name + "','" + phone + "','"+mail+"')")
    con.commit()
    return jsonify({"task":"success"})
  except:
    return jsonify({"task": "failed"})

@app.route('/login',methods=['post'])
def login():
  try:
    name=request.args.get('name')
    password=request.args.get('pass')


    cmd.execute("insert into login values(null,'" + name + "','" + password + "')")
    con.commit()
    return jsonify({"task":"success"})
  except:
    return jsonify({"task": "failed"})

if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000)