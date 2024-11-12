def algorytm_pleckaowy(wagi, zyski, poj, ilosc): 
    if ilosc == 0 or poj == 0: 
        return 0
    
    if wynik[ilosc][poj] != -1: 
        return wynik[ilosc][poj]
    
    if wagi[ilosc-1] <= poj: 
        wynik[ilosc][poj] = max(zyski[ilosc-1] + algorytm_pleckaowy(wagi, zyski, poj - wagi[ilosc-1], ilosc - 1), 
                      algorytm_pleckaowy(wagi, zyski, poj, ilosc - 1))
    else:
        wynik[ilosc][poj] = algorytm_pleckaowy(wagi, zyski, poj, ilosc - 1)

    return wynik[ilosc][poj]

zyski = [12, 43, 88] 
wagi = [1, 12, 22] 
pojemnosc = 50

wynik = []
for i in range(len(zyski) + 1):
    wynik.append([-1] * (pojemnosc + 1))

print(algorytm_pleckaowy(wagi, zyski, pojemnosc, len(zyski)))
