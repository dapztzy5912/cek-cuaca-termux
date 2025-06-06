import requests
import time
from colorama import Fore, Style, init

init(autoreset=True)

def banner():
    print(Fore.CYAN + """
╔═╗┌─┐┌─┐┬┌─┌─┐   ╔═╗┬ ┬┌─┐┌┬┐┌─┐
╚═╗├─┘├─┤├┴┐│ │───╠╣ ├─┤├─┤ │ ├┤ 
╚═╝┴  ┴ ┴┴ ┴└─┘   ╚  ┴ ┴┴ ┴ ┴ └─┘
        """)
    print(Fore.YELLOW + "            by @XdpzQ | wttr.in API\n")

def loading():
    print(Fore.GREEN + "🔍 Mengambil data cuaca", end="")
    for _ in range(3):
        print(".", end="", flush=True)
        time.sleep(0.5)
    print()

def get_weather(city):
    try:
        url = f"https://wttr.in/{city}?format=3"
        response = requests.get(url)
        print(Fore.LIGHTMAGENTA_EX + "📍 Cuaca di", Fore.CYAN + city.title())
        print(Fore.LIGHTYELLOW_EX + "🌤️", response.text)
    except Exception as e:
        print(Fore.RED + "Gagal mengambil data cuaca:", e)

if __name__ == "__main__":
    banner()
    kota = input(Fore.LIGHTGREEN_EX + "📌 Masukkan nama kota: ")
    loading()
    get_weather(kota)
    print(Fore.LIGHTBLUE_EX + "\n📡 Data diambil dari wttr.in — Simple Weather API\n")
