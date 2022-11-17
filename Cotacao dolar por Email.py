#Essa automação pesquisa o valor do dolar hoje e enviar para o usuário via E-mail.

import pyautogui as posicaoMouse #importando a biblioteca pyautogui para automações.


posicaoMouse.sleep(4) #Aguardar 4 Segundos
posicaoMouse.moveTo(x=700, y=25) #Mover o Mouse sobre o icone do Chrome
posicaoMouse.doubleClick(x=35, y=185) #Duplo Clique no Google Chrome


posicaoMouse.moveTo(x=1095, y=145) #Mover mouse para Maximizar o navegador
posicaoMouse.sleep(2) #Aguardar Maximizar o Navegador
posicaoMouse.click(x=1095, y=145) #Clicar para Maximizar
posicaoMouse.typewrite('https://g.co/finance/USD-BRL') #Digita Dolar na barra do navegador
posicaoMouse.sleep(2) #Aguardar Maximizar o Navegador
posicaoMouse.press('enter') #pressiona a tecla Enter
posicaoMouse.sleep(5) #Aguardar Maximizar o Navegador

posicaoMouse.click(x=1095, y=305) #Clicar para Compartilhar
posicaoMouse.sleep(2) #Aguardar 2 Segundos
posicaoMouse.click(x=795, y=490) #Clicar em Copiar Link
posicaoMouse.sleep(2) #Aguardar 2 Segundos
posicaoMouse.click(x=795, y=320) #Clicar em Fechar Tela de Compartilhar
posicaoMouse.sleep(2) #Aguardar 2 Segundos
posicaoMouse.click(x=265, y=15) #Clicar em Fechar Tela de Compartilhar
posicaoMouse.sleep(2) #Aguardarr 2 Segundos

posicaoMouse.typewrite("www.gmail.com") #Digita o site do Gmail na barra de pesquisas do Chrome
posicaoMouse.sleep(2) #Aguardar 2 Segundos
posicaoMouse.press('enter') #Aperta a tecla Enter
posicaoMouse.sleep(5) #Aguardar 5 Segundos
posicaoMouse.click(x=75, y=190) #Clicar em Escrever
posicaoMouse.sleep(2) #Aguardar 2 Segundos

posicaoMouse.typewrite("rickydecamargo14@gmail.com") #Digita o Email do Usuário
posicaoMouse.sleep(2) #Aguardar 2 Segundos
posicaoMouse.press('enter') #Aperta a tecla Enter

posicaoMouse.moveTo(x=850, y=370) #Mover mouse para Assunto
posicaoMouse.click(x=850, y=370) #Clicar no Assunto
posicaoMouse.sleep(2) #Aguardar 2 Segundos
posicaoMouse.typewrite('Cotacao do Dolar Hoje')
posicaoMouse.sleep(2) #Aguardar 2 Segundos
posicaoMouse.press('tab')
posicaoMouse.sleep(2) #Aguardar 2 Segundos

posicaoMouse.moveTo(x=850, y=400) #Mover mouse para Corpo do Email
posicaoMouse.rightClick(x=835, y=380) #Clicou com Botão Direito do Mouse
posicaoMouse.sleep(2) #Aguardar 2 Segundos

posicaoMouse.moveTo(x=870, y=530) #Mover mouse Colar
posicaoMouse.click(x=870, y=530) #Clicou em Colar
posicaoMouse.sleep(2) #Aguardar 2 Segundos

posicaoMouse.moveTo(x=850, y=400) #Mover mouse para cima do link
posicaoMouse.tripleClick(x=835, y=380) #Clicar 3 vezes com o botão esquerdo
posicaoMouse.sleep(2) #Aguardar 2 Segundos

posicaoMouse.moveTo(x=1000, y=695) #Mover mouse para Hyperlink
posicaoMouse.click(x=1000, y=695) #Clicou em Hyperlink
posicaoMouse.sleep(2) #Aguardar 2 Segundos

posicaoMouse.moveTo(x=855, y=695) #Mover mouse para Enviar
posicaoMouse.click(x=855, y=695) #Mover mouse para Enviar

posicaoMouse.sleep(2) #Aguardar 2 Segundos

print('Email enviado para o usuário.')