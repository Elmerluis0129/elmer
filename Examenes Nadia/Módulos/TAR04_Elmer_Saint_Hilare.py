"""
Escriba un programa que permita crear una lista de palabras y que, a continuación, pida una palabra y diga cuántas veces aparece esa palabra en la lista.
Elmer Saint-Hilare 21/1354
"""
from emoji import emojize as em # Esto no es parte del ejercicio, es decoración.

def programa4 (): # Esta linea no es parte del ejercicio, es del examen.
#Declaro mis variables a utilizar.
    Lista = []#Aquí se almacenan todos los elementos que el usuario más adelante va a proporcionar.
    x = 1 #Aquí es para poder cambiar el mandato en el bucle for.

    print("""
*--------------------------------------------*
|Ingresar las 5 palabras para crear la lista.|
*--------------------------------------------*
\n""")#Decorando la intrucción.

#Bucle for para hacer las iteraciones necesarias para crear la lista, en este caso 5 veces.
    for n in range(5):
        #Aquí para saber qué mandato le va a dar al usuario dependiendo de qué valor tenga x en dicho momento.
        if x == 1: #Aquí para la primera iteración tendrá un valor de 1 la x, por lo que le pondrá el 1er mandato.
            Lista.append(input("Ingresar la primera palabra para la lista: "))
        elif x == 2: #Aquí para la segunda iteración tendrá un valor de 2 la x, por lo que le pondrá el 2do mandato.
            Lista.append(input("Ingresar la segunda palabra para la lista: "))
        elif x == 3: #Aquí para la tercera iteración tendrá un valor de 3 la x, por lo que le pondrá el 2do mandato.
            Lista.append(input("Ingresar la tercera palabra para la lista: "))
        elif x == 4: #Aquí para la cuarta iteración tendrá un valor de 4 la x, por lo que le pondrá el 2do mandato.
            Lista.append(input("Ingresar la cuarta palabra para la lista: "))
        elif x == 5: #Aquí para la quinta iteración tendrá un valor de 5 la x, por lo que le pondrá el 2do mandato.
            Lista.append(input("Ingresar la quinta palabra para la lista: "))
            break #Esto sirve para cuanddo vaya por la 5ta iteración y se cumpla la condición el bucle for se rompa, terminando por completo con las iteraciones.
        x = x+1 #Este es la magia del bucle, aquí la variable x irá aumentando su valor de 1 en 1, por lo que es lo que ayuda a que cada condición se vaya cumpliendo según aumente el valor de x.
        
    #Aquí creo las variables que me van a contener tanto la entrada por teclado del usuario, como las veces que aparece la palabra.
    buscarPalabra = input("\nEscriba la palabra que desea buscar: ") #Aqui para saber que palabra desea buscar en la lista.
    VecesPalabraAparece = Lista.count(buscarPalabra) #Para saber si la palabra aparece o no y cuantas veces en caso de sí.
    
    #Aquí uso estas condiciones para saber qué cantidad de veces aparece la palabra, y poder varíar la respuesta, tipo: una vez o tantas veces. o no aparece.
    if VecesPalabraAparece > 1:
        print("\nLa palabra: ","'"+str(buscarPalabra)+"'", "aparece",VecesPalabraAparece, "veces en la lista.") #Aquí si aparece más de 1 vez, usará "Veces".
    elif VecesPalabraAparece == 1:
        print("\nLa palabra: ","'"+str(buscarPalabra)+"'", "aparece",VecesPalabraAparece, "vez en la lista.") #Aquí si aparece 1 sola vez, usará "Vez".
    elif not buscarPalabra in Lista:
        print("\nLa palabra: ","'"+str(buscarPalabra)+"'", "no aparece en la lista que haz creado anteriormente.")  #Aquí si no aparece la palabra se lo especifica.
    
    #========================== Agradecimiento por usar el programa =========================#  
    
    """
    Aquí imprimo por pantalla el agradecimiento y por quién fue creado, en este caso por mi.
    """
    
    print(em("""
*-----------------------------------------*
|  ¡Programa 4 Finalizado exitosamente! :smiling_face_with_smiling_eyes:|
*-----------------------------------------*
"""))
#========================== Fin Agradecimiento por usar el programa =========================#