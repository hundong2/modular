"""Mojo의 type, List, loop를 이용한 작은 ReLU 실습."""


def relu(value: Float64) -> Float64:
    """음수는 0으로, 양수는 그대로 반환합니다."""
    if value < 0.0:
        return 0.0
    return value


def main():
    var activations = List[Float64]([-2.0, -0.25, 0.5, 3.0])
    var total = 0.0

    for i in range(len(activations)):
        # 결과를 같은 List에 기록해 mutable value의 사용을 확인합니다.
        activations[i] = relu(activations[i])
        total += activations[i]

    print("relu activations:", activations)
    print("sum:", total)
