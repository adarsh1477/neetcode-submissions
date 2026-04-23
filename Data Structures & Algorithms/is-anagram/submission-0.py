class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
      check1={}
      for i in s:
        if i in check1:
            check1[i]=check1[i]+1
        else:
            check1[i]=1
      check2={}
      for j in t:
        if j in check2:
            check2[j]=check2[j]+1
        else:
            check2[j]=1

      if check1==check2:
            return True
      return False
        
        