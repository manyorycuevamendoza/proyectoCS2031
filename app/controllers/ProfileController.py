from app import app
import re
from flask import render_template, request, redirect, flash
from app import db
from app.models import NewUser
import requests
import json

def profile():
    user = request.args
    username = user.get("username")
    password = user.get("password")
    return render_template("profile.html", username=username, password=password)

"""que muestre un form que le pida al usuario ingresar 
su nombre y contraseña y le permita borrar toda
 la información de su cuenta."""
def delete():
    if request.method=='POST':
        username=request.form["username"]
        password=request.form["password"]


        if username==None or username=="" or password==None or password=="":
            return "Missing form parameter username or password"
        Usuario=NewUser.query.filter(NewUser.username==username).first()
        if Usuario==None or Usuario.password!=password:
            return "Invalid username or password"
        try:
            db.session.delete(Usuario)
            db.session.commit()
        except Exception as err:
            print("Error inesperado",err)
            return "Error while deleting user. Try again."
        return redirect("/index")
    return render_template('delete.html')

def update():
    if request.method=='POST':
        username=request.form['username']
        password=request.form['password']
        email=request.form['email']
        newusername=request.form['newusername']
        if not username and not password and not email:
            return "Missing username or password or email"
        user =NewUser.query.filter(NewUser.username==newusername).first()
        if user==None:
            return "Invalid username"
        
        if username:
            user.username=username
        if password:
            user.password=password
        if email:
            user.email=email
        try:
            db.session.commit()
        except Exception as err:
            print("Error inesperado",err)
            return "Invalid new parameters"
        return redirect("/index")
    return render_template('update.html')



