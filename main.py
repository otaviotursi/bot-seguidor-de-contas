import ctypes
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.chrome.options import Options 
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup, NavigableString, Tag
import time
import random
import configparser

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(500, 420)
        MainWindow.setMinimumSize(QtCore.QSize(500, 420))
        MainWindow.setMaximumSize(QtCore.QSize(500, 420))
        MainWindow.setMouseTracking(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 501, 421))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tabWidget.setFont(font)
        self.tabWidget.setMouseTracking(False)
        self.tabWidget.setObjectName("tabWidget")
        self.INFOS = QtWidgets.QWidget()
        self.INFOS.setObjectName("INFOS")
        self.inputLoginEmail = QtWidgets.QLineEdit(self.INFOS)
        self.inputLoginEmail.setGeometry(QtCore.QRect(80, 20, 171, 22))
        self.inputLoginEmail.setObjectName("inputLoginEmail")
        self.inputLoginSenha = QtWidgets.QLineEdit(self.INFOS)
        self.inputLoginSenha.setGeometry(QtCore.QRect(80, 50, 171, 22))
        self.inputLoginSenha.setObjectName("inputLoginSenha")
        self.labelEmail = QtWidgets.QLabel(self.INFOS)
        self.labelEmail.setGeometry(QtCore.QRect(10, 20, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelEmail.setFont(font)
        self.labelEmail.setObjectName("labelEmail")
        self.labelSenha = QtWidgets.QLabel(self.INFOS)
        self.labelSenha.setGeometry(QtCore.QRect(10, 50, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelSenha.setFont(font)
        self.labelSenha.setObjectName("labelSenha")
        self.groupBox = QtWidgets.QGroupBox(self.INFOS)
        self.groupBox.setGeometry(QtCore.QRect(250, 80, 241, 111))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.inputIntervaloMinimo = QtWidgets.QLineEdit(self.groupBox)
        self.inputIntervaloMinimo.setGeometry(QtCore.QRect(80, 30, 113, 22))
        self.inputIntervaloMinimo.setObjectName("inputIntervaloMinimo")
        self.inputIntervaloMaximo = QtWidgets.QLineEdit(self.groupBox)
        self.inputIntervaloMaximo.setGeometry(QtCore.QRect(80, 60, 113, 22))
        self.inputIntervaloMaximo.setObjectName("inputIntervaloMaximo")
        self.labelIntervaloMinimo = QtWidgets.QLabel(self.groupBox)
        self.labelIntervaloMinimo.setGeometry(QtCore.QRect(10, 30, 71, 16))
        self.labelIntervaloMinimo.setObjectName("labelIntervaloMinimo")
        self.labelIntervaloMaximo = QtWidgets.QLabel(self.groupBox)
        self.labelIntervaloMaximo.setGeometry(QtCore.QRect(10, 60, 71, 16))
        self.labelIntervaloMaximo.setObjectName("labelIntervaloMaximo")
        self.groupBox_2 = QtWidgets.QGroupBox(self.INFOS)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 200, 241, 111))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.inputMinutosStories = QtWidgets.QLineEdit(self.groupBox_2)
        self.inputMinutosStories.setGeometry(QtCore.QRect(80, 30, 113, 22))
        self.inputMinutosStories.setObjectName("inputMinutosStories")
        self.labelTempoStories = QtWidgets.QLabel(self.groupBox_2)
        self.labelTempoStories.setGeometry(QtCore.QRect(10, 30, 71, 21))
        self.labelTempoStories.setObjectName("labelTempoStories")
        self.checkBoxAssistirStories = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBoxAssistirStories.setGeometry(QtCore.QRect(10, 70, 211, 20))
        self.checkBoxAssistirStories.setObjectName("checkBoxAssistirStories")
        self.labelQntSeguimos = QtWidgets.QLabel(self.INFOS)
        self.labelQntSeguimos.setGeometry(QtCore.QRect(10, 330, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelQntSeguimos.setFont(font)
        self.labelQntSeguimos.setObjectName("labelQntSeguimos")
        self.btnIniciar = QtWidgets.QPushButton(self.INFOS)
        self.btnIniciar.setGeometry(QtCore.QRect(380, 330, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btnIniciar.setFont(font)
        self.btnIniciar.setObjectName("btnIniciar")
        self.groupBox_3 = QtWidgets.QGroupBox(self.INFOS)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 80, 241, 111))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.inputTarefaMinimo = QtWidgets.QLineEdit(self.groupBox_3)
        self.inputTarefaMinimo.setGeometry(QtCore.QRect(80, 30, 113, 22))
        self.inputTarefaMinimo.setObjectName("inputTarefaMinimo")
        self.inputTarefaMaximo = QtWidgets.QLineEdit(self.groupBox_3)
        self.inputTarefaMaximo.setGeometry(QtCore.QRect(80, 60, 113, 22))
        self.inputTarefaMaximo.setObjectName("inputTarefaMaximo")
        self.labelQntTarefasMinimo = QtWidgets.QLabel(self.groupBox_3)
        self.labelQntTarefasMinimo.setGeometry(QtCore.QRect(10, 30, 71, 16))
        self.labelQntTarefasMinimo.setObjectName("labelQntTarefasMinimo")
        self.labelQntTarefasMaximo = QtWidgets.QLabel(self.groupBox_3)
        self.labelQntTarefasMaximo.setGeometry(QtCore.QRect(10, 60, 71, 16))
        self.labelQntTarefasMaximo.setObjectName("labelQntTarefasMaximo")
        self.groupBox_4 = QtWidgets.QGroupBox(self.INFOS)
        self.groupBox_4.setGeometry(QtCore.QRect(250, 200, 241, 111))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setObjectName("groupBox_4")
        self.inputComboTextPerfisAlvos = QtWidgets.QPlainTextEdit(self.groupBox_4)
        self.inputComboTextPerfisAlvos.setGeometry(QtCore.QRect(10, 30, 221, 71))
        self.inputComboTextPerfisAlvos.setObjectName("inputComboTextPerfisAlvos")
        self.tabWidget.addTab(self.INFOS, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.database()
        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
    def database(self):
        self.config = configparser.ConfigParser()
        self.config.read('config.ini')
        self.loginInsta = self.config['configs']['loginInsta']
        self.senhaInsta = self.config['configs']['senhainsta']
        self.IntervaloMin = self.config['configs']['intervalomin']
        self.IntervaloMax = self.config['configs']['intervalomax']
        self.tempoStories = self.config['configs']['tempostories']
        self.tarefaMin = self.config['configs']['tarefamin']
        self.tarefaMax = self.config['configs']['tarefamax']
        self.boxCaixaPerfis = self.config['configs']['boxcaixaperfis']
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "TauBot - SEGUIR"))
        self.inputLoginEmail.setText(_translate("MainWindow", self.loginInsta))
        self.inputLoginSenha.setText(_translate("MainWindow", self.senhaInsta))
        self.labelEmail.setText(_translate("MainWindow", "Usuário:"))
        self.labelSenha.setText(_translate("MainWindow", "Senha:"))
        self.groupBox.setTitle(_translate("MainWindow", "Intervalo de ações (segundos)"))
        self.inputIntervaloMinimo.setText(_translate("MainWindow", self.IntervaloMin))
        self.inputIntervaloMaximo.setText(_translate("MainWindow", self.IntervaloMax))
        self.labelIntervaloMinimo.setText(_translate("MainWindow", "Minimo:"))
        self.labelIntervaloMaximo.setText(_translate("MainWindow", "Maximo:"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Assistir Stories (minutos)"))
        self.inputMinutosStories.setText(_translate("MainWindow", self.tempoStories))
        self.labelTempoStories.setText(_translate("MainWindow", "Tempo:"))
        self.checkBoxAssistirStories.setText(_translate("MainWindow", "Assistir Stories"))
        self.labelQntSeguimos.setText(_translate("MainWindow", "Seguimos: "))
        self.btnIniciar.setText(_translate("MainWindow", "INICIAR"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Tarefas"))
        self.inputTarefaMinimo.setText(_translate("MainWindow", self.tarefaMin))
        self.inputTarefaMaximo.setText(_translate("MainWindow", self.tarefaMax))
        self.labelQntTarefasMinimo.setText(_translate("MainWindow", "Minimo:"))
        self.labelQntTarefasMaximo.setText(_translate("MainWindow", "Maximo:"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Perfis para seguir"))
        self.inputComboTextPerfisAlvos.setPlainText(_translate("MainWindow", self.boxCaixaPerfis))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.INFOS), _translate("MainWindow", "INFOS"))

        self.btnIniciar.clicked.connect(self.iniciar)
        
    def iniciar(self):
        from threading import Event, Thread
        import threading
        self.t3 = Thread(target=self.tarefas, args=(), daemon=True)
        self.t3.start()
        
    def tarefas(self):
        self.config.set('configs', 'loginInsta', self.inputLoginEmail.text())
        self.config.set('configs', 'senhainsta', self.inputLoginSenha.text())
        self.config.set('configs', 'intervalomin', self.inputIntervaloMinimo.text())
        self.config.set('configs', 'intervalomax', self.inputIntervaloMaximo.text())
        self.config.set('configs', 'tempostories', self.inputMinutosStories.text())
        self.config.set('configs', 'tarefamin', self.inputTarefaMinimo.text())
        self.config.set('configs', 'tarefamax', self.inputTarefaMaximo.text())
        self.config.set('configs', 'boxcaixaperfis', self.inputComboTextPerfisAlvos.toPlainText())
        with open('config.ini', 'w') as configfile:
            self.config.write(configfile)
            
        self.sinalContaBloqueada = False
        self.openDriver()
        driver = self.driver
        self.openInsta()
        try:
            people = self.inputComboTextPerfisAlvos.toPlainText().split(';')
        except Exception as e:
            print(e)
        #verifica se tem bloqueio, se não tiver, começa a realizar as tarefas
        if not self.sinalContaBloqueada:
            for person in people:
                self.assistirStories()
                driver.get(f'https://www.instagram.com/{person}/')
                self.realizarTarefas()
        else:
            print('Conta bloqueada')
            
    def openDriver(self):
        
        options = Options()
        options.add_argument('--disable-gpu')
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        options.add_argument("--mute-audio")
        options.add_argument('--no-sandbox')
        options.add_argument('disable-infobars')
        options.add_argument('--disable-popup-blocking')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument("--incognito")
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        
    def openInsta(self):
        driver = self.driver
        driver.get('https://www.instagram.com/')
        #Digita o login do perfil no instagram
        try:
            WebDriverWait(driver,10).until(ec.presence_of_element_located((By.XPATH, "//input[@name='username']"))).send_keys(self.inputLoginEmail.text())
        except Exception:
            pass
        #Digita a senha do perfil no instagram
        try:
            WebDriverWait(driver,10).until(ec.presence_of_element_located((By.XPATH, "//input[@name='password']"))).send_keys(self.inputLoginSenha.text() + Keys.ENTER)
        except Exception:
            pass
        time.sleep(3)
        #vai verificar os bloqueios
        self.validandoConta()
        #verifica se tem bloqueio, se não tiver, assiste stories

    def assistirStories(self):
        driver = self.driver
        if self.checkBoxAssistirStories.isChecked():
            print('Vamos assistir stories!')
            driver.get('https://www.instagram.com/')
            try:
                WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.CSS_SELECTOR, 'body > div.RnEpo.Yx5HN > div > div > div > div.mt3GC > button.aOOlW.HoLwm'))).click()
            except Exception:
                pass
            # abre o storie
            time.sleep(random.randint(2,3))
            WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.CSS_SELECTOR, '#react-root > section > main > section > div > div.zGtbP.VideM > div > div > div > div > ul > li:nth-child(6)'))).click()
            if self.inputMinutosStories.text().isdigit():
                time.sleep(int(self.inputMinutosStories.text())*60)
            else:
                time.sleep(2)
            
    def realizarTarefas(self):
        driver  = self.driver
        sinalPrecisaScrool = False
        #abre a area de seguidores do perfil selecionado
        WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.CSS_SELECTOR, '.Y8-fY:nth-child(2) > .-nal3'))).click()
        #  sorteia a quantidade de tarefas a serem feitas
        qntSorteada = random.randint(int(self.inputTarefaMinimo.text()), int(self.inputTarefaMaximo.text()))
        contadorDeTarefas = 0
        while contadorDeTarefas <= qntSorteada:
            contadorDeTarefas += 1
            
            self.labelQntSeguimos.setText('Seguimos: ' + str(contadorDeTarefas-1))
            try:
                #vai descer a pagina se não encontrar ninguem para seguir
                if sinalPrecisaScrool:
                    fBody  = driver.find_element_by_xpath("//div[@class='isgrP']")
                    scroll = 0
                    while scroll < 5: # scroll 5 times
                        driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', fBody)
                        time.sleep(2)
                        scroll += 1
            except Exception:
                pass
            if self.sinalContaBloqueada:
                print('Conta bloqueada')
                break
            try:
                #faz a ação de seguir as pessoas
                WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, '//button[@class="sqdOP  L3NKy   y3zKF     "]'))).click()
                sinalPrecisaScrool = False
            except Exception:
                sinalPrecisaScrool = True
                if contadorDeTarefas > 0:
                    contadorDeTarefas -= 1
                    
            #sorteia o tempo de pause entre as ações
            tempoSorteado = random.randint(int(self.inputIntervaloMinimo.text()), int(self.inputIntervaloMaximo.text()))
            time.sleep(tempoSorteado-5)
            #verifica se tem bloqueio
            self.validandoConta()
            
    def validandoConta(self):
        driver = self.driver
        emailErrado = []
        driver.implicitly_wait(1)
        try:
            driver.find_element_by_css_selector('body')
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            for _, heading in enumerate(soup.find_all(["p"])):
                
                emailErrado.append(heading.text.strip())
                if emailErrado[0] == 'Sua senha está incorreta. Confira-a.':
                    print(f'Sua senha está incorreta. Confira-a. Conta: {self.inputLoginEmail.text()}')
                    self.sinalContaBloqueada = True
                    break

                else:   
                    driver.find_element_by_css_selector('niowefnvidocvio')
        except Exception:
            pass
        listVerificao7dias = []
        try:
            # page = requests.get("https://sites.google.com/view/taubot/atualizar")
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            for _, heading in enumerate(soup.find_all(["div"])):
                
                listVerificao7dias.append(heading.text.strip('.'))
                if listVerificao7dias == 'Sua conta foi temporariamente impedida de realizar essa ação':
                    # print(listVerificao7dias[0])
                    print(f'conta: {self.inputLoginEmail.text()}, Bloqueio de data')

                    self.sinalContaBloqueada = True

                else:
                    driver.find_element_by_css_selector('niowefnvidocvio')
            

        except NoSuchElementException:
            try:
                driver.find_element_by_xpath('//button[@class="aOOlW  bIiDR  "]')
                # clica em reportar erro
                driver.find_element_by_xpath('//button[@class="aOOlW  bIiDR  "]').click()
                # #identifica a conta que ta com o erro
                print(f'conta: {self.inputLoginEmail.text()}, BlockAction')
                # #envia pra lista de contas bloqueadas
                
                self.sinalContaBloqueada = True
        
            except NoSuchElementException:
            
                listVerificaoSms =[]
                try:
                    # page = requests.get("https://sites.google.com/view/taubot/atualizar")
                    soup = BeautifulSoup(driver.page_source, 'html.parser')
                    for _, heading in enumerate(soup.find_all(["h2"])):
                        
                        listVerificaoSms.append(heading.text.strip())
                        if listVerificaoSms[0] == 'Confirme que é você fazendo login':
                            # print(listVerificaoSms[0])
                            print(f'conta: {self.inputLoginEmail.text()}, precisando ser retirada do site, verificacao necessaria')
                            
                            self.sinalContaBloqueada = True
                            
                        else:   
                            driver.find_element_by_css_selector('niowefnvidocvio')
                    
                except NoSuchElementException:
                    # print('passou a verificao de email')
                    try:
                        driver.find_element_by_css_selector('#react-root > section > div > div > div.GA2q- > form > span > button')
                        print(f'conta: {self.inputLoginEmail.text()}, necessita codigo de seguranca(email)')
                        
                        self.sinalContaBloqueada = True
                        
                    except NoSuchElementException:
                        try:
                            driver.find_element_by_css_selector('div.gr27e:nth-child(1)')
                            print(f'conta: {self.inputLoginEmail.text()}, login errado')
                            self.sinalContaBloqueada = True
                        except Exception:
                        # print("sem erros encontrados")
                            pass
# if __name__ == "__main__":
def inicio():    
    ctypes.windll.user32.ShowWindow( ctypes.windll.kernel32.GetConsoleWindow(), 0 )
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
    
inicio()