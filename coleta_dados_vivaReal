# Imports
import os # operation system
import re # regular expression
import csv # manipula arquivos csv
import pickle # cria cache de acesso a uma pag web
import requests # requisição a pag
from bs4 import BeautifulSoup # para fazer o parser da pag html
from selenium import webdriver # simular clicks
from time import sleep

# Coleta links dos imóveis de cada página
def coleta_links():

    # abre navegador
    navegador = webdriver.Chrome()
    
    # 36 imoveis por pagina
    pagConsulta = 2 # Total de páginas para consultar
    # lista vazia para receber as linhas
    links_linhas = []
    for i in range(1, pagConsulta+1):

        site_page = ''
        if i==1:
            # Rio
            site_page = 'https://www.vivareal.com.br/venda/rj/rio-de-janeiro/apartamento_residencial/#tipos=apartamento_residencial,casa_residencial,condominio_residencial,cobertura_residencial,flat_residencial,kitnet_residencial,sobrado_residencial'
            # BH
            # site_page = 'https://www.vivareal.com.br/venda/minas-gerais/belo-horizonte/apartamento_residencial/#tipos=apartamento_residencial,casa_residencial,condominio_residencial,cobertura_residencial,flat_residencial,kitnet_residencial,sobrado_residencial'
            # SP
            # site_page = 'https://www.vivareal.com.br/venda/sp/sao-paulo/apartamento_residencial/#tipos=apartamento_residencial,casa_residencial,condominio_residencial,cobertura_residencial,flat_residencial,kitnet_residencial,sobrado_residencial'

            # navega na URL
            navegador.get(site_page)
        else:
            # rolagem para o final da página
            #sleep(2) # espera 2 segundos
            navegador.execute_script("window.scrollTo(0, 10000)")
            # clica no botão proxima página
            navegador.find_element_by_xpath('//*[@id="js-site-main"]/div[2]/div[1]/section/div[2]/div[2]/div/ul/li[9]/a').click()
            sleep(3) # espera 3 segundos

        # Faz o parser do texto da página
        soup = BeautifulSoup(navegador.page_source, 'html.parser')

        # Extraindo informações de repetidas divisões (tag div)
        blocks = []
        blocks = soup.find_all('article', class_='property-card__container js-property-card')

        # links_linhas.append(i)

        # Loop pelos blocos de dados
        for cb in blocks:
            # pega os links
            links_linhas.append('https://www.vivareal.com.br' + cb.find('a').get("href"))

    navegador.close()
    return links_linhas


# Função para extrair os dados
def extrai_dados(link_imovel):

    # abre navegador
    navegador = webdriver.Chrome()
    navegador.get(link_imovel)

    # Faz o parser do texto da página
    soup = BeautifulSoup(navegador.page_source, 'html.parser')

    # Titulo
    if soup.find('h3', class_='description__title js-description-title').text.replace('\n', ''):
        titulo = soup.find('h3', class_='description__title js-description-title').text.replace('\n', '')
    else:
        titulo = 'nao identificado'

    # Valor
    if soup.find('h3', class_='price__price-info js-price-sale').text.replace('\n', '').replace(' ', ''):
        valor = soup.find('h3', class_='price__price-info js-price-sale').text.replace('\n', '').replace(' ', '')
    else:
        valor = 'nao identificado'
    
    # Condominio
    if soup.find('span', class_='price__list-value condominium js-condominium'):
        condominio = soup.find('span', class_='price__list-value condominium js-condominium').text.replace('\n', '').replace(' ', '')
    else:
        condominio = '-'

    # IPTU
    if soup.find('span', class_='price__list-value iptu js-iptu'):
        iptu = soup.find('span', class_='price__list-value iptu js-iptu').text.replace('\n', '').replace(' ', '')
    else:
        iptu = '-'
    
    # Área
    if soup.find('li', class_='features__item features__item--area js-area').text.replace('\n', '').replace(' ', ''):
        area = soup.find('li', class_='features__item features__item--area js-area').text.replace('\n', '').replace(' ', '')
    else:
        area = 'nao identificado'

    # Endereço
    if soup.find('p', class_='title__address js-address').text:
        endereco = soup.find('p', class_='title__address js-address').text
    else:
        endereco = 'nao identificado'

    # Regiao e Bairro
    regiao = ""
    bairro = ""
    cabecalho = soup.find_all('a', class_='breadcrumb__item-name js-link')
    if cabecalho[0].text.replace('Imóveis','').replace(' ','') == "Novos":
        if len(cabecalho)>=3:
            regiao = cabecalho[2].text
            if len(cabecalho)>=4:
                bairro = cabecalho[3].text
    else:
        if len(cabecalho)>=4:
            regiao = cabecalho[3].text
            if len(cabecalho)>=5:    
                bairro = cabecalho[4].text

    # Quartos
    if soup.find('li', class_='features__item features__item--bedroom js-bedrooms').text.replace(' quartos','').replace(' quarto','').replace(' ',''):
        quartos = soup.find('li', class_='features__item features__item--bedroom js-bedrooms').text.replace(' quartos','').replace(' quarto','').replace(' ','')
    else:
        quartos = 'nao identificado'
        
    # Suite
    if soup.find('small', class_='features__extra-info'):
        suites = soup.find('small', class_='features__extra-info').text.replace(' suítes','').replace(' suíte','').replace(' ','')
    else:
        suites = "--"
    
    # Banheiros
    if soup.find('li', class_='features__item features__item--bathroom js-bathrooms').text.replace('os','o').split(' banheiro')[0]:
        banheiros = soup.find('li', class_='features__item features__item--bathroom js-bathrooms').text.replace('os','o').split(' banheiro')[0]
    else:
        banheiros = 'nao identificado'
    
    # Vagas
    if soup.find('li', class_='features__item features__item--parking js-parking').text.replace(' vagas','').replace(' vaga','').replace(' ',''):
        vagas = soup.find('li', class_='features__item features__item--parking js-parking').text.replace(' vagas','').replace(' vaga','').replace(' ','')
    else:
        vagas = 'nao identificado'

    # Elevador
    if soup.find('div', class_='amenities__lightbox js-amenities-modal'):
        adicionais = soup.find('div', class_='amenities__lightbox js-amenities-modal').text.find('Elevador')
        if adicionais == -1:
            elevador = '--'
        else:
            elevador = 'sim'
    else:
        elevador = '--'
    
    # Metro e Trem
    if soup.find('h3', class_='poi-nearby__title'):
        metro_trem = 'sim'
    else:
        metro_trem = '--'

    # Geramos um dicinário para cada linha extraída
    linha = dict(link=link_imovel, titulo=titulo, valor=valor, condominio=condominio, iptu=iptu, 
    area=area, endereco=endereco, bairro=bairro, regiao=regiao, quartos=quartos, suites=suites, 
    banheiros=banheiros, vagas=vagas, elevador=elevador, metro_trem=metro_trem)

    navegador.close()
    return linha

# Execução principal do programa
if __name__ == "__main__":

    # Coleta os links dos imoveis das páginas
    links = coleta_links()
    print("QTDE= ", len(links))

    # Arquivo para guardar os dados copiados em cache
    filename = 'dados_copiados_v1.pickle'

    # Grava o resultado em csv
    with open("dados_copiados_v1.csv", "w") as f:

        imoveisLista = []
        contador = 1
        for imovel in links:

            imoveisLista.append(extrai_dados(imovel))
            sleep(1)

            if contador == 1:
                writer = csv.DictWriter(f, fieldnames = imoveisLista[0].keys())
                writer.writeheader()
            elif contador%10 == 0:
                writer.writerows(imoveisLista)
                imoveisLista = []

            contador = contador + 1
        
        writer.writerows(imoveisLista)
