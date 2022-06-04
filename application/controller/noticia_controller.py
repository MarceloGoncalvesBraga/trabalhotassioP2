from flask import render_template
from application import main
from application.model.dao.noticias_dao import NoticiasDao
from application.model.entity.noticia import Noticias
from application.model.dao.comentarios_dao import ComentarioDao
from application.model.entity.comentario import Comentarios

from flask import Flask, render_template, url_for, request, jsonify, json
import re 



@main.route("/exibir_noticia/<int:id>")
def exibir_noticia(id):
    noticias_dao = NoticiasDao.listar_noticia()
    comentarios = ComentarioDao.Listar_Comentario()

    for noticia in noticias_dao:

        if noticia.get_id() == id:
            com = []
            for comentario in comentarios:
               if comentario.get_id_noticia() == noticia.get_id():
                  com.append(comentario) 

            return render_template("exibir-noticia.html",
                noticia=noticia,
                comentarios = com   )
    return render_template("home.html", noticias=noticias_dao)

@main.route("/salvar", methods=['POST', 'GET'])
def Salvar():    
  comentarios = ComentarioDao.Listar_Comentario()
  if request.method == "POST":
    id_noticia = request.form.get('id_noticia', '...')

    if id_noticia != "": 
      some = 0
      id_noticia = request.form.get('id_noticia', '...')
      nome = request.form.get('nome', '----')
      email = request.form.get('email', '----')
      texto = request.form.get('texto', '...')
      if len(nome) == "":
        nome = "vazio"
        some = 1
      regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
      if(re.search(regex,email)):  
        print("Email valido")  
      else:  
        print("Invalido Email") 
        some += 1 
      
      if some == 0:
       comentarios.append((Comentarios(id=100,id_noticia=id_noticia,nome=nome,email=email, texto=texto)))
       print('\t------------------Comentarios------------------------')
       print('\t Nome:',nome)
       print('\t Email:',email)
       print('\t Texto:',texto)
       print('\t-----------------------End---------------------------')
       print('\t-----------------Comentarios-atuais------------------')
       
       for com in comentarios:
         if com.get_id_noticia() == id_noticia:
          print('\nId Noticia', com.get_id_noticia())
          print('Nome:', com.get_nome())
          print('Email:', com.get_email())
          print('Texto:', com.get_texto())

      noticias = NoticiasDao.listar_noticia()
      return render_template("index.html",
       noticias= noticias      )

      