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

        #verificando si usuario y password existen
        try:
            newuser = NewUser.query.filter(NewUser.username == username).first()
            newpassword = NewUser.query.filter(NewUser.password == password).first()
        except Exception as err:
            print(err)
            return "Error while creating user. Try again."
        if newuser ==None or newpassword ==None:
            return "User or password does not exist"
        
        #teniendo los datos del usuario, se borra
        all_user=NewUser.query.all()
        for user in all_user:
            if user.username==username and user.password==password:
                db.session.delete(user)
                db.session.commit()
        return redirect("/index")
    return render_template("delete.html")



