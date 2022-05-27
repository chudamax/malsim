import dns.zone
import dns.resolver

def dns_zone_transfer(domain, ip):
    try:
        zone = dns.zone.from_xfr(dns.query.xfr(str(ip),domain))
        hosts = [host for host in zone]
        return hosts
    except:
        return