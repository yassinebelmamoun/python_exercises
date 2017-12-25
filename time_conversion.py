import re

# INPUT
x = "02:05:45PM" 


pattern = "([01][012]|[1-9]):([0-5][0-9]):([0-5][0-9])(AM|PM)"

def compile_military_time(h, m, s, period):
    if period == 'AM':
        return h + ':' + m + ':' + s
    else:
        return str(12+int(h)) + ':' + m + ':' + s

if re.match(pattern, x): 
    h = re.match(pattern,x).group(1)
    m = re.match(pattern,x).group(2)
    s = re.match(pattern,x).group(3)
    period = re.match(pattern,x).group(4)
    military_time = compile_military_time(h, m, s, period)
    print(military_time)
else:
    print('Format of Time is not readable, please use: HH:MM:SSAM or HH:MM:SSPM format')

