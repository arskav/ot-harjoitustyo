```mermaid
   classDiagram
      Monopoli "1" --> "1" Pelaajat
      Monopoli "1" --> "1" Pelilauta
      Monopoli "1" --> "1" Nopat
      Pelaajat "1" --> "2..8" Pelaaja
      Pelilauta "1" --> "40" Ruudut
      Ruudut "1" --> "1" Ruudut
      Pelinappula "1" --> "1" Ruudut
      Pelaaja "1" --> "1" Pelinappula      
      Nopat "1" --> "1" Pelinappula  
```