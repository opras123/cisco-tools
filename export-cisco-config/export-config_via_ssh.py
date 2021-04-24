from netmiko import ConnectHandler
import os

router = {
    'device_type':'cisco_ios',
    'ip':'172.16.1.21',
    'username':'automation',
    'password':'ccna',
    'secret':'cisco'
    }

conn = ConnectHandler(**router)
try:
    enable = conn.enable()
    run_conf = conn.send_command('show running-config')
    # you can define path for saving file manually, or automatic select path
    
    #path = os.path.join(os.getcwd(), 'export-config.txt')
    path = os.path.join("C:\Python\Python37\myscipt", "export-config.txt")
    file = open(dir, "w")
    file.write(run_conf)
    print(run_conf)
    print(f"Succesfully Export Configuration, File already saved in {dir}")

except Exception as Err:
    print(Err)

