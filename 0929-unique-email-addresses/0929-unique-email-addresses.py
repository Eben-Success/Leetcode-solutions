class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        
        res = set()
        
        for email in emails:
            local_name, domain_name = email.split("@")
            
            local_name = local_name.replace('.', '')
            
            if "+" in local_name:
                local_name = local_name[:local_name.index('+')]
                
            email = local_name + '@' + domain_name
            
            res.add(email)
            
        return len(res)
            
            
        