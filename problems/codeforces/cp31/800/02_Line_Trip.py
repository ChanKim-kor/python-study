test_case = int(input())

for _ in range(test_case):
    n ,x = list(map(int, input().split()))
    gas_station = list(map(int, input().split()))
    gas_usage_betwn_stations = [gas_station[0]]


    for i in range(1, n):
        gas_usage_betwn_stations.append(gas_station[i]-gas_station[i-1])

    gas_usage_betwn_stations.append(2*(x - gas_station[-1]))

    print(max(gas_usage_betwn_stations))


# Review
# - Result: AC
# - Solve time: ~10m
# - Attempts: 1
#
# What was good:
# - 출발점 0부터 첫 주유소까지의 거리도 빠뜨리지 않았다.
# - 중간 주유소 사이의 최대 간격을 올바르게 계산했다.
# - 마지막 주유소 이후에는 x에 주유소가 없으므로
#   왕복 거리를 고려해 `2 * (x - last_station)`으로 처리했다.
#
# Things to improve:
# - `gas_usage_betwn_stations`는 `gaps`처럼 더 짧고 명확한 이름으로 쓸 수 있다.
# - `n, x = list(map(...))`에서 `list()`는 필요 없다.
# - 모든 gap을 리스트에 저장하지 않고 최대값만 갱신하면
#   추가 공간을 O(1)로 줄일 수 있다.
#
# Key takeaway:
# - 문제에서 "마지막 구간의 조건이 다른지" 꼭 확인하자.
# - 일반 구간과 경계 구간(start/end)은 같은 공식이 아닐 수 있다.
#
# Complexity:
# - Time: O(n)
# - Space: O(n)