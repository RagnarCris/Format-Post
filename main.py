import subprocess
import sys

def conserta_arquivo(filename):

    resultfile = ''

    file = open(filename, 'r')

    lines = file.readlines()

    newlines = []

    print(len(lines))

    for line in lines:
        partes = line.split(' ] [ ')    
        aux = partes[0]
        teste = aux.split(' [ ')
        partes.remove(partes[0])
        partes.insert(0, teste[1])
        #partes.insert(0, teste[0])
        resultfile = teste[0] + '_new_post.txt'
        aux = partes[-1]
        partes.pop(-1)
        xua = aux.split(' ]')
        partes.append(xua[0])
        newlines = partes

    with open(resultfile, 'w+') as filehandle:
        filehandle.writelines("%s\n" % newline for newline in newlines)

def roda_int2sym(filename, saida=''):
    if saida != '':
        comando = 'int2sym.pl -f 1 data/grammar/lang/words.txt ' + filename + ' > ' + saida
    else:
        comando = 'int2sym.pl -f 1 data/grammar/lang/words.txt ' + filename
    output = subprocess.check_output(comando, shell=True, universal_newlines=True)
   
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Falta-lhe argumentos meu caro, voce pode colocar apenas o arquivo de entrada, ou o arquivo de entrada e saida, para o caso de nao querer visualizar no terminal.")
    else:       
        conserta_arquivo(sys.argv[1])
        '''
        if len(sys.argv) == 2:
            roda_int2sym(sys.argv[1])        
        if len(sys.argv) == 3:
            print("O arquivo de saida sera: %s"%(sys.argv[2]))
            roda_int2sym(sys.argv[1], sys.argv[2])
        '''
