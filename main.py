from flask import Flask, render_template, session, request , redirect, url_for
from datetime import datetime
import sqlite3


app = Flask(__name__,template_folder="F:\CITS3403\chat-app\myproject")



db= sqlite3.connect('F:\CITS3403\chat-app\myproject\data\loginDetail.db')    
print("z")

@app.route('/')
def index():
    return render_template('login.html')

@app.route("/login", methods=['POST'])


def login():
   username = request.form['username']
   password = request.form['password']
   db= sqlite3.connect('F:\CITS3403\chat-app\myproject\data\loginDetail.db') 
   cur=db.cursor()
   cur.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
   user= cur.fetchone()
   db.close()
  
   if user:
        return redirect(url_for('main'))
   else:
        error = 'Invalid username or password'
        return render_template('login.html', error=error)

@app.route("/main")
def main():
    return render_template("html.html")
    
@app.route("/register",methods=["POST"])
def register():
    if request.method == 'POST':
        # 获取表单数据
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        password_confirm = request.form['password-confirm']
        
        print(f"username: {username}, email: {email}, password: {password}, confirm_password: {password_confirm}")
        # 在这里将数据插入数据库
        db= sqlite3.connect('F:\CITS3403\chat-app\myproject\data\loginDetail.db')
        cur = db.cursor()
        cur.execute("INSERT INTO users (username, email, password) VALUES (?, ?, ?)", (username, email, password))
        db.commit()
        cur.close()
        msg="成功"
        return '注册成功！'

    return render_template('register.html')


if __name__ == '__main__':
    app.run()