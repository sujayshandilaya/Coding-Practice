class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        email_set=set()
        def emailGenerator(email:str) ->str:
            name=email.split('@')
            local_name=name[0].split('+')
            email_name=local_name[0].replace('.','')
            return(email_name+'@'+name[1])
            
            
        
        for i in range(len(emails)):
            email=emailGenerator(emails[i])
            email_set.add(email)
        
        return(len(email_set))
                
            