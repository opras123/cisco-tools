from netmiko import ConnectHandler
import os
import re

listip = ["172.20.1.246","172.20.1.245"]

for ip in listip:
    print(ip)
    router = {
        'device_type':'cisco_ios',
        'ip':ip,
        'username':'automation',
        'password':'test',
        'secret':'cisco'
        }

    conn = ConnectHandler(**router)
    try:
        enable = conn.enable()
        print("Succesfully Connect")
        run_conf = conn.send_command('show running-config')
        # you can define path for saving file manually, or automatic select path
    
        #path = os.path.join(os.getcwd(), 'export.txt')
        hostname = re.search("hostname(.*)\s",run_conf).group(0).split(" ")
        namefile = ("exp_cfg-{}.txt".format(hostname[1].replace("\n","")))
        print (namefile)
        path = os.path.join("C:\Python\Python37\myscipt", namefile)
        file = open(path, "w")
        file.write(run_conf)
        print(f"Succesfully Export Configuration, File already saved in {dir}")

    except Exception as Err:
        print(Err)

