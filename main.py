import shutil
import pyautogui

def copiaraquivo():

    #COPIANDO ARQUIVO E JÁ RENOMEANDO

    origem = r"C:\Users\User\Desktop\BACK UP.txt"

    destino = r"C:\Users\User\Downloads\NOVO PY.txt"

    try:

        shutil.copy(origem, destino )

    except Exception as E:

        print(f"Erro {E}")




pyautogui.moveTo(5000, 5000)
