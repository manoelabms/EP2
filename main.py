print('Comandos possíveis: \n -dica: entra no mercado de dicas \n -desisto: desiste da rodada \n -inventario: exibe sua posição')
print('Você tem {} tentativas'.format(contador_tentativas))
pais_ou_dica = input('Insira seu palpite')

contador_tentativas = 20
lista_tentativas = [] #nessa lista devem ser adicionados os paises de forma crescente pela distancia de haversine

