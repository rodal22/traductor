traduccion= {
    "JUICIOSO":"Persona Responsable"
    "AGUACATE":"Fruta tambien conocida como PALTA"
    "ESFERO":"Tambien conocido como Boligrafo o Lapicero"
    "EH AVE MARIA PUES":"Sirve para expresar asombro"
}

word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")

if word in traduccion.keys():
    print("El significado de la palabra es: ",traduccion[word] )
    # ¿Qué debemos hacer si se encuentra la palabra?
else:
    # ¿Qué hacer si no se encuentra la palabra?
    print("Esa palabra no existe en nuestro diccionario")
