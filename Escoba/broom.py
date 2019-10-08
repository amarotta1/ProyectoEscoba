import random


class Broom():

    def __init__(self):

        self.mazo = {"1 Basto":1,"1 Copa":1,"1 Oro":1,"1 Espada":1,"2 Basto":2,"2 Copa":2,"2 Oro":2,"2 Espada":2,
        "3 Basto":3,"3 Copa":3,"3 Oro":3,"3 Espada":3,"4 Basto":4,"4 Copa":4,"4 Oro":4,"4 Espada":4,
        "5 Basto":5,"5 Copa":5,"5 Oro":5,"5 Espada":5,"6 Basto":6,"6 Copa":6,"6 Oro":6,"6 Espada":6,
        "7 Basto":7,"7 Copa":7,"7 Oro":7,"7 Espada":7,"10 Basto":8,"10 Copa":8,"10 Oro":8,"10 Espada":8,
        "11 Basto":9,"11 Copa":9,"11 Oro":9,"11 Espada":9,"12 Basto":10,"12 Copa":10,"12 Oro":10,"12 Espada":10}

        self.mazoMezclado = list(self.mazo.keys())
        random.shuffle(self.mazoMezclado)
       

        self.manoHumano = []
        self.manoCpu = []
        self.mesa = []

        self.puntosHumano = 0
        self.puntosCpu = 0

        self.tocoHumano = []
        self.tocoCpu = []

        self.escobaHumano = 0
        self.escobaCpu = 0

 

          

    def repartir(self):            

       #reparte las cartas a los jugadores del mazo ya mezclado una y una
        
        if len(self.manoHumano) == 0 and len(self.manoCpu)==0 and len(self.mazo) >=6:

            for i in range(3):
                self.manoHumano.append(self.mazoMezclado.pop()) #pop para sacar la carta de la lista como si saliera del mazo
                self.manoCpu.append(self.mazoMezclado.pop())
           
           
        #cuando retorno dos valores se vuelve una tupla , puedo obtener los valores si hago a,b= objeto.repartir()
        
        return self.manoHumano, self.manoCpu, self.mazoMezclado

    def cartasMesa(self): #solo se llama la primera vez, en la primera ronda

        for i in range(4):
            self.mesa.append(self.mazoMezclado.pop())
        
        return self.mesa , self.mazoMezclado

    def sumar15(self):
        #para cpu : Debe comprobar si las cartas de la mesa suman 15, si no es asi fijarse si con alguna de la mano suma 15,
        #devolver cuales son las cartas que cumplen esa condicion
        #para Humano: debe comprobar que las cartas que selecciono efectivamente sumen 15
        pass

    def jugarcartas(self):
        #si sumaron 15 llevarlas al toco,si no dejar una carta en la mesa
        #si no quedan cartas en la mesa = escoba
        pass

    def puntos(self):
        
        self.puntosHumano = self.escobaHumano*2
        self.puntosCpu = self.escobaCpu*2

        if len(self.tocoCpu)>len(self.tocoHumano) :
            self.puntosCpu +=1
        else:
            self.puntosHumano +=1
        
        if "7 Oro" in self.tocoCpu:
            self.puntosCpu +=1
        elif "7 Oro" in self.tocoHumano:
            self.puntosHumano +=1

        return self.puntosCpu, self.puntosHumano

    
        

 


