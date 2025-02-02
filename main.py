meme_dict ={ "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "ezz": "muy facil",
            "damn": "expresion de sorpresa"}
           

pregunta=input("ingrese una palabra: ")

for palabra in meme_dict.keys():
    if pregunta == palabra:
         print(f"El signifcado de la palabra {pregunta} es {meme_dict[palabra]}")