main = {
    "me": "mine",
    "you": "yours",
    "him": "his"
}
mank = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three"
}
mark = ["we", "was", "wonk", "wallow"]


# print(main["me"])
# for i in [0, 1, 2, 3]:
#     print(mank[i])
for i in range(2):
    try:
        print(mark[i])
    except:
        print("NO MORE")
        break
