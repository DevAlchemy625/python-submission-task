inFp = None
inStr=""

inFp = open("C:\Users\bee76\OneDrive\바탕 화면\상명대 1-1\파이썬 프로그래밍\제출용\python-submission-task-1\PYTHON실습\FileTest\data1.txt", "r")

inStr=inFp.readline()
print(inStr, end="")

inStr=inFp.readline()
print(inStr, end="")

inStr=inFp.readline()
print(inStr, end="")

inFp.close()