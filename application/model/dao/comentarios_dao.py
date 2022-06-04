
from application.model.entity.comentario import Comentarios
#class Dao:
class ComentarioDao:

    def Listar_Comentario():
        #Retorar uma lista de noticias!
        lista_Comentarios = [
            Comentarios(1, 1, 'marcelo', 'marcelogbc9@gmail.com', 'uma grande ideia'),
            Comentarios(2, 2, 'Ana', 'ana@gmail.com', 'Gostei !'),
            Comentarios(3, 1, 'Joana', 'Joana@gmail.com', 'Legal !'),
            Comentarios(4, 2, 'Marcia', 'marcia@gmail.com', 'Interessante !'),
            Comentarios(5, 3, 'Paula', 'paula@gmail.com', 'uma noticia clara sobre rolou !'),
            Comentarios(6, 3, 'Erika', 'erika@gmail.com', 'uma coisa acontece as vezes !'),

         ]

        return lista_Comentarios

