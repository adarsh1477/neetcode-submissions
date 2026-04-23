class Solution:
    def isHappy(self, n: int) -> bool:
        seen=set()
        def happy(n):
            total=0
            while n!=0:
                digit=n%10
                total=total+(digit*digit)
                n=n//10
           
            if total==1:
                return True
            elif total not in seen:
                seen.add(total)
                return happy(total)
            else:
                return False
        
        return happy(n)
            
            
        
      
            



