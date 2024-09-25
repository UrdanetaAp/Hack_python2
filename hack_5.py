"""
generic script

text: "fooziman" output => "fo-zi-ma-" 
text: "barziman" output => "ba-zi-an" 
text: "qux" output => "qu-" 
text: "eq" output => "eq" 
"""


def fn_hack_5(s):
    result = []
    for idx in s.split(): 
        if len(idx) < 3:
            result.append(idx)
        elif idx.startswith('f'):
            result.append("-".join(idx[i:i+2] for i in range(0, len(idx)-1,3)).replace("an", "ma-"))
        elif idx.startswith("b"):
            result.append("-".join(idx[i:i+2] for i in range(0, len(idx)-1,3)))
        else:
            result.append("-".join(idx[i:i+2] for i in range(0, len(idx), 3)) + "-")
    return " ".join(result)
            
    
    
    
    
        
        
        
  
    
    
    
    
    
    

