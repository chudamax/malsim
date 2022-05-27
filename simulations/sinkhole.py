import os

#https://github.com/grettir/malware-sinkholes/blob/master/malware_sinkholes.txt

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
DOMAINS_PATH = os.path.join(CURRENT_DIR,'..\\','lists','sinholed_domains.txt')

def get_domains(count):
    with open(DOMAINS_PATH) as f:
        domains = [domain.replace('[.]','.').strip() for domain in f.readlines()][:count]

    return domains

def update_list():
    #TODO
    pass

