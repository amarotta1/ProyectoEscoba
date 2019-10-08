from broom import Broom
import unittest


prueba = Broom()


prueba.repartir()
prueba.cartasMesa()

prueba.escobaCpu =2
prueba.escobaHumano = 3

prueba.tocoHumano.extend(["10 Espada","8 Copa","4 Oro"])
prueba.tocoCpu.extend(["7 Oro","2 Basto"])



class TestBromm(unittest.TestCase):

    def test_cartas_en_mano_Humano(self):
        self.assertEqual(len(prueba.manoHumano), 3)
    
    def test_cartas_en_mano_Compu(self):
        self.assertEqual(len(prueba.manoCpu), 3)

    def test_cartas_mesa(self):        
        self.assertEqual(len(prueba.mesa),4)

    def test_mazo_saca_cartas(self):
        self.assertEqual(len(prueba.mazoMezclado),30)

    def test_puntos(self):
        self.assertEqual(prueba.puntos(),(5,7))

    





if __name__ == "__main__":
    unittest.main()
