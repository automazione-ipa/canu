celsius=input("Insert temperature in celsius to be converted\n")
def converter(var):
    fahrenheit=1.8*float(var)+32
    return fahrenheit

print("Celsius "+ celsius +" ---> Farhenight ",round(converter(celsius), 2))