def parcelas(p, valor):
    
    for p in range(1, 25):
        v = valor / p
        print(f'{p}x de R$ {v:.2f}')

def main():
    p = 1
    v = int(input('Digite o valor: '))

    resultado = parcelas(p, v)

    return(f'{resultado}')
    
    

if __name__ == "__main__":
    main()
        
