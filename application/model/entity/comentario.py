class Comentarios:

    def __init__(self, id, id_noticia, nome, email, texto):
        self._id = id
        self._id_noticia = id_noticia
        self._nome = nome
        self._email = email
        self._texto = texto

        
    def get_id(self):
        return self._id
        
    def get_id_noticia(self):
        return self._id_noticia

    def get_nome(self):
        return self._nome

    def get_email(self):
        return self._email

    def get_texto(self):
        return self._texto

