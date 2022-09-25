from app import app
import re
from flask import render_template, request, redirect, flash
from app import db
from app.models import NewUser
import requests
import json

#registrando usuarios
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        email= request.form["email"]
        if username==None or username=="" or password==None or password=="" or email==None or email=="":
            return "Missing form parameter username or password or email"
        #verificando si el usuario y el email ya existen

        #creando el usuario
        try:
            user = NewUser.query.filter(NewUser.username == username).first()
            email = NewUser.query.filter(NewUser.email == email).first()
        except Exception as err:
            print(err)
            return "Error while creating user. Try again."
        if user !=None or email !=None:
            return "User or email already exists"

        newuser = NewUser(username=username, password=password, email=email)
        try: 
            db.session.add(newuser)
            db.session.commit()
            return redirect("login.html")
        except Exception as err:
            print(err)
            return "Error while creating user. Try again."
    return render_template("register.html")
