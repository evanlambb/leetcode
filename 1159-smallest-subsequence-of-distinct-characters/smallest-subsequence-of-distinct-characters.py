class Solution:
    def smallestSubsequence(self, s: str) -> str:
        letters = dict()
        for letter in s:
            if letter not in letters:
                letters[letter] = 1
            else: 
                letters[letter] += 1
                
        ans = []
        counts = set()
        
        for letter in s:
            # 2. ONLY run the stack logic if we need to add the letter
            if letter not in counts:
                
                # Pop larger characters that appear again later
                while len(ans) > 0 and letter < ans[-1] and letters[ans[-1]] > 0:
                    counts.remove(ans[-1])
                    ans.pop()
                    
                # Now add the current letter
                ans.append(letter)
                counts.add(letter)

            letters[letter] -= 1
            
        return ''.join(ans)