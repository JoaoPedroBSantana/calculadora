a = int(input("DIGITE UM VALOR: "))

b = int(a)
c = int(a)
#d = int(a)

bin = format(b, 'b')

print(bin)

z = int(input("DIGITE 1 PARA OCTAL OU 2 PARA HEXADECIMAL: "))

if z == 1:

    oct = format(c, 'o')
    print(oct)

elif z == 2:

    hex = format(c, 'x')
    print(hex)
