# 하나만 출력합니다.
print("# 하나만 출력합니다.")
print("Hello Python Programing...!")
print()

# 여러 개를 출력합니다.
print("# 여러 개를 출력합니다.")
print(10, 20, 30, 40, 50)
print("안녕하세요", "저의", "이름은", "윤인성입니다!")
print()

# 아무 것도 입력하지 않으면 단순하게 줄바꿈합니다.
print("# 아무 것도 출력하지 않습니다.")
print("--- 확인 전용선 ---")
print()
print()
print("--- 확인 전용선 ---")

# 이스케이프 예제
print("이름\t나이\t지역")
print("윤인성\t25\t강서구\n")

#문자열 반복 연산자
print("안녕하세요"*3)

#문자열 선택 연산자
print("# 문자 선택 연산자")
print("안녕하세요"[0])
print("안녕하세요"[1])
print("안녕하세요"[2])
print("안녕하세요"[3])
print("안녕하세요"[4])

#input 함수와 float 함수의 조합
input_a=float(input("첫 번째 숫자> "))
input_b=float(input("두 번째 숫자> "))

print("덧셈 결과:", input_a + input_b)
print("뺄셈 결과:", input_a - input_b)
print("곱셈 결과:", input_a * input_b)
print("나눗셈 결과:", input_a / input_b) 