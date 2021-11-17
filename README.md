# Calcularea factorialului oricarui număr real folosind metoda Monte Carlo

## Introducere
Pentru a calcula factorialul unui număr natural ‘n’ putem folosi direct formula 1×2×3×..×n, însă, problema evoluează atunci când încercăm să calculăm factorialul unui număr real, de exemplu, (1/2)!, √2! sau chiar e!.

Această problemă a fost rezolvată chiar în secolul al XVIII-lea, de către matematicianul elvețian Leonard Euler, prin utilizarea unei integrale simple.

## Funcția Gamma
Funcția Gamma este o funcție ce are ca parametru un numar real (aceasta poate fi extinsă și în spațiul complex), și returnează factorialul acesteia. Funcția este de forma unei integrale definite.

<p align="center">
<img src="https://i.ibb.co/tqC6C3Q/Gamma-56a8fa853df78cf772a26da7.jpg" alt="Image not found" width="190">
</p>
  
Avantajul folosirii unei integrale în această problemă este că, pentru a obține factorialul unui număr, trebuie să calculăm aria de sub grafic, iar aproximarea Monte Carlo excelează în astfel de situații.

<p align="center">
<img src="https://i.ibb.co/t45LcRk/graph.png" alt="Image not found" width="400">
</p>

## Metodă de rezolvare
Pentru a rezolva această problemă vom folosi o metodă asemănătoare celei prezentate la laborator pentru a calcula valoarea lui pi. Vom avea o singura valoare de intrare- numărul al cărui factorial vrem să îl calculăm (n).

În primul rând, realizăm un “bounding box” în jurul zonei în care vom lua valori aleatorii. Acest bounding box va avea drept colțuri - origininea (0, 0), (0, f(n) + err), (3.4 * n, 0), (3.4 * n, f(n) + err)

Am ales f(n) + err pentru a avea o mică marjă de eroare atunci când suntem aproape de valoarea maximă a funcției din interiorul integralei (această valoare se află mereu în punctul x=n). Și am ales 3 * n deoarece, pentru n < 100, f(3.4 * n) tinde spre 0 și nu are sens să plotăm puncte după acea valoare.

Odată alese punctele, calculăm raportul dintre cele care se află sub grafic, față de cele care se află peste grafic. Pentru a face verificarea unui punct, putem verifica dacă din perechea aleasă aleator (x, y), avem y <= f(x), unde f(x) este funcția din interiorul integralei.

Pentru a spori acuratețea, vom repeta acest proces de câteva ori, la final calculând media dintre valorile obținute, astfel acesta fiind răspunsul final.

<p align="center">
<img src="https://i.ibb.co/8sChBT9/plot.png" alt="Image not found" width="400">
</p>
