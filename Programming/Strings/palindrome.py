class Solution:
    
    def isPalindrome(self, A):
        
        start = 0
        end = len(A) - 1
        
        while start < end:
            
            if not A[start].isalnum():
                start += 1
                continue
            if not A[end].isalnum():
                end -= 1
                continue
            if A[start].lower() != A[end].lower():
                return 0
            
            start += 1
            end -= 1
        
        return 1
    
    
if __name__ == '__main__':
    
    S = Solution()
    A = "A man, a plan, a canal: Panama"
    B = "race a car"
    C = '....,,,,,,/,.;./,.,/]\][\[;;l'
    
    print(S.isPalindrome(A))
    print(S.isPalindrome(B))
    print(S.isPalindrome(C))