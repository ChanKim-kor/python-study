while True:
    try:
        output_power = float(input("Please enter the output power in [kW]: "))
        input_power = float(input("Please enter the input power in [kW]: "))

        print(f"Efficiency: {output_power/input_power * 100:.2f}%")
        break
    
    except ValueError:
        print("Please enter a valid value. Try again.")

    except ZeroDivisionError:
        print("Input power cannot be ZERO. Try again.")

        # [복습 포인트]
#
# 1. while True는 break가 실행될 때까지 계속 반복한다.
#
# 2. try를 while 안에 두면
#    예외 발생 → except 실행 → 다음 반복에서 다시 입력
#    구조를 만들 수 있다.
#
# 3. break는 가장 가까운 반복문을 즉시 종료한다.
#
# 4. 정상적인 입력과 계산이 모두 끝난 뒤에 break를 두면,
#    오류가 발생한 경우에는 break까지 도달하지 못하므로 다시 반복한다.
#
# 5. ValueError:
#    float("abc")처럼 값 변환이 불가능할 때 발생
#
# 6. ZeroDivisionError:
#    0으로 나눌 때 발생
#
# 7. 예외가 아니더라도 프로그램의 의미상 잘못된 값이 있을 수 있다.
#    예: 음수 전력, 출력전력 > 입력전력
#    이런 경우는 별도의 validation(유효성 검사)이 필요하다.