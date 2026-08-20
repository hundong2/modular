<!-- rumdl-disable-file MD013 -->

# 단계별 실습

## 준비

Mojo/MAX는 Linux 또는 macOS에서 실행하세요. stable 환경 예시:

```bash
uv init modular-guide
cd modular-guide
uv add mojo
```

이 디렉터리의 파일을 project에 복사한 뒤 실행합니다. MAX Python API는 사용 중인 stable/nightly 문서에 맞는 MAX package 환경에서 실행해야 합니다.

## 1. Mojo 기초

```bash
mojo run 01_mojo_basics.mojo
```

목표: 정적 type, 함수, 변경 가능한 `List`와 loop를 사용해 작은 activation 변환을 수행합니다.

예상 출력:

```text
relu activations: [0.0, 0.0, 0.5, 3.0]
sum: 3.5
```

## 2. SIMD 연산

```bash
mojo run 02_simd_math.mojo
```

목표: 네 lane의 element-wise 연산과 horizontal reduction을 확인합니다.

예상 출력:

```text
scaled: [0.5, 1.0, 1.5, 2.0]
sum: 5.0
max: 2.0
```

## 3. MAX Graph

```bash
python 03_max_graph.py
```

목표: CPU device의 vector-add graph를 정의하고 compile한 뒤 buffer를 실행합니다. MAX API는 빠르게 변하므로 오류가 나면 현재 checkout의 `max/examples/capi/test_capi.py`와 `max/examples/custom_ops/addition.py`를 먼저 비교하세요.

## 실습 확장

- 기초 예제에 generic dtype 또는 compile-time width 추가
- SIMD width를 바꾸고 생성 assembly·성능 비교
- MAX Graph의 vector 길이를 symbolic dimension으로 변경
- CPU와 accelerator 결과를 tolerance 내에서 비교
- 잘못된 shape·dtype 입력이 명확히 실패하는 test 추가
