# mercadoImobiliario
Projeto em Python para coleta, tratamento e análise de dados de imóveis. Desenvolvido na Mentoria DSA 2021, juntamente com Graziele Rodrigues, Carlos Eduardo e Rodrigo Carvalho.

########
O primeiro passo é coletar os dados de imóveis nos diferentes sites.
Os scripts de coleta estão no diretório principal com os seguintes nomes:
- coleta_dados_5andar
- coleta_dados_lar_imoveis
- coleta_dados_vivaReal.py

########
Depois de coletar, é necessário tratar os dados para ajustar o formato, pois os arquivos salvos apresentam campos em formato 'object'.
O script para formatação dos dados também estão separados de acordo com a fonte:
- tratamento_dados_5andar
- tratamento_dados_VivaReal
- tratamento_dados_larImoveis

########
Após este tratamento inicial, juntamos os arquivos e removemos os outliers, utilizando o código constante do arquivo:
- juncao_tratamento_final
