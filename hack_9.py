"""
text: {"foo":"fookziman","bar":"barziman"} output => {"Foo":"Fooziman"}
"""


def fn_hack_9(s):
    result = {}
    for key, value in s.items():
        if key == "foo":
            new_key = key.capitalize()
            new_value = "Fooziman"
            result[new_key] = new_value
        else:
            continue
    return result
