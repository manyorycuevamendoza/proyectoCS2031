from app import app
import re
from flask import render_template, request, redirect, flash
from app import db
from app.models import NewUser
import requests
import json
from cryptography.hazmat.primitives import hashes

def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if not username or not password:
            return "Missing form parameter username or password"
        try:
            user = NewUser.query.filter(NewUser.username == username).first()
            if user == None or password != user.password:
                return "Invalid user or password"
            password = bytes(password, "utf-8")
            digest = hashes.Hash(hashes.SHA256())
            digest.update(password)
            hashedPassword = str(digest.finalize())
            return redirect("/profile?username="+username+"&password="+hashedPassword)
        except Exception as err:
            print(err)
            return "Error while accesing user. Try again."
    return render_template("login.html")


#registrando usuarios
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        email= request.form["email"]

        #verificando si el usuario y el email ya existen
        user = NewUser.query.filter(NewUser.username == username).first()
        if user != None:
            return "Usuario ya registrado"

        email = NewUser.query.filter(NewUser.email == email).first()
        if email != None:
            return "Email ya registrado"

        #creando el usuario
        try:
            user = NewUser(username=username, password=password, email=email)
            db.session.add(user)
            db.session.commit()
            return redirect("/login")
        except Exception as err:
            print(err)
            return "Error while creating user. Try again."
    return render_template("register.html")