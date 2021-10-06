# mercadoImobiliario
Projeto em Python para coleta, tratamento e análise de dados de imóveis. Desenvolvido na Mentoria DSA 2021, pela equipe composta por Graziele Rodrigues, Carlos Eduardo,  Rodrigo Carvalho e Bruna Nicolato.

1. O primeiro passo é coletar os dados de imóveis nos diferentes sites. Os scripts de coleta estão no diretório principal com os seguintes nomes:
- coleta_dados_5andar
- coleta_dados_lar_imoveis
- coleta_dados_vivaReal.py

2. Depois de coletar, é necessário tratar os dados para ajustar o formato, pois os arquivos salvos apresentam campos em formato 'object'.
O script para formatação dos dados também estão separados de acordo com a fonte:
- tratamento_dados_5andar
- tratamento_dados_VivaReal
- tratamento_dados_larImoveis

3. Após este tratamento inicial, juntamos os arquivos e removemos os outliers, utilizando o código constante do arquivo:
- juncao_tratamento_final

4. Opcionalmente, pode-se plotar os dados dos imóveis em mapas, de acordo com os scripts:
- plotar_mapa_limites_coordenadasImoveis (caso queira plotar com as coordenadas dos imóveis)
- plotar_mapa_coordenadasRegioes (caso considere interessante plotar com os dados consolidados por região administrativa dos municípios)

5. A construção e avaliação do modelo constam do notebook:
- modelo.ipynb

5.1 O arquivo tratado e utilizado para a construção do modelo está no repositório:
- TodosImoveis_tratado_v5.csv

5.2 Também consta no repositório o arquivo tratado sem a padronização de bairros/regiões, que somam uma quantidade maior de registros:
- TodosImoveis_tratado_v4.csv

#######ATENÇÃO#######
-
6. Os arquivos da aplicação encontram-se no repositório:
- https://github.com/bruninhanic/vendacasa

7. A aplicação pode ser acessada entrando na pasta do projeto, pelo prompt de comando digite:
streamlit run Stream.py. 
ou pelo site: https://share.streamlit.io/carloseduardobh/vendacasa/Stream.py


