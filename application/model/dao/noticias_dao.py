
from application.model.entity.noticia import Noticias
#class Dao:
class NoticiasDao:

    def listar_noticia():
        #Retorar uma lista de noticias!
        lista_noticias = [
         Noticias(1, "Com recordes diários, janeiro de 2022 será o mês com maior número de casos da Covid em Minas", "Janeiro será o mês com mais contaminados pelo coronavírus em Minas. O recorde do pico de casos pode ocorrer já neste sábado devido à disparada de infecções provocadas pela variante Ômicron. Mesmo defendido por alguns especialistas, um recuo nas flexibilizações não está na pauta de governo do Estado.Dados da Secretaria de Estado de Saúde (SES-MG) indicam março de 2021 com o mês com mais doentes desde o início da pandemia. Foram 245 mil testes positivos. Porém, apenas nos 21 dias de 2022 já são 239 mil. Desde terça-feira, 20 mil novos casos são registrados a cada 24 horas.<br><a href='https://youtu.be/vCuYRyafLlw'>video com mais detalhes</a> ", 10,"01/02/2022",3457,"r01.jpg","7846"),
         Noticias(2, "Minas Gerais registra 3.922 casos confirmados nas últimas 24 horas", "De acordo com o Informe Epidemiológico do coronavírus desta quinta-feira (24 de março de 2022), até o momento, foram notificados 3.310.675 casos confirmados de infecção humana pela Covid-19, em Minas Gerais, com registro oficial de 60.687 óbitos confirmados. Estão em acompanhamento 60.932 casos e são 3.189.056 casos recuperados. Nas últimas 24 horas, foram 3.922 casos e 49 óbitos confirmados <br><a href='https://youtu.be/vCuYRyafLlw'>video com mais detalhes</a>", "MG","24/03/2022",11452,"r02.jpeg","16478"),
         Noticias(3, "Chuvas no Nordeste", "De acordo com o Informe desta quinta-feira (24 de março de 2022), até o momento, foram confirmados de perdas humana pela Covid-19, em Minas Gerais, com registro oficial de 60.687 óbitos confirmados. Estão em acompanhamento 60.932 casos e são 3.189.056 casos recuperados. Nas últimas 24 horas, foram 3.922 casos e 49 óbitos confirmados <br><a href='https://youtu.be/vCuYRyafLlw'>video com mais detalhes</a>", "PN","24/03/2022",11452,"r03.jpeg","4546"),

         ]

        return lista_noticias

