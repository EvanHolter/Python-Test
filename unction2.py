#UncStatus = [
#    {"age": "1", "text": "IT'S ALREADY OVER"},
#    {"age": "4", "text": "I DUNNO KID"},
#    {"age": "5", "text": "YOU'RE GETTING UP THERE"}
#]

UncStatus = {
    1: "IT'S ALREADY OVER",
    2: "I DUNNO KID",
    3: "YOU'RE GETTING UP THERE",
}

while True:
    try:
        UserAge = int(input("How old are you? "))
        break
    except ValueError:
        print("THAT IS NOT YOUR FUCKING AGE")

try:
    print(UncStatus[UserAge])
except:
    print("THAT IS SO OLD YOU AREN'T EVEN UNC ANYMORE!")