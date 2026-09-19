power = 100

def calculate():
    power = 50
    print(f"Inside function: {power}")

calculate()

print(f"Outside function: {power}")

# [복습 포인트]
#
# 1. 함수 내부에서 만든 변수는 local variable(지역 변수)이다.
#    함수 밖의 같은 이름 변수와 별개이다.
#
# 2. 함수 밖에서 만든 변수는 global variable(전역 변수)이다.
#
# 3. 함수 안에서 이름을 찾을 때 local scope의 변수가 우선된다.
#
# 4. 함수 내부에 해당 이름의 local 변수가 없다면
#    Python은 바깥 scope의 변수를 찾을 수 있다.
#
# 5. 함수 안에서 변수에 값을 대입하면,
#    기본적으로 그 변수는 local variable로 취급된다.
#
# 6. global 키워드로 전역 변수를 직접 수정할 수 있지만,
#    코드 추적이 어려워질 수 있으므로 남용하지 않는 것이 좋다.
#
# 7. 가능하면 값을 함수의 parameter로 전달하고
#    return으로 결과를 돌려주는 구조가 더 명확하다.


power = 100

def outer():
    power = 80

    def inner():
        print(power)

    inner()

outer()
print(power)

# [복습 포인트]
#
# Python은 변수 이름을 LEGB 순서로 탐색한다.
#
# L: Local      → 현재 함수
# E: Enclosing  → 현재 함수를 감싸는 바깥 함수
# G: Global     → 모듈(파일) 전역
# B: Built-in   → Python 기본 제공 이름 (print, len, sum 등)
#
# 가까운 scope에서 이름을 찾으면 그 값을 사용하고
# 더 바깥 scope까지 탐색하지 않는다.
#
# 같은 이름을 더 가까운 scope에서 정의하면
# 바깥쪽 이름이 가려질 수 있는데 이를 shadowing이라고 한다.
#
# 예: sum = 0 으로 정의하면 built-in sum()이 가려질 수 있다.


power = 100

def outer():
    power = 80

    def inner():
        power = 50
        print(f"Inner: {power}")

    inner()
    print(f"Outer: {power}")

outer()
print(f"Global: {power}")

# [복습 포인트]
#
# 함수마다 local scope가 따로 존재한다.
#
# inner 함수 안에서 power = 50을 만들면
# outer의 power = 80과 global power = 100에는 영향을 주지 않는다.
#
# nonlocal:
# 감싸고 있는 바깥 함수의 변수를 수정할 때 사용
#
# global:
# 모듈 전역 변수를 수정할 때 사용
#
# 가능하면 global/nonlocal에 의존하기보다
# parameter와 return을 이용하는 구조가 더 명확하다.