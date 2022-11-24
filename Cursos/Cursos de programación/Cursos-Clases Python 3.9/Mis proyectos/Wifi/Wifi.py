import subprocess

data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8', errors="backslashreplace").split('\n')
profiles = [i.split(":")[1][1:-1] for i in data if "Perfil de todos los usuarios     : " in i]
for i in profiles:
    try:
        results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8', errors="backslashreplace").split('\n')
        results = [b.split(":")[1][1:-1] for b in results if "Contenido de la clave  : " in b]
        try:
            print("Información de Red \n")
            print ("Name: {:<30}\nPass: {:<}".format(i, results[0]))
        except IndexError:
            print ("Wifi: {:<30}\nPassword: {:<}".format(i, ""))
    except subprocess.CalledProcessError:
        print ("{:<30}|  {:<}".format(i, "ENCODING ERROR"))


input("\nPresiona Enter para salir...\n>")
exit()