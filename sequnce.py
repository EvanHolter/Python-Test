def MySeq(start, end):
    try:
        start = int(start)
        end = int(end)
    except:
        print("ERROR: arguments start and end must be intergers")
    SeqLength = end - start
    if start == end:
        print("ERROR: arguments start and end cannot be the same")
    elif SeqLength < 0:
        SeqLength = SeqLength * -1
    else:
        print(f"{SeqLength}")

MySeq(-1, 3)