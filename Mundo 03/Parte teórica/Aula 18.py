teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste[:])  # Usar "[:]" para copiar lista
teste[0] = 'Maria'
teste[1] = 20
galera.append(teste)
print(galera)
