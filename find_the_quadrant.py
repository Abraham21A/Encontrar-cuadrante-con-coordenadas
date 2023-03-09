
# Encuentra el cuadrante / Programa para determinar el cuadrante de un punto con coordenadas de un plano cartesiano

# Inicia el bucle while que se ejecutará continuamente hasta que se detenga manualmente.
while True:
    # Se utiliza el bloque try-except para manejar errores de entrada de datos.
    try:
        
        # Se solicita al usuario ingresar las coordenadas X e Y del punto
        # Se convierte la entrada en un número decimal.
        coordinate_x = float(input("Ingresa una coordenada X: "))
        coordinate_y = float(input("Ingresa una coordenada Y: "))

        # Se utiliza una serie de condicionales para determinar en 
        # qué cuadrante se encuentra el punto definido por las coordenadas ingresadas.
        # En caso de que alguna de las coordenadas sea igual a cero, se emite un mensaje de error.
        if coordinate_x == 0 or coordinate_y == 0:
            print("Error: Las coordenadas deben ser diferentes de cero.")
        # Si ambas coordenadas son positivas, el punto se encuentra en el cuadrante I.
        elif coordinate_x > 0 and coordinate_y > 0:
            print("El punto X: {}, Y: {} se encuentra en el cuadrante I".format(coordinate_x, coordinate_y))
        # Si la coordenada X es negativa y la coordenada Y es positiva, el punto se encuentra en el cuadrante II.
        elif coordinate_x < 0 and coordinate_y > 0:
            print("El punto X: {}, Y: {} se encuentra en el cuadrante II".format(coordinate_x, coordinate_y))
        # Si ambas coordenadas son negativas, el punto se encuentra en el cuadrante III.
        elif coordinate_x < 0 and coordinate_y < 0:
            print("El punto X: {}, Y: {} se encuentra en el cuadrante III".format(coordinate_x, coordinate_y))
        # Si la coordenada X es positiva y la coordenada Y es negativa, el punto se encuentra en el cuadrante IV.
        else:
            print("El punto X: {}, Y: {} se encuentra en el cuadrante IV".format(coordinate_x, coordinate_y))
        
        # Se utiliza otro bucle while para solicitar al usuario si desea ingresar otra coordenada o salir del programa.
        while True:
            control = input("Escriba (si) si desea ingresar otra coordenada, (no) para finalizar programa: ")
            # Si el usuario ingresa 'no', el programa se detiene.
            if control.lower() == 'no':
                exit() 
            # Si el usuario ingresa 'si', el programa vuelve a solicitar coordenadas.
            elif control.lower() == 'si':
                break
            # Si el usuario ingresa una respuesta inválida, se emite un mensaje de error y se solicita una respuesta válida.
            elif control != "si" and control != "no":
                print("dato no valido, ingrese una respuesta valida")
                continue
    # Se captura la excepción de ValueError, que ocurre si el usuario ingresa un valor no numérico.    
    except ValueError:
        print("Las coordenadas deben ser valores numéricos. Intente otra vez")
        continue