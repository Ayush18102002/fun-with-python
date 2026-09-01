import subprocess

profiles subprocess.check_output("netsh wlan show profil shell=True).decode()

names = [line.split(":")[1].strip()

for line in profiles.split("\n") if "All User Profile" in 1437]

for i, name in enumerate (names, 1):

print(f"[it}] {name}")

ch= int(input("\nChoose WiFi number: "))

wifi names [ch - 1]

result = subprocess.check_output(

f"netsh wlan show profile \"{wifi}\" key=clear", shell=True).decode()

print(f"\nPassword: {result.split(' ') [1].strip()}")