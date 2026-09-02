import re
class Solution:

    def encode(self, strs: List[str]) -> str:
        totalStr = ""
        for chars in strs:
            totalStr = totalStr + str(len(chars)) +"#"
            totalStr = totalStr+chars
        return totalStr

    def decode(self, s: str) -> List[str]:
        words =[]
        word = ""
        ptr = 0
        length = ""
        while ptr < len(s):
            if s[ptr] !="#":
                length+=s[ptr]
                ptr+=1
            else:
                ptr+=1
                counter = int(length)
                for index in range(counter):
                    word+=s[ptr+index]
                ptr+=counter
                words.append(word)
                length = ""
                word =""
        return words






            

