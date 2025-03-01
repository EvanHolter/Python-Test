# def unction(age):
#    if age > 25:
#        print("YOU'RE UNC")
#    else:
#        print("YOU ARE NOT UNC")

def unction(age):
    if age < 5:
        print("YOU'RE A KID")
    elif age < 16:
        print("YOU ARE IN YOUR PRIME")
    elif age < 25:
        print("YOU ARE NOW UNC!")
    elif age < 40:
        print("YOU ARE  UNC")
    elif age < 55:
        print("FIRE UP THE UNC ALARM!!")
    else:
        print("OHH THE UNCTION IS GOING ON")

#def unction(age):
#    match age:
#        case 1|2|3|4|5|6:
#            print("Young")
#        case 7|8|9|10:
#            print("Let him cook")

    
while True:
    try:
        UserAge = int(input("How old are you? "))
        break
    except ValueError:
        pass
        print("THAT IS NOT YOUR FUCKING AGE")
    #else:
    #    break

unction(age=UserAge)