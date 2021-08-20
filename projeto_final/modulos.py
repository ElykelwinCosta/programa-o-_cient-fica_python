import csv
import numpy as np
import matplotlib.pyplot as plt
from prettytable import PrettyTable


def mediaMovel(lista, n): #Recebe uma lista de valores e o intervalo da  média móvel
  novaLista = np.cumsum(lista, dtype=float)
  novaLista[n:] = novaLista[n:] - novaLista[:-n]
  return novaLista[n - 1:] / n


def graficoAcidentesPorDiaMediaMovel(listaDeArquivos, listaAnos):
  data = []; dias = []; axis = []; x = []; y  = []; cont = 0
  opcao = input("De qual ano você deseja ver o gráfico? ")
  n = int(input("Qual o intervalo desejado para a média móvel? "))
  for ano in listaAnos:
    if(ano == opcao):
      with open(listaDeArquivos[cont]) as arquivo:
        dadosAnoX = csv.DictReader(arquivo)
        data = [row["data_inversa"] for row in dadosAnoX]
      for k in data:
        if k not in dias:
          y.append(data.count(k))
          x.append(k)
          dias.append(k)
    cont += 1
  fig, ax = plt.subplots(figsize=(7, 4))
  ax.set_title("Total de acidentes nas BRs da Paraíba por dia entre 26/02 à 30/06\nAno: {}".format(opcao))
  ax.plot(x, y, label=opcao)
  ax.plot(x[:-(n-1)], mediaMovel(y, n), label="Média Móvel")
  ax.set_ylabel("Quantidade de acidentes")
  ax.set_xlabel("Dias no período de 26/02 à 30/06")
  ax.set_xticklabels([])
  plt.legend()
  plt.show()


def graficoIncidenciaDeAcidentesDiaSemana(listaDeArquivos, listaAnos):
  data = []; dias = []; axis = []; final = []; x = []; y  = []
  soma = 0; 
  for nomeArquivo in listaDeArquivos: #Loop de nomes dos arquivos
    with open(nomeArquivo) as arquivo:
      dadosAnoX = csv.DictReader(arquivo)
      data = [row["dia_semana"] for row in dadosAnoX] #Somas dos dados necessários
    for k in data:
      if k not in dias:
        y.append(data.count(k))
        x.append(k)
        dias.append(k)
    final.append([x,y])
    data = []; dias = []; y = []; x = []; soma = []
  fig, ax = plt.subplots(figsize=(7, 4), constrained_layout=True)
  if(len(listaAnos) == 1):
    ax.set_title("Total de acidentes nas BRs da Paraíba por dia da semana entre 26/02 à 30/06\nno período da pandemia do COVID-19\n Ano: {}".format(listaAnos[0]))
  else:
    ax.set_title("Total de acidentes nas BRs da Paraíba por dia da semana entre 26/02 à 30/06\nno período da pandemia do COVID-19\n Período: {} - {}".format(listaAnos[0], listaAnos[-1]))
  ano = 0
  for semana in final:
    plt.scatter(semana[0], semana[1], label=listaAnos[ano])
    ano += 1
  ax.set_ylabel("Quantidade de acidentes")
  ax.set_xlabel("Dias da semana")
  plt.setp(ax.get_xticklabels(), rotation=30, ha="right")
  plt.legend()
  plt.show()


def graficoMortosFeridosAno(listaDeArquivos, listaAnos):
  somaMortos = 0; somaFeridos = 0 #Listas e contadores iniciais
  mortos = []; feridos = []
  
  for nomeArquivo in listaDeArquivos: #Loop de nomes dos arquivos
    with open(nomeArquivo) as arquivo:
      dadosAnoX = csv.DictReader(arquivo)
      for row in dadosAnoX: #Somas dos dados necessários
        somaMortos += int(row["mortos"])
        somaFeridos += int(row["feridos_leves"])
        somaFeridos += int(row["feridos_graves"])
    mortos.append(somaMortos) #Adição dos dados às listas
    feridos.append(somaFeridos)
    somaMortos = 0; somaFeridos = 0 #Zeragem dos contadores
    
  #Gerando o gráfico
  labels = listaAnos
  fig, ax = plt.subplots()
  width = 0.35
  plt.y_top = 700
  barra1 = ax.bar(labels, feridos, width, label="Feridos")
  barra2 = ax.bar(labels, mortos, width, label="Mortos")
  ax.set_ylabel("Vítimas")
  ax.set_ylim(0, 700)
  ax.set_xlabel("Anos")
  if(len(listaAnos) == 0):
    ax.set_title("Mortos e feridos em acidentes nas BRs da Paraíba entre 26/02 à 30/06\nno período da pandemia do COVID-19\n Período: {}".format(listaAnos[0]))
  else:
    ax.set_title("Mortos e feridos em acidentes nas BRs da Paraíba entre 26/02 à 30/06\nno período da pandemia do COVID-19\n Período: {} - {}".format(listaAnos[0], listaAnos[-1]))
  ax.legend()
  for b1, b2 in zip(barra1, barra2):
    height = b1.get_height()
    height2 = b2.get_height()
    ax.annotate('{}'.format(height), xy=(b1.get_x() + b1.get_width() / 2, height), xytext=(0, 3), textcoords="offset points", ha='center', va='bottom')
    ax.annotate('{}'.format(height2), xy=(b2.get_x() + b2.get_width() / 2, height2), xytext=(0, 3), textcoords="offset points", ha='center', va='bottom')
  plt.show()


def graficoPorcentagemMortosAno(listaDeArquivos, listaAnos):
  somaMortos = 0; cont = 0#Listas e contadores iniciais
  mortos = []; acidentes = []
  
  for nomeArquivo in listaDeArquivos: #Loop de nomes dos arquivos
    with open(nomeArquivo) as arquivo:
      dadosAnoX = csv.DictReader(arquivo)
      for row in dadosAnoX: #Somas dos dados necessários
        somaMortos += int(row["mortos"])
        cont += 1
      mortos.append(float("{:.2f}".format((somaMortos/cont)*100)))
      acidentes.append(cont)
    somaMortos = 0; cont = 0

  #Gerando o gráfico
  labels = listaAnos
  fig, ax = plt.subplots()
  width = 0.35
  plt.y_top = 700
  barra1 = ax.bar(labels, acidentes, width, label="Acidentes")
  barra2 = ax.bar(labels, mortos, width, label="Mortos %")
  ax.set_ylabel("Vítimas")
  ax.set_ylim(0, 700)
  ax.set_xlabel("Anos")
  if(len(listaAnos) == 0):
    ax.set_title("Porcentagem de mortos em acidentes nas BRs da Paraíba entre 26/02 à 30/06\n período da pandemia do COVID-19\n Ano: {}".format(listaAnos[0]))
  else:
    ax.set_title("Porcentagem de mortos em acidentes nas BRs da Paraíba entre 26/02 à 30/06\n período da pandemia do COVID-19\n Anos: {} - {}".format(listaAnos[0], listaAnos[-1]))
  ax.legend()
  for b1, b2 in zip(barra1, barra2):
    height = b1.get_height()
    height2 = b2.get_height()
    ax.annotate('{}'.format(height), xy=(b1.get_x() + b1.get_width() / 2, height), xytext=(0, 3), textcoords="offset points", ha='center', va='bottom')
    ax.annotate('{}%'.format(height2), xy=(b2.get_x() + b2.get_width() / 2, height2), xytext=(0, 3), textcoords="offset points", ha='center', va='bottom')
  plt.show()


def tabelaMortosFeridosBr(listaDeArquivos, listaAnos):
  somaMortos = 0; somaFeridosLeves = 0; somaFeridosGraves = 0 #Listas e contadores iniciais
  listaDados = []
  brs = []
  listaMortos = []; listaFeridosLeves = []; listaFeridosGraves = []
  lista = []
  for nomeArquivo in listaDeArquivos: #Loop de nomes dos arquivos
    with open(nomeArquivo) as arquivo:
      dadosAnoX = csv.DictReader(arquivo)
      for row in dadosAnoX: #Somas dos dados necessários
        listaDados.append([row["br"], row["mortos"], row["feridos_leves"], row["feridos_graves"]])
      listaDados.sort()
      for dado in listaDados:
        if(dado[0] in brs):
          somaMortos += int(dado[1])
          somaFeridosLeves += int(dado[2])
          somaFeridosGraves += int(dado[3])
        else:
          listaMortos.append(somaMortos)
          listaFeridosLeves.append(somaFeridosLeves)
          listaFeridosGraves.append(somaFeridosGraves)
          brs.append(dado[0])
          somaMortos = int(dado[1])
          somaFeridosLeves = int(dado[2])
          somaFeridosGraves = int(dado[3])
      listaMortos.append(somaMortos)
      listaFeridosLeves.append(somaFeridosLeves)
      listaFeridosGraves.append(somaFeridosGraves)
      lista.append([brs, listaMortos[1:], listaFeridosLeves[1:], listaFeridosGraves[1:]])
      brs = []; listaDados = []; listaMortos = []; listaFeridosLeves = []; listaFeridosGraves = [] 
      somaMortos = 0; somaFeridosLeves = 0; somaFeridosGraves = 0
  ano = 0
  soma = 0
  x = "_"
  for k in lista:
    print("Ano de referência = ", listaAnos[ano])
    # Cria a tabela
    x = PrettyTable(["BR", "MORTOS", "FERIDOS LEVES", "FERIDOS GRAVES"])
    # Alinha as colunas
    x.align["BR"] = "c"
    x.align["MORTOS"] = "c"
    x.align["FERIDOS LEVES"] = "c"
    x.align["FERIDOS GRAVES"] = "c"
    for br, mortos, leves, graves in zip(k[0], k[1], k[2], k[3]):
      x.padding_width = 1
      x.add_row([br, mortos, leves, graves])
    ano += 1
    print(x)


def tabelaMortosFeridosMunicipio(listaDeArquivos, listaAnos):
  ano = 0; somaMortos = 0; somaFeridosLeves = 0; somaFeridosGraves = 0
  municipios = ['ALCANTIL', 'ALHANDRA', 'APARECIDA', 'BARRA DE SANTA ROSA', 'BARRA DE SANTANA',
                       'BAYEUX', 'BOA VISTA', 'BOM JESUS', 'CAAPORA', 'CABEDELO', 'CACHOEIRA DOS INDIOS',
                       'CACHOEIRA DOS ÍNDIOS', 'CAJAZEIRAS', 'CALDAS BRANDAO', 'CALDAS BRANDÃO', 'CAMPINA GRANDE',
                       'CAPIM', 'CATINGUEIRA', 'CONDADO', 'CONDE', 'CRUZ DO ESPIRITO SANTO', 'CRUZ DO ESPÍRITO SANTO',
                       'CUITE', 'ESPERANÇA', 'GURINHEM', 'GURINHÉM', 'INGÁ', 'ITAPORANGA', 'JOÃO PESSOA', 'JUAZEIRINHO',
                        'JUNCO DO SERIDO', 'LAGOA SECA', 'MALTA', 'MAMANGUAPE', 'MARIZOPOLIS', 'MARIZÓPOLIS', 'MASSARANDUBA',
                        'MATARACA', 'MOGEIRO', 'MONTEIRO', 'NOVA FLORESTA', 'OLHO DAGUA', 'PATOS', 'PAULISTA', 'PEDRAS DE FOGO',
                        'PIANCO', 'POCINHOS', 'POMBAL', 'QUEIMADAS', 'QUIXABA', 'REMIGIO', 'REMÍGIO', 'RIACHÃO DO BACAMARTE',
                       'RIACHÃO DO POCO', 'RIO TINTO', 'SANTA LUZIA', 'SANTA RITA', 'SANTA TERESINHA', 'SERRA BRANCA', 'SOBRADO',
                       'SOLEDADE', 'SOUSA', 'SUMÉ', 'SÃO BENTINHO', 'SÃO JOÃO DO CARIRI', 'SÃO JOÃO DO RIO DO PEIXE', 'SÃO MAMEDE',
                       'SÃO MIGUEL DE TAIPU', 'SÃO SEBASTIAO DE LAGOA DE  ROCA', 'SÃO SEBASTIÃO DE LAGOA DE  ROCA', 'UIRAÚNA']

  municipio = input("\nQual município deseja pesquisar? " ).upper()
  # Cria a tabela
  x = PrettyTable(["ANO", "MORTOS", "FERIDOS LEVES", "FERIDOS GRAVES"])    
  # Alinha as colunas
  x.align["ANO"] = "c"
  x.align["MORTOS"] = "c"
  x.align["FERIDOS LEVES"] = "c"
  x.align["FERIDOS GRAVES"] = "c"
  for nomeArquivo in listaDeArquivos: #Loop de nomes dos arquivos
    with open(nomeArquivo) as arquivo:
      dadosAnoX = csv.DictReader(arquivo)
      for row in dadosAnoX: #Somas dos dados necessários
        if(municipio == row["município"]):
          somaMortos += int(row["mortos"])
          somaFeridosLeves += int(row["feridos_leves"])
          somaFeridosGraves += int(row["feridos_graves"])
      else:
        print("\nMunicípio não encontrado, reveja a lista, a ortografia e tente novamente.\n")
        break
    x.padding_width = 1
    x.add_row([listaAnos[ano], somaMortos, somaFeridosLeves, somaFeridosGraves])
    ano += 1
  print(x)


def adicionarArquivos(listaDeArquivos, listaAnos):
  print("Arquivos já adicionados: {}".format(listaDeArquivos))
  quant = int(input("Quantos arquivos gostaria de comparar? "))
  for k in range(quant):
    nomeArquivo = input("Digite o nome do arquivo .csv: ")
    ano = input("Digite o ano de coleta do arquivo: ")
    listaDeArquivos.append(nomeArquivo)
    listaAnos.append(ano)
  print("Lista atual: {}".format(listaDeArquivos))


def removerArquivos(listaDeArquivos, listaAnos):
  print("Arquivos já adicionados: {}".format(listaDeArquivos))
  quant = int(input("Quantos arquivos gostaria de remover? "))
  for k in range(quant):
    nomeArquivo = input("Digite o nome do arquivo que gostaria de remover .csv: ")
    ano = input("Digite o ano de coleta do arquivo que gostaria de remover: ")
    listaDeArquivos.remove(nomeArquivo)
    listaAnos.remove(ano)
  print("Lista atual: {}".format(listaDeArquivos))
