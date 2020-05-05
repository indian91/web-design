from flask import *
import pymysql as sql

app=Flask(__name__)
app.secret_key = "ojfijoifieoijpijpowpinon123445nojpifjpijpejpoppijpj"
@app.route('/home')
def home():
    return render_template('header.html')
@app.route('/signup')
def signup():
    return render_template('signup.html')
@app.route('/login')
def login():
    return render_template('login.html')
@app.route("/signup/signup1",methods=["POST","GET"])
def signup1():
    Fname=request.form.get('Fname')
    Lname=request.form.get('Lname')
    Pass=request.form.get('pass')
    Email=request.form.get('email')
    db=sql.connect(host='localhost',port=3306,user='root',password='',database='bankapp')
    cur=db.cursor()
    cmd="insert into userinfo(Fname,Lname,Pass,Email) values('{}','{}','{}','{}')".format(Fname,Lname,Pass,Email)
    cur.execute(cmd)
    db.commit()
    cmd='select * from userinfo order by Acc desc limit 1'
    cur.execute(cmd)
    data=cur.fetchall()
    data={'Acc':data[0][0],'Fname':data[0][1],'Lname':data[0][2],'Pass':data[0][3],'Email':data[0][4]}
    return render_template('signup1.html',data=data)
@app.route('/login/login1',methods=["POST","GET"])
def transaction():
    #resp = make_response(render_template("transaction.html"))
    #resp.set_cookie('email',email)
    #resp.set_cookie('login','true')
    #return resp
    #session['email']=email
    #session['login']='true'
    acc=request.form.get('acc')
    Pass=request.form.get('pass')
    db=sql.connect(host='localhost',port=3306,user='root',password='',database='bankapp')
    cur=db.cursor()
    cmd="select * from userinfo where Acc='{}'".format(acc)
    cur.execute(cmd)
    data=cur.fetchall()
    if data:
        if Pass==data[0][3]:
            msg=f'Hello {data[0][1]}! You are at transaction page now'
            return render_template('transaction.html',msg=msg)
        else:
            msg='Invalid Password'
            return render_template('login.html',msg=msg)
    else:
        msg='Account not Exist......'
        return render_template('signup.html',msg=msg)
@app.route('/login/login1/debit')
def debit():
    return render_template('debit.html')
@app.route('/login/login1/debit/debit1',methods=['GET','POST'])
def debit1():
    acc=request.form.get('acc')
    Pass=request.form.get('pass')
    bal=request.form.get('bal')
    db=sql.connect(host='localhost',port=3306,user='root',password='',database='bankapp')
    cur=db.cursor()
    cmd="select * from userinfo where Acc='{}'".format(acc)
    cur.execute(cmd)
    data=cur.fetchall()
    if data:
        if Pass==data[0][3]:
            bal=int(bal)
            if bal < data[0][5]:
                bal=data[0][5]-bal
                cmd="update userinfo set balance='{}' where Acc='{}'".format(bal,acc)
                cur.execute(cmd)
                db.commit()
                msg=f'Debit successful and ur updated balance is {bal}'
                return render_template('login.html',msg=msg)
            else:
                msg='Insufficient Balance...'
                return render_template('transaction.html',msg=msg)
        else:
            msg='Invalid Password'
            return render_template('login.html',msg=msg)
        return render_template('transaction.html')
    else:
        msg='Account Does not exist'
        return render_template('signup.html',msg=msg)
@app.route('/login/login1/credit')
def credit():
    return render_template('credit.html')
@app.route('/login/login1/credit/credit1',methods=['GET','POST'])
def credit1():
    acc=request.form.get('acc')
    Pass=request.form.get('pass')
    bal=request.form.get('bal')
    db=sql.connect(host='localhost',port=3306,user='root',password='',database='bankapp')
    cur=db.cursor()
    cmd="select * from userinfo where Acc='{}'".format(acc)
    cur.execute(cmd)
    data=cur.fetchall()
    if data:
        if Pass==data[0][3]:
            bal=int(bal)
            bal=data[0][5]+bal
            cmd="update userinfo set balance='{}' where Acc='{}'".format(bal,acc)
            cur.execute(cmd)
            db.commit()
            msg=f'Credit successful and ur updated balance is {bal}'
            return render_template('login.html',msg=msg)
            
        else:
            msg='Invalid Password'
            return render_template('login.html',msg=msg)
        return render_template('transaction.html')
    else:
        msg='Account Does not exist'
        return render_template('signup.html',msg=msg)
if __name__=='__main__':
    app.run(host='127.0.0.1',port=5000,debug=True)