productos = {
'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
'2175HD': ['Acer', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
'123FHD': ['Acer', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
'342FHD': ['Acer', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'],
}

stock = {
'8475HD': ['HP', 387990, 10],
'2175HD': ['Acer', 327990, 4],
'JjfFHD': ['Asus', 424990, 1],
'fgdxFHD': ['HP', 664990, 21],
'123FHD': ['Acer', 290890, 32],
'342FHD': ['Acer', 444990, 7],
'GF75HD': ['Asus', 749990, 2],
'UWU131HD': ['Dell', 349990, 1]
}

def mostrar_menu():
    print('*** MENU PRINCIPAL ***')
    print('1. Stock marca.')
    print('2. Busqueda por RAM y precio.')
    print('3. Eliminar producto.')
    print('4. Salir')

def stock_marca():
    marca = input('> Ingrese marca a consultar: ')
    try:
        if marca == 'HP':
            print('El stock es: 31')
        elif marca == 'Acer':
            print('El stock es: 43')
        elif marca == 'Asus':
            print('El stock es: 3')
        elif marca == 'Dell':
            print('El stock es: 1')
    except ValueError:
        print('Valor no valido. Intente nuevamente.')


while True:

    mostrar_menu()
    opc = input('> Ingrese opcion: ')
    if opc == '1':
        stock_marca()
    elif opc == '4':
        print('Saliendo del sistema...')
        print('Programa finalizado.')
        break
    else:
        print('Debe seleccionar una opcion valida!!')