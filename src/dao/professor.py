import pandas as pd
import os

class Professor:

    CAMINHO = 'src/bd/map.xlsx'

    def __init__(self,id =[], nome = None, titulacao = None, formacao = None, atuacao = None, curso=[], data=None) -> None:
        self.id = id
        self.nome = nome
        self.titulacao = titulacao
        self.formacao = formacao
        self.areaatuacao = atuacao
        self.curso = curso
       
        self.data_resposta = data


    def get_data(self, id):
        df = pd.read_excel(Professor.CAMINHO)

        #profs = Professor
        df2 = df.iloc[id]
        
        profs = Professor()
        lista_cursos = []
        dict_cursos = {}

        for (colname, colvalues) in df2.iteritems():
                lista_cursos.append(colname)

                if ('técnico' in colname.lower() or 'unidades' in colname.lower()) and ('NÃO' not in str(colvalues)) and ('nan' not in str(colvalues)) :
                        dict_cursos[colname] = colvalues
        
        profs = Professor(nome=df2.get(lista_cursos[1]), 
                          titulacao=df2.get(lista_cursos[2]), 
                          formacao=df2.get(lista_cursos[3]),
                          atuacao=df2.get(lista_cursos[4]),
                          curso=dict_cursos,
                          data=df2.get(lista_cursos[0])
                          )
        return profs

    
    def get_professor_name(self):
        

        
        lista_professor = []
        try:
            df = pd.read_excel(Professor.CAMINHO)
            id = 0
            for dados in df['NOME']:
                professor = Professor(nome=dados, id=id)
                lista_professor.append(professor)
                id += 1
            return lista_professor
        except:
            return lista_professor         
    
    def search_bd(self, file):
        if os.path.isfile(f'{Professor.CAMINHO}'):
             os.remove(Professor.CAMINHO)
        file.save(Professor.CAMINHO)
        file.close()
