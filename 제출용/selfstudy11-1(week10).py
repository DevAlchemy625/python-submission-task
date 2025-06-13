inFp = None
inStr = ""
lineNum = 1  # 줄 번호를 위한 변수 추가

inFp = open("C:/Temp/data1.txt", "r")

while True:
    inStr = inFp.readline()
    if inStr == "":
        break
    print("%d: %s" % (lineNum, inStr), end="")  # 줄 번호와 함께 출력
    lineNum += 1  # 줄 번호 증가

inFp.close()
