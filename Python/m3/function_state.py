addresslist = ["3022 Broadway, New York, NY 10027, USA" ,
 "3021 Broadway, Chicago , IL 20001, USA",
 "3727 Ullamcorper, Roseville, NH 11523"]

def get_state(address):
    state = address.split(', ')[2].split()[0]
    return state

for address in addresslist:
    print(get_state(address))
