import subprocess
import sys

def merge_files(filepostname, fileconfname):
    
    resultfile = ''

    filepost = open(filepostname, 'r')

    fileconf = open(fileconfname, 'r')

    linesPost = filepost.readlines()

    linesConf = fileconf.readlines()

    newLinesPost = []

    resultList = []

    print(len(linesPost))
    print(len(linesConf))

    for line in linesPost:
        partes = line.split(' ] [ ')    
        aux = partes[0]
        teste = aux.split(' [ ')
        partes.remove(partes[0])
        partes.insert(0, teste[1])
        #partes.insert(0, teste[0])
        resultfile = 'result_' + teste[0] + '.txt'
        aux = partes[-1]
        partes.pop(-1)
        xua = aux.split(' ]')
        partes.append(xua[0])
        newLinesPost = partes

    ind = 0
    for line in linesConf:
        partes = line.split(' ')
        partes.pop(-1)
        linhaPost = newLinesPost[ind]
        aux = linhaPost.split(' ')
        partes.append(aux[1])
        linha = ' '.join(partes)
        resultList.append(linha)
        ind+=1

    with open(resultfile, 'w+') as filehandle:
        filehandle.writelines("%s\n" % newline for newline in resultList)
   
if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Falta-lhe argumentos meu caro, eh necessario o arquivo post e o ctm-conf respectivamente.")
    elif len(sys.argv) == 3:   
        merge_files(sys.argv[1], sys.argv[2])
    else:
        print("Argumentos demais meu caro, manera ai")