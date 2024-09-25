"""
text: [{"a":"b"},{"c","d"},{"e":"f"}] output => [{"1":"2"},{"3","4"},{"5":"6"}]
"""


def fn_hack_10(s):
    
    char_map = {
        "a" : "1",
        "b" : "2",
        "c" : "3",
        "d" : "4",
        "e" : "5",
        "f" : "6"
    }
    
    result = []
    
    for item in s:
        if isinstance(item, dict):
            new_item = {}
            for key, value in item.items():
                new_item[char_map.get(key, key)] = char_map.get(value, value)
            result.append(new_item)
        else:
            new_item = []
            for i in item:
                new_item.append(char_map.get(i, i))
            result.append(tuple(new_item))
    
    return result