"""네 개의 Float32 lane을 동시에 계산하는 SIMD 실습."""


def main():
    var values = SIMD[DType.float32, 4](1.0, 2.0, 3.0, 4.0)
    # scalar는 모든 lane으로 broadcast되어 element-wise로 곱해집니다.
    var scaled = values * 0.5

    print("scaled:", scaled)
    print("sum:", scaled.reduce_add())
    print("max:", scaled.reduce_max())
