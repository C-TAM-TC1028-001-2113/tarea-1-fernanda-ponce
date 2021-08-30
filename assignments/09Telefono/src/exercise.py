def main():
    # escribe tu código abajo de esta línea
    pass
mensajes = int(input("Dame el número de mensajes: "))
megas = float(input("Dame el número de megas: "))
minutos = int(input("Dame el número de minutos: "))
costo_mensual = 0.80 * (mensajes + megas + minutos)
print("El costo mensual es:", costo_mensual)

if __name__ == '__main__':
    main()
