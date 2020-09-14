def sequencia(a):
    for a in range(10, 1000, 10):
        print(a, end = ', ')
    print('1000.')
        
def main():
    a= 10
    r = sequencia(a)
    return(f'{r}')

if __name__ == "__main__":
    main()
