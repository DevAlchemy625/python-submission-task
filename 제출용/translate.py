# 입력값 진법 변환 프로그램

#입력 진수 결정정
translate = int(input("입력 진수 결정(16/10/8/2) : "))

#값 입력
value = input("값 입력 : ")

#값 진수 변환
A = int(value, translate)

#값 출력
print("16진수 ==>", hex(A))
print("10진수 ==>", A)
print("8진수 ==>", oct(A))
print("2진수 ==>", bin(A))