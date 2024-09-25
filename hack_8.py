"""
generic script

text: ["a","b","c","d","e"] output => ["e-5","d-4","c-3","b-2","a-1"]
text: ["a","b","c"] output => ["c-3","b-2","a-1"]
text: ["a","b","c","d"] output => ["4","3","2","1"]
text: ["a","b"] output => ["2","1"]
"""


def fn_hack_8(s):
    result = []
    
    if len(s) % 2 == 0:
        for i in range(len(s),0,-1):
            result.append(str(i))
    else:
        for i, element in enumerate(s, start=1):
            result.append(f"{element}-{i}")
        result.reverse()
    return result  
            
           

        
        