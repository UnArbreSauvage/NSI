class AttributeError(Exception):
    pass

def GetArea(cm : float,power : int):
    if power == 2 or power == 3:
        return cm**power
    else:
        raise AttributeError("Unexcepted power '" + str(power) + "', must be 2 or 3.")

print(GetArea(4,4))