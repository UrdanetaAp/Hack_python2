"""
generic script

a = @
e = 3
i = ¡
o = 0
u = v

text: "fooziman" output => "F00z¡m@N" 
text: "barziman" output => "B@rz¡m@N" 
text: "3q" output => "3Q" 
text: "qu" output => "Qv" 
text: "qux" output => "QvX" 
"""



def fn_hack_3(s):
    result = s
    
    char_map = {
        "a" : "@",
        "e" : "3",
        "i" : "¡",
        "o" : "0",
        "u" : "v",
        "f" : "F",
        "n" : "N",
        "b" : "B",
        "q" : "Q",
        "x" : "X"
    }
    
    new_result = []
    
    for char in s:
        if char.lower() in char_map:
            new_result.append(char_map[char.lower()])
        else:
            new_result.append(char)
    return "".join(new_result)

            
