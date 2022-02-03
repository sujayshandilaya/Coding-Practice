class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        
        domain_dict={}
        for domains in cpdomains:
            domain=domains.split()
            rep=int(domain[0])
            domain_dict[domain[1]]=domain_dict.get(domain[1],0)+rep
            domain=domain[1].split('.')
            if len(domain)==2:
                domain_dict[domain[1]]=domain_dict.get(domain[1],0)+rep
            else:
                domain_dict[domain[2]]=domain_dict.get(domain[2],0)+rep
                sub_domain=domain[1]+'.'+ domain[2]
                domain_dict[sub_domain]=domain_dict.get(sub_domain,0)+rep
            
        output=["{} {}".format(str(v),k) for k,v in domain_dict.items()]
       #output=["%d %s" % (domain_dict[k], k) for k in domain_dict]
       #output=[f'{v} {k}' for k,v in domain_dict.items()]
        
        return output
            
                
                
                
            