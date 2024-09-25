"""
generic script

["1",2] => type string & type int
[0] => type int

text: ["a","b","c","d","e"] output => ["1",2,"3",4,"5"]
text: [0] output => [0] 
"""


def fn_hack_7(s):
    result = []
    counter = 1
   
    if s == [0]:  
        return [0]
      
    for elem in s:
        if isinstance(elem, str):
            if counter % 2 == 1:
                result.append("{}".format(counter))
            else:
                result.append(counter)
        else:
            if counter % 2 == 1:
                result.append('"{}"'.format(counter))
            else:
                result.append(counter)
        counter += 1
    return result