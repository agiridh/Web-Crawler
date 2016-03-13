from urllib.parse import urlparse

## This file will extract the domain name from a url

# Get domain name(example.com)
def get_domain_name(url):
    try:
        domain = get_sub_domain_name(url).split('.')
        # no matter what the subdomain is, the domain name will always lie in the
        # last two elements of domain list
        return domain[-2] + '.' + domain[-1]
    except:
        return ''

# Get subdomain name (name.example.com)
def get_sub_domain_name(url):

    try:
        return urlparse(url).netloc
    except:
        return ''