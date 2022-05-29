from netmiko import ConnectHandler
import os
import re

listip = ["172.23.0.242"]
# sample multiple ip ["172.12.1.1","172.10.12.1"]

for ip in listip:
    print(ip)
    router = {
        'device_type':'cisco_ios',
        'ip':ip,
        'username':'automation',
        'password':'automation',
        'secret':'cisco'
        }

    conn = ConnectHandler(**router)
    try:
        enable = conn.enable()
        print("Succesfully Connect")
        run_conf = conn.send_command('show running-config')
        # you can define path for saving file manually, or automatic select path
        hostname = re.search("hostname(.*)\s",run_conf).group(0).split(" ")
        namefile = ("exp_cfg-{}.txt".format(hostname[1].replace("\n","")))
        #path = os.path.join(os.getcwd(), namefile)
        path = os.path.join(".\data", namefile)
        file = open(path, "w")
        file.write(run_conf)
        print(f"Succesfully Export Configuration, File already saved in {path}")
    except Exception as Err:
        print(Err)

