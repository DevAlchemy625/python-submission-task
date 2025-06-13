inFp = None
inList, inStr = [], ""

inFp = open("C:/Temp/data1.txt", "r")

inList = inFp.readlines()

lineNum = 1  # 줄 번호 변수

for inStr in inList:
    print("%d: %s" % (lineNum, inStr), end="")  # 줄 번호와 내용 출력
    lineNum += 1

inFp.close()
