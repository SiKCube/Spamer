import pyautogui
import time

try: 
    print("\nModo texto (repite el texto que quieras) -> 0")
    print("Modo pegar (pega lo que copiaste antes) -> 1\n")
    mode = str(input("Que modo de spam usar? (selecciona con numero): "))

    if mode == "0":
        print("Seleccionaste Texto")
        limit = int(input("Cuantos mensajes a enviar?: "))

        calldown = float(input("Tiempo a esperar entre mensajes: "))

        msg = str(input("Mensaje a spamear: "))

        input("Preciona cualquier tecla en 10 segundos para seleccionar el input de texto a spamear")

        _i = 0

        for _x in range(10):
            time.sleep(1)

        while _i < limit:
            pyautogui.typewrite(msg)
            time.sleep(calldown)
            pyautogui.press("Enter")

            _i += 1

    elif mode == "1":
        print("Seleccionaste Pegar")
        limit = int(input("Cuantos mensajes a enviar?: "))

        calldown = float(input("Tiempo a esperar entre mensajes: "))

        input("Al precionar cualquier tecla entras 10 segundos para seleccionar un input de texto y tendras q copiar la imagen a spamear")

        _i = 0

        for _x in range(10):
            time.sleep(1)

        while _i < limit:
            pyautogui.hotkey("ctrl", "v")
            time.sleep(calldown)
            pyautogui.press("Enter")

            _i += 1

    else:
        print("No existe el comando")


except Exception as ex:
    input("Hubo un Error")
