#4주차 제출과제 입력 수식 계산, 두 수 사이의 총합 계산

select=int(input("사용할 형식을 고르세요(1번, 2번) : "))

total=0

if select==1:
    a=input("*** 수식을 입력하세요 : ")

    result=eval(a)
    print(a, "결과는", result, "입니다.")
elif select==2:
    b=int(input("*** 첫 번째 숫자를 입력하세요 : "))
    c=int(input("*** 두 번째 숫자를 입력하세요 : "))

    for i in range(b,c+1):
        total=total+i
    print(b,"+...+",c,"는",total,"입니다.")
else:
    print("등록 된 형식을 고르세요.")

    