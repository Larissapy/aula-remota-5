def e_par(n):
    return n % 2 == 0

def numeros_pares_impares(p, i):
    for n in range(100):
        num = int(input())
        if e_par(num):
            p += 1
        else:
            i += 1
    print(f'Temos {p} números pares')
    print(f'Temos {i} números ímpares')

def main():
    par = 0
    impar = 0
    numeros_pares_impares(par, impar)

if __name__ == "__main__":
    main()
    
