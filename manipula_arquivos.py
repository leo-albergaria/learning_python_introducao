def escrever_arquivo(texto):
    diretorio = 'C:/WorkSpaceWEB/pythonProject/app_dio/notas.txt'
    arquivos = open(diretorio, 'w')
    arquivos.write(texto)
    arquivos.close()

def atualizar_arquivo(nome_arquivo, texto):
    arquivos = open(nome_arquivo, 'a')
    arquivos.write(texto)
    arquivos.close()

def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    texto = arquivo.read()
    print(texto)

def media_notas(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    aluno_nota = arquivo.read()
    aluno_nota = aluno_nota.split('\n')
    lista_media = []
    for x in aluno_nota:
        lista_notas = x.split(',')
        aluno = lista_notas[0]
        lista_notas.pop(0)
        media = lambda notas: sum([int (i) for i in notas]) / 4
        lista_media.append({aluno:media(lista_notas)})
    return lista_media

def copiar_arquivo(nome_arquivo):
    import shutil
    diretorio = 'C:/WorkSpaceWEB/pythonProject/app_dio/teste.txt'
    shutil.copy(nome_arquivo, diretorio)

if __name__ == '__main__':
    aluno = 'Aluno 1,7,8,5,6\n'
    escrever_arquivo(aluno)
    aluno = 'Aluno 2,6,8,3,6\n'
    atualizar_arquivo('notas.txt', aluno)
    aluno = 'Aluno 3,2,1,3,2\n'
    atualizar_arquivo('notas.txt', aluno)
    aluno = 'Aluno 4,2,5,7,9'
    atualizar_arquivo('notas.txt', aluno)

    lista_media = media_notas('notas.txt')
    print(lista_media)

    copiar_arquivo('notas.txt')
