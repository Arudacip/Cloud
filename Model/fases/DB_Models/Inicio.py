from Model.fases.DB_Models.faseModel import faseModel
from Model.fases.DB_Models.faseLigacao import faseLigacao
from abc import ABC, abstractmethod

class Inicio(faseModel):

    Code = 0
    classNameFaseImplementation = 'Inicio'
    CorFase = 'blue'
    LabelFase = 'Inicio'
    NomeFase = 'Inicio'
    ShapeFase = 'dot'

    def __init__(self):
        ligacao = faseLigacao()
        ligacao.CodeFaseAtual = 0
        ligacao.CodeProximaFase = None
        
        listaLigacao = list()
        listaLigacao.append(ligacao) #Fazer isso para todas as ligações

        pass
    
