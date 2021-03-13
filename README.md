# PROJETO PYTHON: Conexão LDAP

> Modelo de Script de conexão com o sistema LDAP, que retorna os usuários encontrados de cada grupo.

# Tecnologias Utilizadas

* **_VScode_**;

* **_Python3;_** 

  

# Bibliotecas e Configurações

### Bibliotecas Utilizadas

```python
from ldap3 import Connection, Server
import time
import os
import logging
import json
```

### Configurações

> O script foi feito com base na estrutura POO.

```python
class Conexao:
    def __init__(self):

usuario = Conexao()
usuario.Retorna_Users()
```

# Fontes

> https://ldap3.readthedocs.io/en/latest/tutorial_searches.html
>
> https://ldap3.readthedocs.io/en/latest/server.html
>
> https://www.youtube.com/watch?v=fhQE342ZTrk&t=227s

# Detalhes de Processo

### LOG

```python
# Configuração da LOG.
1. self.data_exec = time.strftime("%Y/%m/%d")
2. self.log_folder = self.dirScripts + 'LOGS/' + self.data_exec + '/'
3. os.makedirs(os.path.dirname(self.log_folder), exist_ok=True)
4. logging.basicConfig(level=logging.INFO,
5.                   format='%(asctime)s %(name)-12s %(levelname)-8s  (message)s',
6.                   datefmt='%d/%m/%Y - %H:%M:%S',
7.                   filename=self.log_folder + 'Conexao_LDAP.log',
8.                   filemode='a')
9. self.logger = logging.getLogger('Processo')
```

> Linha 1: Cria uma variável que recebe o Ano / Mês / Dia atual.
>
> Linha2:   Cria uma variável com o diretório que a LOG vai seguir.
>
> Linha 3: Cria o diretório.
>
> Linha 4, 5, 6, 7, 8: Faz a configuração da LOG (Formato / Data-Hora / Nome / Tipo) .
>
> Linha 9:  Nome de cada etapa da LOG.

### Configuração JSON

```json
{
    "AD": {
        "Server": "",
        "Port": "",
        "User": "",
        "Password": "",
        "Search_Groups": ""
    },
    "Grupos_LDAP":[""]
}
```

> O arquivo config.json serve para armazenar as configurações de conexão do LDAP, isso ajuda a não ter que alterar dentro do script toda vez que algum parâmetro for trocado, podendo apenas modificar o JSON.

> Objetos que são armazenados:
>
> __Server:__ O host em que será conectado (12.345.67.890 ou host.com.br)
>
> __Port:__ Onde a conexão pode entrar (636, por exemplo)
>
> __User:__ usuário que está conectando no LDAP (caminho na árvore onde está o usuário, por exemplo,                                        cn=<nome_usuário_aqui>,cn=<campo_de_usuários>,dc=<caminho_user>,dc=<caminho_user>)
>
> __Password:__ A senha que é usada para se conectar com o LDAP.
>
> __Grupos_LDAP:__ Lista que armazena os nomes dos grupos que existem dentro do LDAP (ADM / MASTER / ACCOUNT/ ...)



``` python
# Carrega o config.json
1. try:
2.   with open('./config.json') as f:
3.    self.config = json.load(f)
4.    self.logger.info('Arquivo de configuração carregado com sucesso')
5. except Exception as error:
6.    self.logger.error('Problemas ao carregar arquivo de configuração - ERROR: {}'.format(str(error)))
7.    exit(1)
```

> Linha 1: Chama a função de Try.
>
> Linha 2:  Abre o arquivo __config.json__ e coloca em uma variável chamada __f__.
>
> Linha 3:  Cria uma variável  que recebe arquivo carregado como JSON.
>
> Linha 4: Faz uma chamada de LOG com tipo INFO.
>
> Linha 5:  Chama a Exceção e da uma apelido de __error__ (criado junto com o Try), serve para retornar caso tenha algum erro de execução.
>
> Linha 6: Faz uma chamada de LOG com tipo ERROR.
>
> Linha 7: Fecha o programa com o comando __exit()__.



### Configurações LDAP

```python
1 try:
2    self.server = Server(self.config['AD']['Server'], port=self.config['AD']['Port'], use_ssl=True)
3    self.user = self.config['AD']['User']
4    self.password = self.config['AD']['Password']
5    self.conexao = Connection(self.server, self.user, self.password, auto_bind=True)
6    self.logger.info('LDAP: Administradores LDAP carregados com sucesso')
7 except Exception as erro:
8    self.logger.error('LDAP: Erro ao conectar com LDAP - ERROR: {}'.format(str(erro)))
9    exit(1)
```

> Linha 1:  Chama a função de Try.
>
> Linha 2: Recebe a configuração do server -> Server (<server_do_config.json>, port= <porta_no_config.json>, user_ssl =True)
>
> Linha 3: Pega o nome do usuário no config.json
>
> Linha 4: Pega a senha do usuário no config.json
>
> Linha 5: Faz a conexão -> Connection (<server>, <user>, <password>, auto_bind =True)
>
> Linha 6: Faz uma chamada de LOG com tipo INFO.
>
> Linha 7: Chama a Exceção.
>
> Linha 8: Faz uma chamada de LOG com tipo ERROR.
>
> Linha 9: Fecha  o programa.

# Retorno dos Dados

```python
1. def Retorna_Users(self):
2.   for grupo in self.config["Grupos_LDAP"]:
3.   	self.conexao.search(self.config["AD"]["Search_Groups"].format(grupo), "(sAMAccountName=*)")
4.   	lista_users = self.conexao.entries
5.   	print(lista_users)
```

> Linha 1: Cria a função __Retorna_Users__
>
> Linha 2: Cria uma laço que passa pelos nomes de cada grupo no config.json
>
> Linha 3: Faz uma busca pelos grupos com o atributo de __sAMAccountName__
>
> Linha 4: Recebe os dados em formato de lista.
>
> Linha 5: Retorna todos os usuário com seus grupos correspondentes.

