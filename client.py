import argparse, sys, time
from simulations import kraken_dga_v1, kraken_dga_v2, cobaltstrike_dns

#https://github.com/paulc/dnslib
try:
    from dnslib import *
    from dnslib.label import DNSLabel
    from dnslib.server import DNSServer, DNSHandler, BaseResolver, DNSLogger
    from dnslib.digparser import DigParser
except ImportError:
    print("Missing dependency dnslib: <https://pypi.python.org/pypi/dnslib>. Please install it with `pip`.")
    sys.exit(2)

def make_request(domain, qtype="A", server="8.8.8.8"):
    q = DNSRecord(q=DNSQuestion(domain,getattr(QTYPE,qtype)))
    a_pkt = q.send(server,53)
    a = DNSRecord.parse(a_pkt)
    return a

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
        make_request(domain=domain, qtype="A", server=server)

#based on bin.re/blog/krakens-two-domain-generation-algorithms/
def kraken_ddns():
    domains = kraken_dga_v1.get_domains(count)
    for domain in domains:
        make_request(domain=domain, qtype="A", server=server)

def well_known_malicious_domains():
    pass

def sinholed_domains():
    pass

def dnz_zone_transfer():
    pass


cobaltstrike_dns_tunneling_staging()
cobaltstrike_dns_tunneling_beaconing()


#kraken_ddns()
#kraken_dga()