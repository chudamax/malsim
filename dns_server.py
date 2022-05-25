import argparse, sys, time

#https://github.com/paulc/dnslib
from dnslib import RR,QTYPE, RCODE, TXT, A, parse_time
from dnslib.label import DNSLabel
from dnslib.server import DNSServer, DNSHandler, BaseResolver, DNSLogger

from io import StringIO, BytesIO
from io import BytesIO


class Resolver(BaseResolver):

    def __init__(self, origin, ttl):
        self.origin = DNSLabel(origin)
        self.ttl = parse_time(ttl)
        self.clients = {}

    def reply_to_client(self, request):
        reply = request.reply()
        qname = request.q.qname

        print ("1", qname)

    def resolve(self, request, handler):        
        reply = request.reply()
        qname = request.q.qname

        print ("2", qname)


if __name__ == '__main__':

    p = argparse.ArgumentParser(description="Malsim Client")
    p.add_argument("--origin","-o",default=".",metavar="<origin>", help="Origin domain label (default: .)")
    p.add_argument("--ttl","-t",default="60s", metavar="<ttl>", help="Response TTL (default: 60s)")
    p.add_argument("--port","-p",type=int,default=53, metavar="<port>", help="Server port (default:53)")
    p.add_argument("--address","-a",default="", metavar="<address>", help="Listen address (default:all)")
    p.add_argument("--udplen","-u",type=int,default=0, metavar="<udplen>", help="Max UDP packet length (default:0)")
    p.add_argument("--log", default="request,reply,truncated,error", help="Log hooks to enable (default: +request,+reply,+truncated,+error,-recv,-send,-data)")
    p.add_argument("--log-prefix", action='store_true',default=False, help="Log prefix (timestamp/handler/resolver) (default: False)")
    args = p.parse_args()

    resolver = Resolver(args.origin, args.ttl)
    logger = DNSLogger(args.log, args.log_prefix)
    

    if args.udplen:
        DNSHandler.udplen = args.udplen

    udp_server = DNSServer(resolver, port=args.port, address=args.address, logger=logger)
    udp_server.start_thread()

    print("Starting Malsim DNS Resolver (%s:%d) [%s]" % (args.address or "*", args.port, "UDP"))

    while udp_server.isAlive():
        time.sleep(1)
