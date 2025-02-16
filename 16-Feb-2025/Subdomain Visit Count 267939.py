# Problem: Subdomain Visit Count - https://leetcode.com/problems/subdomain-visit-count

from collections import defaultdict
class Solution(object):
    def subdomainVisits( self,cpdomains):
        result=[]
        freq_dect=defaultdict(int)

        for cpdomain in cpdomains:
            n,domains=cpdomain.split()
            n=int(n)
            domain_lst=domains.split(".")
            domain=""

            for i in range(len(domain_lst)-1,-1,-1):

                if i == len(domain_lst)-1:
                    domain=domain_lst[-1]
                
                else:
                    domain=domain_lst[i]+"."+domain
                freq_dect[domain]+=n
        for key ,value in freq_dect.items():
            result.append(str(value)+" "+key)
        return result