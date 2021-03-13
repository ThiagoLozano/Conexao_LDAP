from ldap3 import Connection, Server
import time
import os
import logging
import json


class Conexao:
    # Método construtor.
    def __init__(self):

        # Configuração da LOG.
        self.data_exec = time.strftime("%Y/%m/%d")
        self.log_folder = self.dirScripts + 'LOGS/' + self.data_exec + '/'
        os.makedirs(os.path.dirname(self.log_folder), exist_ok=True)
        logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                            datefmt='%d/%m/%Y - %H:%M:%S',
                            filename=self.log_folder + 'Conexao_LDAP.log',
                            filemode='a')
        self.logger = logging.getLogger('Processo')

        # Carrega o config.json
        try:
            with open('./config.json') as f:
                self.config = json.load(f)
            self.logger.info('Arquivo de configuração carregado com sucesso')
        except Exception as error:
            self.logger.info('Problemas ao carregar arquivo de configuração - ERROR: {}'.format(str(error)))
            exit(1)

        # Configuração LDAP.
        try:
            self.server = Server(self.config['AD']['Server'], port=self.config['AD']['Port'], use_ssl=True)
            self.user = self.config['AD']['User']
            self.password = self.config['AD']['Password']
            self.conexao = Connection(self.server, self.user, self.password, auto_bind=True)
            self.logger.info('LDAP: Administradores LDAP carregados com sucesso')
        except Exception as erro:
            self.logger.error('LDAP: Erro ao conectar com LDAP - ERROR: {}'.format(str(erro)))
            exit(1)
    
    # Método que mostra os usuários do LDAP e seus grupos correspondentes.
    def Retorna_Users(self):
        for grupo in self.config["Grupos_LDAP"]:
            self.conexao.search(self.config["AD"]["Search_Groups"].format(grupo), "(sAMAccountName=*)")
        
        lista_users = self.conexao.entries
        print(lista_users)

usuario = Conexao()
usuario.Retorna_Users()
