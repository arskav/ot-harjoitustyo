```mermaid
participant kallen_kortti
    participant ratikka6
    participant bussi244
    participant rautatietori
    participant lippu_luukku    
    participant laitehallinto    
    Main ->> laitehallinto: HKLLaitehallinto()
    Main ->> rautatietori: Lataajalaite()
    Main ->> ratikka6: Lukijalaite()
    Main ->> bussi244: Lukijalaite()
    Main ->> laitehallinto: lisaa_lataaja(rautatietori)
    Main ->> laitehallinto: lisaa_lukija(ratikka6)
    Main ->> laitehallinto: lisaa_lukija(bussi244)
    Main ->> lippu_luukku: Kioski()
    lippu_luukku ->> kallen_kortti: osta_matkakortti("Kalle")
    Main ->> rautatietori: lataa_arvoa(kallen_kortti, 3)
    rautatietori -->> kallen_kortti: 3
    Main ->> ratikka6: osta_lippu(kallen_kortti, 0)
    ratikka6 -->> kallen_kortti: -1.5
    kallen_kortti -->> ratikka6: True
    Main ->> bussi244: osta_lippu(kallen_kortti, 2)
    bussi244 -->> kallen_kortti: -3.5
    kallen_kortti -->> bussi244: False
```