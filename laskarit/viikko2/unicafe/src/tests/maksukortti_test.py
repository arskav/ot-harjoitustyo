import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_saldo_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")    

    def test_rahan_lataaminen_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(1234)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 22.34 euroa")    

    def test_rahan_ottaminen_toimii_oikein(self):
        self.maksukortti.ota_rahaa(525)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 4.75 euroa")    


    def test_rahan_ottaminen_saldo_ei_muutu(self):
        self.maksukortti.ota_rahaa(1001)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")    

    def test_rahan_ottaminen_kun_riitti(self):
        self.assertEqual(self.maksukortti.ota_rahaa(500), True)

    def test_rahan_ottaminen_kun_ei_riita(self):
        self.assertEqual(self.maksukortti.ota_rahaa(1500), False)
    