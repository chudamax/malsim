import argparse, sys, time

from simulations import kraken_dga_v1, kraken_dga_v2, cobaltstrike_dns, dns_zone_transfer, well_known_ioc, sinkhole
from utils.dns_utils import make_request, get_default_resolver

#based on https://www.youtube.com/watch?v=zAB5G-QOyx8
def cobaltstrike_dns_tunneling_staging(dns_server, base_domain, count):
    print ('\nUnitTest: Cobaltstrike DNS-tunneling staging')
    domains = cobaltstrike_dns.get_domains_staging(count=count, domain=base_domain)
    for domain in domains:
        resp = make_request(domain=domain, qtype="TXT", server=dns_server)
        print ('Resolver: {}, Query:[TXT]: {}, Response:{}'.format(dns_server, domain, resp.rr))
    print ('Done')

#based on https://www.youtube.com/watch?v=zAB5G-QOyx8
def cobaltstrike_dns_tunneling_beaconing(dns_server, base_domain, count):
    print ('\nUnitTest: Cobaltstrike DNS-tunneling beaconing')
    domains = cobaltstrike_dns.get_domains_beaconing(count=count, domain=base_domain)
    for domain in domains:
        resp = make_request(domain=domain, qtype="A", server=dns_server)
        print ('Resolver: {}, Query:[A]: {}, Response:{}'.format(dns_server, domain, resp.rr))
    print ('Done')

#based on bin.re/blog/krakens-two-domain-generation-algorithms/
def kraken_dga(dns_server, count):
    print ('\nUnitTest: Kraken pure DGA')
    domains = kraken_dga_v2.get_domains(count)
    for domain in domains:
        resp = make_request(domain=domain, qtype="A", server=dns_server)
        print ('Resolver: {}, Query:[A]: {}, Response:{}'.format(dns_server, domain, resp.rr))
    print ('Done')

#based on bin.re/blog/krakens-two-domain-generation-algorithms/
def kraken_ddns(dns_server, count):
    print ('\nUnitTest: Kraken DGA + DDNS')
    domains = kraken_dga_v1.get_domains(count)
    for domain in domains:
        resp = make_request(domain=domain, qtype="A", server=dns_server)
        print ('Resolver: {}, Query:[A]: {}, Response:{}'.format(dns_server, domain, resp.rr))
    print ('Done')

def well_known_malicious_domains(dns_server, count):
    print ('\nUnitTest: Well-known malicious domains')
    domains = well_known_ioc.get_domains(count)
    for domain in domains:
        resp = make_request(domain=domain, qtype="A", server=dns_server)
        print ('Resolver: {}, Query:[A]: {}, Response:{}'.format(dns_server, domain, resp.rr))
    print ('Done')

def sinholed_domains(dns_server, count):
    print ('\nUnitTest: Sinkcoled domains')
    domains = sinkhole.get_domains(count)
    for domain in domains:
        resp = make_request(domain=domain, qtype="A", server=dns_server)
        print ('Resolver: {}, Query:[A]: {}, Response:{}'.format(dns_server, domain, resp.rr))
    print ('Done')

def dnz_zone_transfer(dns_server, domain):
    print ('\nUnitTest: DNS Zone Transfer')
    hosts = dns_zone_transfer.dns_zone_transfer(domain=domain, ip=dns_server)
    if not hosts:
        print ('Resolver: {}. DNZ Zone Transfer failed'.format(dns_server))
    else:
        print ('Resolver: {}, Response:{}'.format(dns_server, hosts))
    print ('Done')

def parser_error(errmsg):
    print("Usage: python3 " + sys.argv[0] + " [Options] use -h for help")
    print("Error: " + errmsg)
    sys.exit()

def parse_args():
    # parse the arguments
    parser = argparse.ArgumentParser(epilog='\tExample: \r\npython3 ' + sys.argv[0] + " -m cobaltstrike_dns_tunneling_staging -c 10 -d unittest.com -s dns1.corp.local")
    parser.error = parser_error
    parser._optionals.title = "OPTIONS"
    parser.add_argument('-m', '--module', help="module to run", required=True)
    parser.add_argument('-c', '--count', help="amount of domains to generate", type=int, default=10)
    parser.add_argument('-d', '--domain', help="domain", default="use-case-test.com")
    parser.add_argument('-r', '--resolver', help="dns resolver/server")

    return parser.parse_args()
    
def main():
    args = parse_args()
    dns_server = args.resolver
    if not dns_server:
        dns_server = get_default_resolver()

    if args.module in ['cobaltstrike_dns_tunneling_staging', 'all']:
        cobaltstrike_dns_tunneling_staging(dns_server=dns_server, base_domain=args.domain, count=args.count)
    
    if args.module in ['cobaltstrike_dns_tunneling_beaconing', 'all']:
        cobaltstrike_dns_tunneling_beaconing(dns_server=dns_server, base_domain=args.domain, count=args.count)

    if args.module in ['kraken_dga', 'all']:
        kraken_dga(dns_server=dns_server, count=args.count)

    if args.module in ['kraken_ddns', 'all']:
        kraken_ddns(dns_server=dns_server, count=args.count)

    if args.module in ['well_known_malicious_domains', 'all']:
        well_known_malicious_domains(dns_server=dns_server, count=args.count)

    if args.module in ['sinholed_domains', 'all']:
        sinholed_domains(dns_server=dns_server, count=args.count)

    if args.module in ['dnz_zone_transfer', 'all']:
        dnz_zone_transfer(dns_server=dns_server, domain=args.domain)


if __name__ == '__main__':
    main()

#dnz_zone_transfer('hpbank.local','192.168.0.167')
#cobaltstrike_dns_tunneling_staging()
#cobaltstrike_dns_tunneling_beaconing()
#kraken_ddns()
#kraken_dga()
