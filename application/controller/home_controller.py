from hashlib import new
import imp
from flask import Flask, render_template, url_for, request, jsonify, json
from application.model.dao.noticias_dao import NoticiasDao
from application.model.dao.comentarios_dao import ComentarioDao
from application import main
from application.model.entity.comentario import Comentarios
from application.model.entity.noticia import Noticias

@main.route("/")
def home():
    noticias = NoticiasDao.listar_noticia()
    return render_template("index.html",
       noticias= noticias
    )

