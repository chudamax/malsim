import argparse, sys, time
from simulations import kraken_dga_v1, kraken_dga_v2, cobaltstrike_dns, dns_zone_transfer
from simulations.utils import make_request

#answer = request(domain="test111.pentestcnc.ru",qtype="A", server="8.8.8.8")
#print (answer.rr[0].rdata)

base_domain = 'pentestcnc.ru'
server ="8.8.8.8"
count = 10

#based on https://www.youtube.com/watch?v=zAB5G-QOyx8
def cobaltstrike_dns_tunneling_staging():
    domains = cobaltstrike_dns.get_domains_staging(count=count, domain=base_domain)
    for domain in domains:
        make_request(domain=domain, qtype="TXT", server=server)

#based on https://www.youtube.com/watch?v=zAB5G-QOyx8
def cobaltstrike_dns_tunneling_beaconing():
    domains = cobaltstrike_dns.get_domains_beaconing(count=count, domain=base_domain)
    for domain in domains:
        make_request(domain=domain, qtype="A", server=server)

#based on bin.re/blog/krakens-two-domain-generation-algorithms/
def kraken_dga():
    domains = kraken_dga_v2.get_domains(count)
    for domain in domains:
        print (domain)
        make_request(domain=domain, qtype="A", server=server)

#based on bin.re/blog/krakens-two-domain-generation-algorithms/
def kraken_ddns():
    domains = kraken_dga_v1.get_domains(count)
    for domain in domains:
        print (domain)
        make_request(domain=domain, qtype="A", server=server)

def well_known_malicious_domains():
    pass

def sinholed_domains():
    pass

def dnz_zone_transfer(domain, server):
    hosts = dns_zone_transfer.dns_zone_transfer(domain=domain, ip=server)
    print (hosts)

#dnz_zone_transfer('hpbank.local','192.168.0.167')
#cobaltstrike_dns_tunneling_staging()
#cobaltstrike_dns_tunneling_beaconing()
#kraken_ddns()
kraken_dga()
