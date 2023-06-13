from PyQt5 import QtWidgets, uic

class Escape:
    def __init__(self) -> None:
        app = QtWidgets.QApplication([])
        self.tela_inicial = uic.loadUi("telas/inicio.ui")
        self.sala1 = uic.loadUi("telas/sala1.ui")
        self.sala2 = uic.loadUi("telas/sala2.ui")
        self.sala3 = uic.loadUi("telas/sala3.ui")
        self.sala4 = uic.loadUi("telas/sala4.ui")
        self.sala5 = uic.loadUi("telas/sala5.ui")
        self.final = uic.loadUi("telas/final.ui")


#       BOTÕES TELA INICIAL 
        self.tela_inicial.btIniciar.clicked.connect(self.abrir_sala1)
#       BOTÕES SALA 1
        self.sala1.btObj.clicked.connect(self.abrir_sala2)
        self.sala1.btDesistir.clicked.connect(self.desistir)
#       BOTÕES SALA 2        
        self.sala2.btObj.clicked.connect(self.abrir_sala3)
        self.sala2.btDesistir.clicked.connect(self.desistir)
#       BOTÕES SALA 3
        self.sala3.btObj.clicked.connect(self.abrir_sala4)
        self.sala3.btDesistir.clicked.connect(self.desistir)
#       BOTÕES SALA 4
        self.sala4.btObj.clicked.connect(self.abrir_sala5)
        self.sala4.btDesistir.clicked.connect(self.desistir)
#       BOTÕES SALA 5        
        self.sala5.btObj.clicked.connect(self.abrir_final)
        self.sala5.btDesistir.clicked.connect(self.desistir)
#       BOTÕES FINAL        
        self.final.btDesistir.clicked.connect(self.desistir)


        self.tela_inicial.show()
        app.exec()

    def abrir_sala1(self):
        self.tela_inicial.close()
        self.sala1.show()

    def abrir_sala2(self):
        self.sala1.close()
        self.sala2.show()         

    def abrir_sala3(self):
        self.sala2.close()
        self.sala3.show()         

    def abrir_sala4(self):
        self.sala3.close()
        self.sala4.show()         

    def abrir_sala5(self):
        self.sala4.close()
        self.sala5.show()

    def abrir_final(self):
        self.sala5.close()
        self.final.show()

    def desistir(self):
        self.sala1.close()    
        self.sala2.close()    
        self.sala3.close()    
        self.sala4.close()    
        self.sala5.close()    
        self.final.close()    

Escape()
