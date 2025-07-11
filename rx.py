productos = {
    '8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
    '2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
    'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
    'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
    'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
    '123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
    '342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
    'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'],
}

stock = {
    '8475HD': [387990, 10],'2175HD': [327990, 4],'JjfFHD': [424990, 1],
    'fgdxFHD': [664990, 21],
    '123FHD': [290890, 32],
    '342FHD': [444990, 7],
    'GF75HD': [749990, 2],
    'UWU131HD': [349990, 1],
    'FS1230HD': [249990, 0],
}

def stock_marca(marca):
    total = 0
    marca = marca.lower()
    for modelo in productos:
        if productos[modelo][0].lower() == marca:
            total += stock.get(modelo, [0, 0])[1]
    print(f"El stock es: {total}")

def busqueda_precio(p_min, p_max):
    resultados = []
    for modelo, datos in stock.items():
        precio, cantidad = datos
        if p_min <= precio <= p_max and cantidad > 0:
            marca = productos[modelo][0]
            resultados.append(f"{marca}--{modelo}")
    if resultados:
        print("Los notebooks entre los precios consultas son:", sorted(resultados))
    else:
        print("No hay notebooks en ese rango de precios.")

def actualizar(modelo, nuevo_precio):
    if modelo in stock:
        stock[modelo][0] = nuevo_precio
        return True
    else:
        return False

def main():
    while True:
        print("\n ***MENU*** ")
        print("1. stock marca.")
        print("2. buscar por precio.")
        print("3. cambiar precio.")
        print("4. Salir.")
        opcion = input("Ingrese opción: ")
        
        if opcion == '1':
            marca = input("Ingrese marca: ")
            stock_marca(marca)
        
        elif opcion == '2':
            while True:
                try:
                    p_min = int(input("Ingresa el precio minimo: "))
                    p_max = int(input("Ingrese el precio maximo: "))
                    break
                except ValueError:
                    print("tiene que ingresar valores enteros")
            busqueda_precio(p_min, p_max)
        
        elif opcion == '3':
            while True:
                modelo = input("Ingrese el modelo para actualizar: ")
                try:
                    nuevo_precio = int(input("ingresa el precio nuevo: "))
                except ValueError:
                    print("Debe ingresar un precio valido entero")
                    continue

                if actualizar(modelo, nuevo_precio):
                    print("Precio actualizado")
                else:
                    print("El modelo no esta")
                
                continuar = input("Desea actualizar otro precio (si/no)?: ").strip().lower()
                if continuar in ['si']:
                        continue  
                elif continuar in ['no']:
                    break  
                else:
                    print("Debe ingresar'si' o 'no'") 
                    continue
        
        elif opcion == '4':
            print("Fin del programa")
            break

        else:
            print("Ingresa un opcion valida")

main()