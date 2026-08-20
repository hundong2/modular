<!-- rumdl-disable-file MD013 -->

# 02. Mojo와 MAX 핵심 개념

## 1. Mojo value와 ownership

Mojo는 값의 복사·이동·수명을 명시적으로 모델링합니다. 고성능 code에서 불필요한 복사를 피하면서 dangling pointer와 data race 위험을 줄이기 위한 기반입니다.

- `var`: 변경 가능한 binding
- `ref`, `mut`, `out`: 접근과 mutation 의도를 표현하는 argument convention
- `Copyable`, `Movable`, `Deinitable`: type의 lifecycle capability
- `Pointer`: low-level memory 접근. deprecated `UnsafePointer` 대신 최신 API를 사용

API를 작성할 때는 값이 복사되는지, 빌려 쓰는지, 이동되는지를 호출자 관점에서 설명해야 합니다.

## 2. compile-time parameter

Mojo 함수와 type은 compile-time parameter를 받을 수 있습니다.

```mojo
def add_bias[width: Int](value: SIMD[DType.float32, width]):
    return value + 1.0
```

`width`가 compile time에 알려지므로 compiler는 target SIMD 폭이나 tile shape에 맞는 code를 생성할 수 있습니다. 지나친 specialization은 compile time과 binary 크기를 늘리므로 runtime variability와 균형을 맞춰야 합니다.

## 3. SIMD와 vectorization

`SIMD[dtype, width]`는 여러 lane을 한 번에 처리합니다. `std.algorithm.vectorize`는 전체 길이를 SIMD chunk로 나누고 tail을 처리하도록 돕습니다.

실습: [`02_simd_math.mojo`](examples/02_simd_math.mojo)

성능 확인 시에는 scalar 대비 속도뿐 아니라 alignment, contiguous access, tail 처리와 수치 오차를 검사하세요.

## 4. accelerator kernel

GPU kernel은 global/thread index로 작업 위치를 계산하고 device buffer를 읽고 씁니다. 핵심 원칙은 다음과 같습니다.

- 인접 thread가 인접 memory를 읽도록 coalescing을 고려
- CPU↔GPU synchronization과 transfer 최소화
- boundary check와 launch shape의 일치
- device별 capability와 dtype 지원 확인
- 변경 전후 benchmark와 정확성 test 동시 제공

## 5. MAX Graph

MAX Graph는 input type, shape, device와 operator 관계를 선언합니다. `InferenceSession`이 graph를 compile하고 실행 가능한 model로 만듭니다.

```text
TensorType + symbolic shape
  → Graph operator
  → compile / optimize
  → device-specific executable
  → Buffer 입력과 결과
```

symbolic dimension은 여러 input 길이를 하나의 graph로 처리할 수 있게 하지만, 모든 operator와 kernel이 해당 dynamic shape를 지원하는지 확인해야 합니다.

실습: [`03_max_graph.py`](examples/03_max_graph.py)

## 6. model pipeline과 serving

`max/python/max/pipelines`는 model architecture, weight adapter, tokenizer, KV cache와 request context를 연결합니다. `max/python/max/serve`는 batching, scheduling, API schema와 OpenAI 호환 endpoint를 담당합니다.

요청 흐름:

```text
HTTP request
  → schema·tokenization
  → scheduler·batching
  → pipeline / compiled graph
  → KV cache·device execution
  → decoding·streaming response
```

다음: [03. 저장소 개발 흐름](03_repository_workflow.md)
