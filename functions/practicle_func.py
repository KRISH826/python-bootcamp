def convert_tempt(temp, unit):
    if unit == "C":
        return temp * 9/5 + 32
    elif unit == "F":
        return (temp-32)*5/9
    else:
        return None

print(convert_tempt(20, "C")) 

