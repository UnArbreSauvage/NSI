def GetTime(time):
    h = time // 3600
    m = time // 60 % 60
    s = time % 60
    return (h,m,s)

def Format(h,m,s):
    result = ""
    if int(h) < 10:result += f"0{h}:"
    else:result += f"{h}:"

    if int(m) < 10:result += f"0{m}:"
    else:result += f"{m}:"

    if int(s) < 10:result += f"0{s}"
    else:result += str(s)

    return result