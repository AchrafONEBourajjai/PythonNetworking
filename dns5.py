#get dns records of any web site
import dns.resolver
def dnscheck(name):
    for dnstype in 'A','AAAA','CNAME','NS','MX','PTR','SRV','SOA':
        data= dns.resolver.query(name,dnstype,raise_on_no_answer=False)
        # raise_on_no_answer=False dans le cas ou il y'a une erreur
        if data.rrset is not None :
            #data.rrset mean if data are set
            print(data.rrset)
dnscheck('youtube.com')