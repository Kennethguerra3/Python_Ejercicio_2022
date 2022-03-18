nu = int(input('Ingrese la tabla: '))


def multi(Tabla):
    print("=======================================")
    print("         TABLA DE MULTIPLICAR ", nu)
    print("=======================================")
    for x in range(1, 13):
        Tabla = nu * x  # Hacemos la multiplicacion.
        print(nu, 'X', x, '=', Tabla)

    return Tabla


multi(nu)
