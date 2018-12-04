import os
import subprocess
from subprocess import Popen, PIPE, STDOUT

class DBBackup(object):
    def __init__(self, endereco, database, login, senha, porta=3306):
        self.endereco = endereco
        self.database = database
        self.login = login
        self.senha = senha
        self.porta = porta
        self.filename = '{}.bkp'.format(self.database)

    def print_dados(self):
        print('endereco:{}, database:{}, login:{}, senha:{}'.format(self.endereco, self.database, self.login, self.senha))


    def backup(self):
        #subprocess.Popen('mysqldump -h localhost -P 3306 -u -root mydb | mysql -h localhost -P 3306 -u root mydb2', shell=True)
        p1 = subprocess.Popen('mysqldump -h {} -P {} -u {} -p{} {}'.format(
            self.endereco,
            self.porta,
            self.login,
            self.senha,
            self.database
        ), stdout=PIPE, shell=True)
        out, err = p1.communicate()
        fo = open(self.filename, 'w')
        fo.write(out.decode("utf-8"))
        fo.close()
        print("backup terminado do banco de dados")
        return self.filename