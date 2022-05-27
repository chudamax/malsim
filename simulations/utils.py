import argparse, sys, time
from simulations import kraken_dga_v1, kraken_dga_v2

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