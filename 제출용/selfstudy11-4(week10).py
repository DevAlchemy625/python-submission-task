inFp, outFp = None, None
inStr = ""

# 사용자로부터 파일명 입력받기
srcName = input("소스 파일명을 입력하세요: ")
dstName = input("타깃 파일명을 입력하세요: ")

inFp = open(srcName, "r")
outFp = open(dstName, "w")

inList = inFp.readlines()
for inStr in inList:
    outFp.writelines(inStr)

inFp.close()
outFp.close()
print("--- %s 파일이 %s 파일로 복사되었음 ---" % (srcName, dstName))
