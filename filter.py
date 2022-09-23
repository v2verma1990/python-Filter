import sys
import logging
def slash_access(obj, keys):
    keys = keys.split("/")
    current = obj
    for key in keys:
        current = current[key]
    return current

my_object = {"a":{"b":{"c":"d"}}}

try:
    result =slash_access(my_object, "a/b")
    print(result) 
except BaseException:
    logging.exception("Incorrect key")
