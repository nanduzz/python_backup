from DBBackup import DBBackup
import zipfile
import os

def get_dados_db(file_object):
    line = file_object.readline()
    if line is '\n':
        print("teste")
        return None, None, None, None, None

    dados = line.split('|')
    if(len(dados) < 5):
        dados.append(3306)
    return dados
    

def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file))

def backup_db(file_object):
    endereco, db, login, senha, porta = get_dados_db(fo)

    filename = None
    if endereco is not None:
        DBB =  DBBackup(endereco,db,login,senha, porta)
        filename = DBB.backup()

    return filename

def backup_files(backup_object, files):
        for line in files :
            if(os.path.isfile(line)):
                backup.write(line, compress_type=zipfile.ZIP_DEFLATED)
            else:
                zipdir(line, backup)
        backup.close()

if __name__ == "__main__":
    fo = open('bkp.dat', 'r')
    empresa = fo.readline()[:-1]
    db_filename = backup_db(fo)
    lines = fo.read().splitlines()
    if db_filename is not None :
        lines.append(db_filename)

    backup = zipfile.ZipFile('{}.zip'.format(empresa), 'w')
    backup_files(backup, lines)


    

