import os
import psutil

def Port_8000():
    if '8000' in os.popen('netstat -tulpn | grep :8000').read():
        return True
    else:
        return False





def Port_3000():
    if '3000' in os.popen('netstat -tulpn | grep :3000').read():
        return True
    else:
        return False

def Postgresql_Status():
    if 'inactive' in os.popen('systemctl status postgresql.service').read():
        return False
    else:
        return True

def Apache2_Status():
    if os.popen('systemctl status apache2').read():
        return True
    else:
        return False

def Last_Root():
    return os.popen('last root').read()



def Server():
    data = {
        'port_8000' : Port_8000(),
        'port_3000' : Port_3000(),
        'Postgres_Status' : Postgresql_Status(),
        'Apache2_Status' : Apache2_Status(),
        'Last_Root' : Last_Root(),
        'The CPU usage is' : psutil.cpu_percent(4),
        'RAM Used (GB)' : psutil.virtual_memory()[3]/1000000000,

    }
    return data

print(Server())
