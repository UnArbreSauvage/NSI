def getDeltaTime(list):
    c = list.split("-")
    result = 0
    result += int(c[0]) * 3600
    result += int(c[1]) * 60
    result += int(c[2])
    return result
 
def Convert(list):
    h = list // 3600
    m = list // 60 % 60
    s = list % 60

    result = ""
    if int(h) < 10:result += f"0{h}:"
    else:result += f"{h}:"

    if int(m) < 10:result += f"0{m}:"
    else:result += f"{m}:"

    if int(s) < 10:result += f"0{s}"
    else:result += str(s)

    return result