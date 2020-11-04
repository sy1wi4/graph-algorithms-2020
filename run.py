# uruchamia daną funkcję dla każdego z plików bez rozszerzenia zawartego w katalogu w którym aktualnie jesteśmy (grafy testowe)


import os
import pathlib
 

# zmienia format ścieżki windowsowej ('\' -> '/')
def fix(path):
    fixed = ''

    for sign in path :
        if sign == '\\' :
            fixed += '/'
        else:
            fixed += sign
        
    return fixed



def run(func):

    # pathlib.Path(__file__).parent.absolute()  ->  ścieżka do katalogu zawierającego ten konkretny plik

    path = fix(str(pathlib.Path(__file__).parent.absolute()))
    
    # os.listdir(path) -> zwraca listę zawierającą nazwy plików w katalogu z danej ścieżki

    for file in os.listdir(path) :

        # os.path.splitext(path) zwraca rozszerzenie pliku danego ścieżką
        print(file)
        if os.path.splitext(path + file)[1] == '' :
            # XD
            if file != '__pycache__' :  
                print(func(file),"\n")
