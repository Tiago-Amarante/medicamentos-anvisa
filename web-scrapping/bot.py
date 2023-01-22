import tools
from time import sleep

bot = tools.tools('https://dados.gov.br/dados/conjuntos-dados/venda-de-medicamentos-controlados-e-antimicrobianos---medicamentos-manipulados')

bot.SiteInitiate(r'D:\Base_de_dados_anvisa')
sleep(2)

bot.OpenSite()
sleep(6)

bot.ClickButton(r'/html/body/div/section/div/div[3]/div[2]/div[3]/div[2]/header/button')
sleep(2)

for i in range(2,97):

    bot.ClickButton(r'/html/body/div/section/div/div[3]/div[2]/div[3]/div[2]/div/div[{}]/div[2]/div[2]/div/button[1]'.format(i))
    print('Fazendo download do arquivo: {}'.format(i))
    sleep(30)
