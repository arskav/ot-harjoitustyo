import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti


class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()

    def test_alkusaldo_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)     

    def test_alku_maukkaat_myyty_oikein(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)     
    
    def test_alku_edulliset_myyty_oikein(self):
        self.assertEqual(self.kassapaate.edulliset, 0)     

    #maukas lounas
    #maksu riittävä: kassassa oleva rahamäärä kasvaa lounaan hinnalla 
    def test_maukkaat_maksu_OK(self):
        self.kassapaate.syo_maukkaasti_kateisella(1000)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)  

    #maksu riittävä: vaihtorahan suuruus on oikea
    def test_maukkaat_maksu_OK_palautus(self):
        palautus = self.kassapaate.syo_maukkaasti_kateisella(610)
        self.assertEqual(palautus, 210)     

    # maksu on riittävä: myytyjen lounaiden määrä kasvaa
    def test_maukkaat_maksu_OK_myydyt(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassapaate.maukkaat, 1)     
     
    #maksu ei ole riittävä: kassassa oleva rahamäärä ei muutu 
    def test_maukkaat_maksu_ei_OK_saldo_samana(self):
        self.kassapaate.syo_maukkaasti_kateisella(300)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)     

    #maksu ei ole riittävä: kaikki rahat palautetaan vaihtorahana
    def test_maukkaat_maksu_ei_OK_palautus(self):
        palautus = self.kassapaate.syo_maukkaasti_kateisella(123)
        self.assertEqual(palautus, 123)     
    

    #maksu ei ole riittävä: myytyjen lounaiden määrässä ei muutosta
    def test_maukkaat_maksu_ei_OK_myydyt_samana(self):
        self.kassapaate.syo_maukkaasti_kateisella(350)
        self.assertEqual(self.kassapaate.maukkaat, 0)     

    
   #edullinen lounas
   #maksu riittävä: kassassa oleva rahamäärä kasvaa lounaan hinnalla 
    def test_edulliset_maksu_OK(self):
        self.kassapaate.syo_edullisesti_kateisella(1000)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)  

    #maksu riittävä: vaihtorahan suuruus on oikea
    def test_edulliset_maksu_OK_palautus(self):
        palautus = self.kassapaate.syo_edullisesti_kateisella(610)
        self.assertEqual(palautus, 370)     

    # maksu on riittävä: myytyjen lounaiden määrä kasvaa
    def test_edulliset_maksu_OK_myydyt(self):
        self.kassapaate.syo_edullisesti_kateisella(260)
        self.assertEqual(self.kassapaate.edulliset, 1)     
     
    #maksu ei ole riittävä: kassassa oleva rahamäärä ei muutu 
    def test_edulliset_maksu_ei_OK_saldo_samana(self):
        self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)     

    #maksu ei ole riittävä: kaikki rahat palautetaan vaihtorahana
    def test_edulliset_maksu_ei_OK_palautus(self):
        palautus = self.kassapaate.syo_edullisesti_kateisella(123)
        self.assertEqual(palautus, 123)     
    

    #maksu ei ole riittävä: myytyjen lounaiden määrässä ei muutosta
    def test_edulliset_maksu_ei_OK_myydyt_samana(self):
        self.kassapaate.syo_edullisesti_kateisella(150)
        self.assertEqual(self.kassapaate.maukkaat, 0)     

    #maukas
    #Jos kortilla on tarpeeksi rahaa, veloitetaan summa kortilta
    def test_veloitus_maukkaasti_ok(self):
        kortti = Maksukortti(1400)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(kortti.saldo, 1000)


    #Jos kortilla on tarpeeksi rahaa, palautetaan True
    def test_veloitus_maukkaasti_ok_return(self):
        kortti = Maksukortti(500)
        onnistui = self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(onnistui, True)

    #Jos kortilla on tarpeeksi rahaa, myytyjen lounaiden määrä kasvaa    
    def test_veloitus_maukkaasti_ok_maara(self):
        kortti = Maksukortti(500)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    #Jos kortilla ei ole tarpeeksi rahaa, kortin rahamäärä ei muutu  
    def test_veloitus_maukkaasti_ei_ok(self):
        kortti = Maksukortti(100)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(kortti.saldo, 100)
  

    #Jos kortilla ei ole tarpeeksi rahaa, myytyjen lounaiden määrä muuttumaton
    def test_veloitus_maukkaasti_ei_ok_maara(self):
        kortti = Maksukortti(100)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(self.kassapaate.maukkaat, 0)


    #Jos kortilla ei ole tarpeeksi rahaa, palautetaan False
    def test_veloitus_maukkaasti_ei_ok_return(self):
        kortti = Maksukortti(100)
        onnistui = self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(onnistui, False)

    #Kassassa oleva rahamäärä ei muutu kortilla ostettaessa
    def test_edulliset_maksu_ei_ok(self):
        kortti = Maksukortti(100)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)  

    #edullinen
    #Jos kortilla on tarpeeksi rahaa, veloitetaan summa kortilta
    def test_veloitus_edullisesti_ok(self):
        kortti = Maksukortti(1240)
        self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(kortti.saldo, 1000)


    #Jos kortilla on tarpeeksi rahaa, palautetaan True
    def test_veloitus_edullisesti_ok_return(self):
        kortti = Maksukortti(500)
        onnistui = self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(onnistui, True)

    #Jos kortilla on tarpeeksi rahaa, myytyjen lounaiden määrä kasvaa    
    def test_veloitus_edullisesti_ok_maara(self):
        kortti = Maksukortti(500)
        self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(self.kassapaate.edulliset, 1)

    #Jos kortilla ei ole tarpeeksi rahaa, kortin rahamäärä ei muutu  
    def test_veloitus_edullisesti_ei_ok(self):
        kortti = Maksukortti(100)
        self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(kortti.saldo, 100)
  

    #Jos kortilla ei ole tarpeeksi rahaa, myytyjen lounaiden määrä muuttumaton
    def test_veloitus_edullisesti_ei_ok_maara(self):
        kortti = Maksukortti(100)
        self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(self.kassapaate.edulliset, 0)


    #Jos kortilla ei ole tarpeeksi rahaa, palautetaan False
    def test_veloitus_edullisesti_ei_ok_return(self):
        kortti = Maksukortti(100)
        onnistui = self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(onnistui, False)

    #Kassassa oleva rahamäärä ei muutu kortilla ostettaessa
    def test_edulliset_maksu_ei_ok(self):
        kortti = Maksukortti(100)
        self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)  



    #Kortille rahaa ladattaessa kortin saldo muuttuu
    def test_kortille_rahaa(self):
        kortti = Maksukortti(0)
        self.kassapaate.lataa_rahaa_kortille(kortti, 1000)
        self.assertEqual(kortti.saldo, 1000)

    #Kortille rahaa ladattaessa kassassa oleva rahamäärä kasvaa ladatulla summalla    
    def test_kortille_rahaa_kassa(self):
        kortti = Maksukortti(0)
        self.kassapaate.lataa_rahaa_kortille(kortti, 1000)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 101000)

    #Tehtävä 9

    #kortille ei voi ladata negatiivista rahamäärää
    def test_kortille_rahaa_kassa_negatiivinen(self):
        kortti = Maksukortti(0)
        self.kassapaate.lataa_rahaa_kortille(kortti, -1000)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)