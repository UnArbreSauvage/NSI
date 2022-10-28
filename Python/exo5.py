def GetDeltaTime(time):
    b = time.split("-")
    result = 0
    result += int(b[0]) * 3600
    result += int(b[1]) * 60
    result += int(b[2])
    return result