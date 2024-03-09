import subprocess
import ctypes
import sys
import os
from qt_core import *
from ui_design import Ui_MainWindow

def run_as_admin(command):
    try:
        if sys.platform == 'win32':
            # Convertendo o comando para uma string wide char
            command = ctypes.c_wchar_p(command)
            # Executa o comando com privilégios elevados
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, command, None, 1)
        else:
            raise RuntimeError("Este método só é suportado no Windows.")
    except Exception as e:
        print(f"Erro ao executar como administrador: {e}")

class MyFirstWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Made by MP")

        # switch buttons clicked
        self.btn_config.clicked.connect(self.switch_page_config)
        self.btn_bluestacks.clicked.connect(self.switch_page_bs)
        self.btn_msi.clicked.connect(self.switch_page_msi)
        self.reg_btn.clicked.connect(self.switch_page_regedit)

        #config page buttons
        self.limp_cache.clicked.connect(self.cache_naveg)
        self.clear_temp.clicked.connect(self.cl_temp)
        self.dele_arq_logs.clicked.connect(self.arq_logs)
        self.del_arg_temp.clicked.connect(self.arq_temp)
        self.des_serv.clicked.connect(self.des_services)
        self.des_win_updt.clicked.connect(self.des_win_updte)
        self.limp_cache_2.clicked.connect(self.limpar_cache)
        self.limpz_servi.clicked.connect(self.limp_services)
        self.mem_ptm.clicked.connect(self.mem_optm)
        self.otm.clicked.connect(self.otimizacao)
        self.ten_apps.clicked.connect(self.ten_app)

        # dowload bluestacks clicked
        self.download_ultra_ego_bs.clicked.connect(self.download_ultra_ego)
        self.download_5_20_0_1037bs.clicked.connect(self.download_bs_5_20_0_1037)
        self.download_4_240_1002bs.clicked.connect(self.download_4_2401002bs)

        # download msi clicked
        self.download_ultra_god_msi.clicked.connect(self.download_ultra_god)
        self.download_msi5_12.clicked.connect(self.download_msi_512)
        self.download_m.clicked.connect(self.download_msi_4_240_5318)

        # buttons of regedits
        self.acelerando_menu.clicked.connect(self.acelerar_menu)
        self.aumentar_capacidade.clicked.connect(self.capacidade_de_resposta)
        self.aumente_fps.clicked.connect(self.aumentar_fps)
        self.des_DVR.clicked.connect(self.des_dVR)
        self.efeitos_visuais.clicked.connect(self.efeitos_Visuais)
        self.full_screen_fix.clicked.connect(self.full_screen_Fix)
        self.game_optm.clicked.connect(self.game_Optm)
        self.red_inp_lag.clicked.connect(self.inp_lag)
        self.des_maps.clicked.connect(self.gerenciador_mapas)
        self.des_blue.clicked.connect(self.bluetooth)
        self.des_impre.clicked.connect(self.impressoras)
        self.des_xbox.clicked.connect(self.xbox)
        self.des_extr_desn.clicked.connect(self.extras_desne)
        self.des_uac.clicked.connect(self.uac)
        self.des_windef.clicked.connect(self.win_def)

    # functions for switch pages
    def switch_page_config(self):
        self.stackedWidget.setCurrentIndex(0)
            
    def switch_page_bs(self):
        self.stackedWidget.setCurrentIndex(1)

    def switch_page_msi(self):
        self.stackedWidget.setCurrentIndex(2)

    def switch_page_regedit(self):
        self.stackedWidget.setCurrentIndex(3)

    # functions of msi download buttons    
    def download_ultra_god(self):
        url = QUrl("https://drive.google.com/file/d/1BCs_OiI6J3a1cUuWuwaKD31B2jvLBkWC/view?pli=1") 
        QDesktopServices.openUrl(url)

    def download_msi_512(self):
        url = QUrl("https://www.mediafire.com/file/txiuddc7fn53cj5/MSI-APP-Player.zip/file") 
        QDesktopServices.openUrl(url)

    def download_msi_4_240_5318(self):
        url = QUrl("https://www.mediafire.com/file/tfgidqovz9nl4h0/BlueStacks-Installer_4.240.15.5318_amd64_native.exe/file") 
        QDesktopServices.openUrl(url)    

    # functions of bluestacks download buttons
    def download_ultra_ego(self):
        url = QUrl("https://www.mediafire.com/file/x2wghpd9p74wrkj/Beta_2.0.zip/file") 
        QDesktopServices.openUrl(url)    

    def download_bs_5_20_0_1037(self):
        url = QUrl("https://www.mediafire.com/file/jlf4kjjtzwwipgx/BlueStacksInstaller_5.20.0.1037_native_b212855fe2cefe4a2d67ee40fa806a88_MzsxNSwwOzUsMTsxNSw0OzE1.exe/file") 
        QDesktopServices.openUrl(url)    

    def download_4_2401002bs(self):
        url = QUrl("https://www.mediafire.com/file/ej76v8p5vgkmqyo/BS+Ultra+Ego+Version+Final+Beta+1x.rar/file") 
        QDesktopServices.openUrl(url)   


    # functions of regedits
    def acelerar_menu(self):
        diretorio_coding = os.path.dirname(os.path.abspath(__file__))
        reg = os.path.join(diretorio_coding, "regs")
        reg_path = os.path.join(reg, "Acelerando o Menu Iniciar.reg")

        try:
            subprocess.Popen(reg_path, shell=True)
            print("Aplicativo iniciado com sucesso!")
        except Exception as e:
            print(f"Erro ao executar o aplicativo: {e}") 

    def capacidade_de_resposta(self):
        diretorio_coding = os.path.dirname(os.path.abspath(__file__))
        reg = os.path.join(diretorio_coding, "regs")
        reg_path = os.path.join(reg, "Aumentar Capacidade de Resposta.reg")

        try:
            subprocess.Popen(reg_path, shell=True)
            print("Aplicativo iniciado com sucesso!")
        except Exception as e:
            print(f"Erro ao executar o aplicativo: {e}")	

    def aumentar_fps(self):
        diretorio_coding = os.path.dirname(os.path.abspath(__file__))
        reg = os.path.join(diretorio_coding, "regs")
        reg_path = os.path.join(reg, "Aumente FPS nos Jogos.reg")

        try:
            subprocess.Popen(reg_path, shell=True)
            print("Aplicativo iniciado com sucesso!")
        except Exception as e:
            print(f"Erro ao executar o aplicativo: {e}")

    def des_dVR(self):
        diretorio_coding = os.path.dirname(os.path.abspath(__file__))
        reg = os.path.join(diretorio_coding, "regs")
        reg_path = os.path.join(reg, "Desabilitar Game DVR.reg")

        try:
            subprocess.Popen(reg_path, shell=True)
            print("Aplicativo iniciado com sucesso!")
        except Exception as e:
            print(f"Erro ao executar o aplicativo: {e}")

    def efeitos_Visuais(self):
        diretorio_coding = os.path.dirname(os.path.abspath(__file__))
        reg = os.path.join(diretorio_coding, "regs")
        reg_path = os.path.join(reg, "Efeitos Visuais.reg")

        try:
            subprocess.Popen(reg_path, shell=True)
            print("Aplicativo iniciado com sucesso!")
        except Exception as e:
            print(f"Erro ao executar o aplicativo: {e}")

    def full_screen_Fix(self):
        diretorio_coding = os.path.dirname(os.path.abspath(__file__))
        reg = os.path.join(diretorio_coding, "regs")
        reg_path = os.path.join(reg, "Fullscreen Fix.reg")

        try:
            subprocess.Popen(reg_path, shell=True)
            print("Aplicativo iniciado com sucesso!")
        except Exception as e:
            print(f"Erro ao executar o aplicativo: {e}")

    def game_Optm(self):
        diretorio_coding = os.path.dirname(os.path.abspath(__file__))
        reg = os.path.join(diretorio_coding, "regs")
        reg_path = os.path.join(reg, "Game Optimizations.reg")

        try:
            subprocess.Popen(reg_path, shell=True)
            print("Aplicativo iniciado com sucesso!")
        except Exception as e:
            print(f"Erro ao executar o aplicativo: {e}")

    def inp_lag(self):
        diretorio_coding = os.path.dirname(os.path.abspath(__file__))
        reg = os.path.join(diretorio_coding, "regs")
        reg_path = os.path.join(reg, "Reduzir Input Lag.reg")

        try:
            subprocess.Popen(reg_path, shell=True)
            print("Aplicativo iniciado com sucesso!")
        except Exception as e:
            print(f"Erro ao executar o aplicativo: {e}")       		

    def gerenciador_mapas(self):
        diretorio_coding = os.path.dirname(os.path.abspath(__file__))
        reg = os.path.join(diretorio_coding, "regs/regs_2")
        reg_path = os.path.join(reg, "Desabilitar gerenciador de mapas.reg")

        try:
            subprocess.Popen(reg_path, shell=True)
            print("Aplicativo iniciado com sucesso!")
        except Exception as e:
            print(f"Erro ao executar o aplicativo: {e}")

    def bluetooth(self):
        diretorio_coding = os.path.dirname(os.path.abspath(__file__))
        reg = os.path.join(diretorio_coding, "regs/regs_2")
        reg_path = os.path.join(reg, "Desabilitar serviços de bluetooth.reg")

        try:
            subprocess.Popen(reg_path, shell=True)
            print("Aplicativo iniciado com sucesso!")
        except Exception as e:
            print(f"Erro ao executar o aplicativo: {e}")

    def impressoras(self):
        diretorio_coding = os.path.dirname(os.path.abspath(__file__))
        reg = os.path.join(diretorio_coding, "regs/regs_2")
        reg_path = os.path.join(reg, "Desabilitar serviços de impressoras.reg")

        try:
            subprocess.Popen(reg_path, shell=True)
            print("Aplicativo iniciado com sucesso!")
        except Exception as e:
            print(f"Erro ao executar o aplicativo: {e}")

    def xbox(self):
        diretorio_coding = os.path.dirname(os.path.abspath(__file__))
        reg = os.path.join(diretorio_coding, "regs/regs_2")
        reg_path = os.path.join(reg, "Desabilitar serviços do Xbox.reg")

        try:
            subprocess.Popen(reg_path, shell=True)
            print("Aplicativo iniciado com sucesso!")
        except Exception as e:
            print(f"Erro ao executar o aplicativo: {e}")

    def extras_desne(self):
        diretorio_coding = os.path.dirname(os.path.abspath(__file__))
        reg = os.path.join(diretorio_coding, "regs/regs_2")
        reg_path = os.path.join(reg, "Desabilitar serviços extras desnecessários.reg")

        try:
            subprocess.Popen(reg_path, shell=True)
            print("Aplicativo iniciado com sucesso!")
        except Exception as e:
            print(f"Erro ao executar o aplicativo: {e}")

    def uac(self):
        diretorio_coding = os.path.dirname(os.path.abspath(__file__))
        reg = os.path.join(diretorio_coding, "regs/regs_2")
        reg_path = os.path.join(reg, "Desabilitar UAC.reg")

        try:
            subprocess.Popen(reg_path, shell=True)
            print("Aplicativo iniciado com sucesso!")
        except Exception as e:
            print(f"Erro ao executar o aplicativo: {e}")

    def win_def(self):
        diretorio_coding = os.path.dirname(os.path.abspath(__file__))
        reg = os.path.join(diretorio_coding, "regs/regs_2")
        reg_path = os.path.join(reg, "Desativar Windows Defender.reg")

        try:
            subprocess.Popen(reg_path, shell=True)
            print("Aplicativo iniciado com sucesso!")
        except Exception as e:
            print(f"Erro ao executar o aplicativo: {e}")


    def run_with_console(self, command):
        try:
            subprocess.Popen(['start', 'cmd', '/k', command], shell=True)
            print("Comando executado com sucesso!")
        except Exception as e:
            print(f"Erro ao executar o comando: {e}")

    def cache_naveg(self):
        diretorio_coding = os.path.dirname(os.path.abspath(__file__))
    
        pasta_executaveis = os.path.join(diretorio_coding, 'executaveis')
    
        bat_file = os.path.join(pasta_executaveis, "Limpar_Cache_de_Navegador.bat")
    
        self.run_with_console(bat_file)

    def cl_temp(self):
        diretorio_coding = os.path.dirname(os.path.abspath(__file__))
    
        pasta_executaveis = os.path.join(diretorio_coding, 'executaveis')
    
        bat_file = os.path.join(pasta_executaveis, "Clear_Temp.bat")
    
        self.run_with_console(bat_file)

    def arq_logs(self):
        diretorio_coding = os.path.dirname(os.path.abspath(__file__))
    
        pasta_executaveis = os.path.join(diretorio_coding, 'executaveis')
    
        bat_file = os.path.join(pasta_executaveis, "Deletar_Arquivos_de_Logs.bat")
    
        self.run_with_console(bat_file)

    def arq_temp(self):
        diretorio_coding = os.path.dirname(os.path.abspath(__file__))
    
        pasta_executaveis = os.path.join(diretorio_coding, 'executaveis')
    
        bat_file = os.path.join(pasta_executaveis, "Deletar_Arquivos_Temporarios.bat")
    
        self.run_with_console(bat_file)

    def des_services(self):
        diretorio_coding = os.path.dirname(os.path.abspath(__file__))
    
        pasta_executaveis = os.path.join(diretorio_coding, 'executaveis')
    
        bat_file = os.path.join(pasta_executaveis, "Desabilitar_Servicos.cmd")
    
        self.run_with_console(bat_file)

    def des_win_updte(self):
        diretorio_coding = os.path.dirname(os.path.abspath(__file__))
    
        pasta_executaveis = os.path.join(diretorio_coding, 'executaveis')
    
        bat_file = os.path.join(pasta_executaveis, "Desativar_Windows_Update.bat")
    
        self.run_with_console(bat_file)

    def limpar_cache(self):
        diretorio_coding = os.path.dirname(os.path.abspath(__file__))
    
        pasta_executaveis = os.path.join(diretorio_coding, 'executaveis')
    
        bat_file = os.path.join(pasta_executaveis, "Limpador_de_Cache.bat")
    
        self.run_with_console(bat_file)

    def limp_services(self):
        diretorio_coding = os.path.dirname(os.path.abspath(__file__))
    
        pasta_executaveis = os.path.join(diretorio_coding, 'executaveis')
    
        bat_file = os.path.join(pasta_executaveis, "Limpeza_De_Serviços.bat")
    
        self.run_with_console(bat_file)

    def mem_optm(self):
        diretorio_coding = os.path.dirname(os.path.abspath(__file__))
    
        pasta_executaveis = os.path.join(diretorio_coding, 'executaveis')
    
        bat_file = os.path.join(pasta_executaveis, "Memory_Optmizer.bat")
    
        self.run_with_console(bat_file)

    def otimizacao(self):
        diretorio_coding = os.path.dirname(os.path.abspath(__file__))
    
        pasta_executaveis = os.path.join(diretorio_coding, 'executaveis')
    
        bat_file = os.path.join(pasta_executaveis, "Otimização.bat")
    
        self.run_with_console(bat_file)

    def ten_app(self):
        diretorio_coding = os.path.dirname(os.path.abspath(__file__))
        app10 = os.path.join(diretorio_coding, "10app_manager")
        application_path = os.path.join(app10, "10AppsManager.exe")

        try:
            subprocess.Popen(application_path, shell=True)
            print("Aplicativo iniciado com sucesso!")
        except Exception as e:
            print(f"Erro ao executar o aplicativo: {e}") 