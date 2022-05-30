import os


CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
DOMAINS_PATH = os.path.join(CURRENT_DIR,'..\\','lists','subdomains-top1mil-5000.txt')


def get_domains(base_domain, count):
    with open(DOMAINS_PATH) as f:
        domains = ['{}.{}'.format(domain.strip(), base_domain) for domain in f.readlines()][:count]

    return domains