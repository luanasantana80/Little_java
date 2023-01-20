sair=0
codigo=[]
produto=[]
preço=[]
cont=0
tap=0
inv=0
ve=0
while sair==0
    sair=int(input("Para sair digite 1 \n Para continuar 0 \n Sua resposta: "))
    codigo.append(int(input("Digite o codigo: ")))
    produto.append(float(input("Digite o nome do produto: ")))
    preço.append(float(input("Digite o preço: ")))
    tipo=int(input("Dos tipos abaixo: \n 1-Edredom \n 2-Tapetes \n 3-Roupas de Inverno: \n 4-Roupas de Verão "))
    if tipo==1:#Edredom
        cont=cont+1
    if tipo==2:#Tapetes
        tap=tap+1
    if tipo==3:#Inverno
        inv=inv+1
    if tipo==4:#Verão
        ve=ve+1
    










