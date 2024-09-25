"""
generic script

["1","-"] => type string
["0"] => type string

text: ["a","b","c","d","e"] output => ["1","-","3","-","5"]
text: [] output => ["0"] 
"""

def fn_hack_6(s):
    result = []
    
    if not s:
        return ["0"]
    
    for i, _ in enumerate(s, start=1):
        if i % 2 == 1:
            result.append(str(i))
        else:
            result.append("-")
     
    return result
