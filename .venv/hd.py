from flask import *
import pymysql
from twisted.conch.insults.window import cursor
app=Flask(__name__)
@app.route("/login",methods=["GET","POST"])
def login():
    if request.method=="GET":
        return render_template("qd.html")
    conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", password="13643929221Li.", charset="utf8",db="users")
    cur = conn.cursor()
    user1 = request.form.get("user")
    password1 = request.form.get("password")

    cur.execute("select user.password from user where user.user1=%s",[user1])
    li = cur.fetchone()
    print(li)
    if li ==None:
        return render_template("qd.html")
    if li[0] == password1:
        cur.execute("select name from user where user.user1=%s",[user1])
        na=cur.fetchone()
        nam=na[0]
        cur.close()
        conn.close()
        return f"<h1 style='color:green'>{nam}   登陆成功</h1>"
    else:

        cur.close()
        conn.close()
        return render_template("qd.html")
@app.route("/res",methods=["GET","POST"])
def res():
    if request.method=="GET":
        return render_template("res.html")
    user_name=request.form.get("name")
    user_user=request.form.get("user")
    password1=request.form.get("password1")
    password2=request.form.get("password2")
    if password1 ==password2 and password1 !="" and user_name!="":
        conn=pymysql.connect(host="127.0.0.1",port=3306,user="root",password="13643929221Li.",charset="utf8",db="users")
        cur=conn.cursor()
        sql="""
            insert into user values(%s,%s,%s);
        """
        cur.execute(sql,[user_user,password1,user_name])
        conn.commit()
        cur.close()
        conn.close()
        return (f"""
            <h1>注册成功</h2>
            <h2>{user_name}</h2>
            <h2>{user_user}</h2>
        """)
    else:
        return render_template("res.html")
if __name__=="__main__":
    app.run(debug=True,host="0.0.0.0")

