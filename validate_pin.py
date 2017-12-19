# def validate_pin(pin):
#     int(pin)
#     if not isinstance(pin, int):
#         print(False)
#     elif not len(str(pin)) == 4 or len(str(pin)) == 6:
#         print(False)
#     else:
#         print(True)

#  right answer below 

def validate_pin(pin):
    try:
        int(pin)
    except:
        return False 
    if len(pin) == 4 or len(pin) == 6:
        return True
    else:
        return False

def validate_pin(pin):
  return re.search('^(\d{4}|\d{6})$', pin) != None
