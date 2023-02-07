print('1- hambúrguer - R$10,00')
print('2- Batata frita -R$5,00 ')
print('3- Refrigerante - R$4,00')
print('4- Sorvete - R$2,00' )
print('5- Hanburguer, Batata Frita, Refrigerante e sorvete - R$50,99')

opcao = int(input('digite o nº da opção desejada:'))
quantidade = int(input('Digite o nº de quantidade desejada:'))
nome = input('Digite o nome do cliente:')

if opcao == 1:
    total = quantidade * 10
    print('Hambúrguer sendo preparado para ', nome ,'\nTempo de espera de 15 minutos','\nTotal:R$' , total)

if opcao == 2:
    total = quantidade * 5  
    print('Batata frita sendo preparado para ', nome ,'\nTempo de espera de 10 minutos','\nTotal:R$' , total)  
if opcao == 3:
    total = quantidade * 4  
    print('Refrigerante sendo preparado para ', nome ,'\nTempo de espera de 2 minutos','\nTotal:R$' , total)      
if opcao == 4:
    total = quantidade * 2  
    print('Sorvete sendo preparado para ', nome ,'\nTempo de espera de 1 minutos','\nTotal:R$' , total) 
if opcao == 5:
    total = quantidade * 50,99  
    print('Sorvete sendo preparado para ', nome ,'\nTempo de espera de 30 minutos','\nTotal:R$' , total)               