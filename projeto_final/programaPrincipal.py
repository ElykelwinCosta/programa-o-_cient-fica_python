import modulos as m



print("Olá, esse sistema tem como objetivo fazer algumas comparações de dados relacionados à acidentes nas BRs da Paraíba entre 26/02 à 30/06.")
print("Como teste iniciais você tem disponível 3 arquivos, relacionados as anos 2018, 2019 e 2020.")
print("Para iniciar é necessário acrescentar ao menos 1 arquivo.\n")

quant = int(input("Quantos arquivos gostaria de comparar? "))
listaDeArquivos = []
listaAnos = []

for k in range(quant):
    nomeArquivo = input("Digite o nome do arquivo .csv: ")
    ano = input("Digite o ano de coleta do arquivo: ")
    listaDeArquivos.append(nomeArquivo)
    listaAnos.append(ano)

sair = False

while sair == False:
    print("\n1 - Gráfico de acidentes por dia com média móvel por ano e intervalo desejado\n",
          "2 - Gráfico de incidencia de acidenstes por dia da semana\n",
          "3 - Gráfico comparativo quantidade de mortos e feridos por ano\n",
          "4 - Gráfico comparatido porcentagem de mortos por ano\n",
          "5 - Tabela comparativa quantidade de mortos e feridos por ano\n",
          "6 - Tabela comparatica quantidade de mortos e feridos por município desejado\n",
          "7 - Adicionar mais arquivos à lista\n",
          "8 - Remover arquivos da lista\n",
          "9 - Sair.\n")
    
    opcao = int(input("\nQual a opção desejada? "))
    if(opcao == 1):
        print("Gráfico de acidentes por dia com média móvel por ano e intervalo desejado")
        m.graficoAcidentesPorDiaMediaMovel(listaDeArquivos, listaAnos)
    elif(opcao == 2):
        m.graficoIncidenciaDeAcidentesDiaSemana(listaDeArquivos, listaAnos)
    elif(opcao == 3):
        m.graficoMortosFeridosAno(listaDeArquivos, listaAnos)
    elif(opcao == 4):
        m.graficoPorcentagemMortosAno(listaDeArquivos, listaAnos)
    elif(opcao == 5):
        m.tabelaMortosFeridosBr(listaDeArquivos, listaAnos)
    elif(opcao == 6):
        m.tabelaMortosFeridosMunicipio(listaDeArquivos, listaAnos)
    elif(opcao == 7):
        m.adicionarArquivos(listaDeArquivos, listaAnos)
    elif(opcao == 8):
        m.removerArquivos(listaDeArquivos, listaAnos)
    elif(opcao == 9):
        print("Até mais!")
        sair = True
    else:
        print("A opção digitada é inválida, tente novamente")


