
import random
import secrets
import string

#aaa.stage.9712556.domain.com
#aab.stage.9712556.domain.com
def get_domains_staging(count, domain):
    domains = []

    rand_hex = secrets.token_hex(16)
    rand_int = random.randint(1000000,9999999)
    domains.append('post.1.{}.{}'.format(rand_hex, domain))

    for c1 in string.ascii_lowercase:
        for c2 in string.ascii_lowercase:
            for c3 in string.ascii_lowercase:
                if len(domains) > count:
                    return domains
                domains.append('{}{}{}.stage.{}.{}'.format(c1,c2,c3,rand_int,domain))

    return domains

#post.randomchars(hex).randomchars(hex).domain.com
def get_domains_beaconing(count, domain):
    domains = []
    for i in range(count):
        new_domain = 'post.{}.{}.{}'.format(secrets.token_hex(31),secrets.token_hex(31),domain)
        domains.append(new_domain)

    return domains
