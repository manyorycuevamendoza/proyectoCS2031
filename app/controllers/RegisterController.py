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
        if not username or not password or not email:
            return "Missing form parameter username or password or email"
        #verificando si el usuario y el email ya existen
        user = NewUser.query.filter(NewUser.username == username).first()
        if user != None:
            return "Usuario ya registrado"

        email = NewUser.query.filter(NewUser.email == email).first()
        if email != None:
            return "Email ya registrado"
        else:
            pass

        #creando el usuario
        try:
            user = NewUser(username=username, password=password, email=email)
            db.session.add(user)
            db.session.commit()
            return redirect("/register?username="+username+"&password="+password+"&email="+email)
        except Exception as err:
            print(err)
            return "Error while creating user. Try again."
    return render_template("register.html")