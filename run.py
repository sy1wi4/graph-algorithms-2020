# uruchamia daną funkcję dla każdego z plików bez rozszerzenia zawartego w katalogu w którym aktualnie jesteśmy (grafy testowe)


import os
import pathlib
import datetime
import dimacs
from colorama import Fore, Style

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

        # os.path.splitext(path) zwsraca rozszerzenie pliku danego ścieżką
      
        if os.path.splitext(path + file)[1] == '' :

            if file != '__pycache__' : 
                print(file) 

                start = datetime.datetime.now()
                expected = dimacs.loadDirectedWeightedGraph(file)[0]
                actual = func(file)

                duration = datetime.datetime.now() - start
                print("expected:", expected)
                print("actual:", actual)
                
                if expected != actual:
                    print(Fore.RED + 'ERROR')
                    print(Style.RESET_ALL)
                else:
                    print(Fore.GREEN + 'OK!')
                    print(Style.RESET_ALL)
                print("duration:",duration, "\n")
