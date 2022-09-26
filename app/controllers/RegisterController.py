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
        try:#el try es para que si hay un error no se rompa la app
            newuser = NewUser.query.filter(NewUser.username == username).first()
            newemail = NewUser.query.filter(NewUser.email == email).first()
        except Exception as err:
            print(err)
            return "Error while creating user. Try again."
        if newuser !=None or newemail !=None:
            return "User or email already exists"

        newuser = NewUser(username=username,email=email,password=password)
        try: 
            db.session.add(newuser)
            db.session.commit()
        except Exception as err:
            print(err)
            return "Error while creating user. Try again."
        return redirect("/login")
    return render_template("register.html")#si no es post, se renderiza la pagina de registro, osea que es get
