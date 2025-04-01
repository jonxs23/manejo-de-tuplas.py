# 📦 lista de productos (cada producto es una tupla con nombre,precio y  stock)
productos = [
     ("laptop", 15000, 5),
     ("mause", 500, 20),
     ("teclado", 800, 15),
     ("monitor", 4000, 10),
     ("USB", 300 , 50)
 ]

def mostrar_menu():
    print("\n📌 MENU DE TIENDA 📌")
    print("1. ver productos ")
    print("2. buscar producto")
    print("3. salir")

def ver_productos():
    print("\n📝 lista de productos:")
    for i, producto in enumerate(producto, 1): #enumeramos para mostrar numeros
        nombre, precio, stock = productos #desempaquetamos la tupla
        print(f"{i}. {nombre} - 💰 💲{precio} - 📦 stock: {stock} ")
        
def buscar_producto():
    nombre_busqueda = input("🔍 ingresa el nombre del producto: ").lower()
    encontrado= False # variable para verificar si se encuentra el producto
    
    for nombre, precio, stock in productos:
        if nombre.lower() == nombre_busqueda:
            print(f"\n✅ producto encontrado: {nombre} - 💰💲{precio} - 📦 stock: {stock}")
            encontrado = True
            break # detenemos la busqueda cuando encontramos el producto
        
    if not encontrado:
        print("❌ producto no encontrado.")

while True:
    mostrar_menu()
    opcion = input("seleecciona una opcion (1-3): ")
    
    if opcion == "1":
        ver_productos()
    elif opcion == "2":
        buscar_producto()
    elif opcion == "3":
        print("👋 ¡gracias por usar la tienda!")
        break #terminar el programa
    else:
        print("⚠ opcion no valida. intenta de nuevo.")
        
