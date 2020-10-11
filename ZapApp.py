from selenium import webdriver
import time

class ZapApp:
    def __init__(self):
        self.message = "Ola, essa mensagem eh um teste"
        self.arquivo = open("encerrados.txt")
        self.numeros = ["11111111111", "00000000000"]                          #self.arquivo.readlines()
        options = webdriver.ChromeOptions()
        options.add_argument("lang=pt-br")
        self.driver = webdriver.Chrome(executable_path=r"./chromedriver.exe")


    def printList(self):
        for grupo in self.numeros:
            print(grupo)
    
    #def EnviarMsg(self):

    def sendMessage(self):
        
        self.driver.get("https://web.whatsapp.com/send?phone=5541995670617")
        time.sleep(10)
        
        for numero in self.numeros:
            url = "https://api.whatsapp.com/send?phone=" + numero
            self.driver.get(url)
            botao = self.driver.find_element_by_id("action-button")# Search for the reference
            time.sleep(2)
            botao.click()

            botao_web = self.driver.find_element_by_xpath("//a[@class='_36or']")
            time.sleep(2)
            botao_web.click()
            
            time.sleep(20)
            
            message_bar = self.driver.find_element_by_class_name("_2vJ01")
            time.sleep(2)
            message_bar.click()
            message_bar.send_keys(self.message)

            send_button = self.driver.find_element_by_xpath("//span[@data-icon='send']")
            time.sleep(3)
            send_button.click()
            time.sleep(3)



za = ZapApp()

za.sendMessage()

#za.printList()

#<span class="_1X4JR">+55 41 9567-0617</span>
#class="_3FRCZ copyable-text selectable-text"
#<span data-testid="send" data-icon="send" class="">

#<a class="_36or _2y_c _2z0c _2z07" href="https://web.whatsapp.com/send?phone=2" title="Compartilhe no WhatsApp" id="action-button">Iniciar conversa</a>
