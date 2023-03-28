




def inverte_string(string):
    ultima_string = len(string)-1
    str_invertida = ''
    while ultima_string >= 0:
        str_invertida += string[ultima_string]
        ultima_string -= 1

    print(str_invertida)




n = 'FIZ'
inverte_string(n)

