import time
import webbrowser
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from comtypes import CLSCTX_ALL

def get_volume():
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = interface.QueryInterface(IAudioEndpointVolume)
    current_volume = volume.GetMasterVolumeLevelScalar() * 100
    return current_volume

def main():
    print("Olá aniversáriante para poder prosseguir, aumente o volume do computador para 50% ou mais e aguarde")
    time.sleep(8)
    while True:
        volume = int(get_volume())
        print(f"Volume: {volume}")
        if volume >= 50:  # Verifica se o volume está acima de 50%
            webbrowser.open("https://presente-zuzb.onrender.com")
            break
        time.sleep(1)

if __name__ == "__main__":
    main()