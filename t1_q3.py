def conjunto(a):
    for n in range(1,101):
        num = int(input('Digite algum número: '))
        a += num
        media = a / n
    print(f'A média é igual a {media:.2f}')
  
def main():
    n = 0
    r = conjunto(n)

    return(f'{r}')

if __name__ == "__main__":
    main()
