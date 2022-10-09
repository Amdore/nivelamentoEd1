pilha = []

listaDePaginas = ['Pagina 1','Pagina 2','Pagina 3']

inteiro = 0

while True:
    temp = input()
    if(temp == 'voltar'):
        inteiro = inteiro - 1
        pilha.pop()
    elif(temp == 'avançar'):
        pilha.append(listaDePaginas[inteiro])
        inteiro = inteiro + 1
    elif(temp == 'printar'):
        print(pilha)
    else:
        break
Footer
© 2022 GitHub, Inc.
Footer navigation
Terms
