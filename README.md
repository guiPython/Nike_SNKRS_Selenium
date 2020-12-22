# Python-Selenium-Nike-SNKRS
Bot criado com python e a biblioteca selenium para automatizar compras de tenis em Nike SNKRS BRASIL.

Esta e a primeira implementacao deste tipo de bot feita por mim , recomendo que veja a implementacao com node js , ela e mais estavel.
Ainda estou estudando criar uma segunda implementacao em python utlizando programacao assincrona.

Para utilizar o programa preencha o arquivo Config.txt com os dados pedidos.

      email:
      senha:
      model:
      sizeM: 
      dataL: HH:MM -> Preencha neste formato

Voce pode rodar esta aplicacao console com dois browsers diferentes Google Chrome e Mozilla Firefox , para configurar basta alterar o nike.py.

    
    from webdriver_manager.chrome import ChromeDriverManager
    #from webdriver_manager.firefox import GeckoDriverManager
    
    from selenium.webdriver.chrome.options import Options
    #from selenium.webdriver.firefox.options import Options


Apenas comente as importacoes relativas ao browser que nao quer usar.

Apos estas configuracoes abra o console na pasta do projeto e digite:

    python nike.py
    
*Importante: Este programa serve como aprendizado ou inspiracao para criacao de aplicacoes parecidas*

Meus agradecimentos , facam bom uso :)
