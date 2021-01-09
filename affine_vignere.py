import math

abecedario_vignere = "abcdefghijklmnopqrstuvwxyz"

def ae(a,n):
    if(n==0):
        if(a != 1):
            return -1 #No son coprimos
        return a
    return ae(n, a%n)

def aee(a,n):
    if n == 0:
        return 0,1,0 #El alfabeto tiene 0 elementos
    x0 = 1
    x1 = 0
    y0 = 0
    y1 = 1
 
    while n != 0:
        q = a//n
        r = a - n * q
        x = x0 - q * x1
        y = y0 - q * y1
        #Actualiza a,n
        a = n
        n = r
        #actualiza para la siguiente iteración
        x0 = x1
        x1 = x
        y0 = y1
        y1 = y
    return  a, x0, y0

def factores (a,n):
    alphas = []
    for i in range(a, n+1):
        if ae(i,n) == 1:
            alphas.append(i)
    return alphas

def modinv(a, m): 
    gcd, x, y = aee(a, m) 
    if gcd != 1: 
        return -1  # no existe inverso modular 
    else: 
        return x % m 

def cifrado_affine(texto, a, b, n):
    ### C = (a*P + b) % n
    #Se obtiene el valor ASCII del caracter a cifrar, aplica la formula, 
    ##se retorna el caracter homólogo y se concatena a una cadena de texto##
    texto_cifrado = ''.join([ chr((( a*(ord(t) - ord(' ')) + b ) % n)
                  + ord(' ')) for t in texto])
    return texto_cifrado

def descifrar_affine(texto_cifrado, a, b, n): 
     
    ##P = (a^-1 * (C - b)) % 26
    #Se aplica la formula utilizando el valor ASCII de cada caracter del texto,##
    ##retornando el caracter original y concatenandolo a una cadena## 
    texto_descifrado = ''.join([ chr((( modinv(a, n)*(ord(c) - ord(' ') - b))  
                    % n) + ord(' ')) for c in texto_cifrado]) 
    return texto_descifrado
  
def cifrado_vigenere(texto, llave):
    texto = texto.replace(" ", "")
    texto_cifrado = ""
    nueva_llave =""
    if len(texto)>len(llave):	# Si la logitud del texto es mayor que la de la nueva_llave... #
        for i in range(int(len(texto)/len(llave))):		## Se alarga la nueva_llave, duplicándola y		 ##
            nueva_llave += llave						## concatenándosela a sí misma, hasta que su ##
        nueva_llave += llave[:len(texto)%len(llave)]	## longitud sea la misma que la del texto  ##

    elif len(texto)<len(llave):	# Si la longitud del texto es menor que la de la nueva_llave...
    	nueva_llave = llave[:len(texto)]	# Se trunca la nueva_llave para que tenga la misma longitud que el texto #

    elif len(texto)==len(llave):	# Si la longitud del texto es igual que la de la nueva_llave... #
    	nueva_llave = llave	# Se guarda la nueva_llave tal cual se encuentra en 'llave' #
    for i in range(len(texto)):
        x = abecedario_vignere.find(texto[i])# Se guarda la posición del caracter del mensaje en el abecedario
        y = abecedario_vignere.find(nueva_llave[i])	# Se guarda la posición del caracter de la clave en el abecedario
        suma = x+y	# Se calcula la suma de ambas posiciones
        modulo = suma%len(abecedario_vignere)	# Se calcula el módulo de la suma respecto a la longitud del abecedario
        texto_cifrado += abecedario_vignere[modulo]	# Se concatena el caracter cifrado con 'texto_cifrado'
    return texto_cifrado

def descifrar_vigenere(texto_cifrado, llave):
    llave_inversa = ""
    nueva_llave = ""
    texto_descifrado = ""
    for i in llave:
        pos = (len(abecedario_vignere) - abecedario_vignere.find(i)
               )%len(abecedario_vignere) ## Se calcula la posición del inverso de cada letra 
        llave_inversa += abecedario_vignere[pos] #se concatena la letra encontrada en la llave inversa
    if len(texto_cifrado)>len(llave_inversa):	# Si la logitud del texto es mayor que la de la nueva_llave... #
        for i in range(int(len(texto_cifrado)/len(llave_inversa))):		## Se alarga la nueva_llave, duplicándola y		 ##
            nueva_llave += llave_inversa                                ## concatenándosela a sí misma, hasta que su ##
        nueva_llave += llave_inversa[:len(texto_cifrado)%len(llave_inversa)]	## longitud sea la misma que la del texto  ##

    elif len(texto_cifrado)<len(llave_inversa):	# Si la longitud del texto es menor que la de la nueva_llave...
    	nueva_llave = llave_inversa[:len(texto_cifrado)]	# Se trunca la nueva_llave para que tenga la misma longitud que el texto #

    elif len(texto_cifrado)==len(llave_inversa):	# Si la longitud del texto es igual que la de la nueva_llave... #
    	nueva_llave = llave_inversa	# Se guarda la nueva_llave tal cual se encuentra en 'llave' #                        

    for i in range(len(texto_cifrado)):
        x = abecedario_vignere.find(texto_cifrado[i])	# Se guarda la posición del caracter del mensaje cifrado en el abecedario
        y = abecedario_vignere.find(nueva_llave[i])	# Se guarda la posición del caracter de la clave en el abecedario
        suma = x+y	# Se calcula la suma de ambas posiciones
        modulo = suma%len(abecedario_vignere)	# Se calcula el módulo de la resta respecto a la longitud del abecedario
        texto_descifrado += abecedario_vignere[modulo]	# Se concatena el caracter descifrado con 'descifrado'
    return texto_descifrado, llave_inversa
    

def get_text_string(fname):
    ##abrimos el archivo
    f = open(fname,encoding='utf-8')
    ##obtenemos el texto
    textString = f.read()
    f.close()
    textString = textString.replace("\n", " ")
    return textString

def save_text(texto, fname):
    f = open(fname, 'w',encoding = 'utf-8')
    f.write(texto)
    f.close()

if __name__ == "__main__":
    '''fname = "simon_paraAffine.txt"
    fname_aff = "simon_paraAffine.aff"
    text = get_text_string(fname)
    a,b = 17, 20
    n= 97
    # calling encryption function 
    affine_encriptado= cifrado_affine(text, a,b,n) 
    save_text(affine_encriptado, fname_aff)
    text_ciph = get_text_string(fname_aff)
    print(descifrar_affine(text_ciph,a,b,n))
    fname = "Elvis_paravigenere.txt"
    fname_vig = "Elvis_paravigenere.aff"
    text = get_text_string(fname)
    llave = "amulets"
    vignere_encriptado = cifrado_vignere(text, llave)
    print(vignere_encriptado)
    print(descifrar_vignere(vignere_encriptado,llave))'''