<!-- rumdl-disable-file MD013 -->

# 03. 저장소 구조와 개발 흐름

## 주요 디렉터리

| 경로 | 읽을 내용 |
|---|---|
| `KGEN/` | Mojo compiler와 MLIR 기반 lowering·tooling |
| `mojo/stdlib/` | Mojo 표준 라이브러리 source와 test |
| `mojo/docs/` | language manual, reference, release note |
| `mojo/proposals/` | language 설계 제안과 근거 |
| `max/kernels/` | CPU/GPU용 Mojo kernel |
| `max/mojo/max/` | GPU, algorithm, benchmark, runtime Mojo package |
| `max/python/max/graph/` | graph API와 operator |
| `max/python/max/pipelines/` | model architecture와 inference pipeline |
| `max/python/max/serve/` | OpenAI 호환 inference server |
| `max/examples/`, `mojo/examples/` | 실행 가능한 대표 사용법 |
| `Support/`, `AsyncRT/`, `Cache/` | compiler/runtime 공통 기반 |

## source를 읽는 방법

새 기능을 이해할 때는 구현 파일 하나만 보지 말고 다음 순서로 추적합니다.

1. public docs와 example에서 사용자 계약 확인
2. public API type과 argument convention 확인
3. graph/operator 또는 stdlib implementation 확인
4. CPU/GPU dispatch와 device-specific kernel 확인
5. source와 같은 구조의 test 확인
6. benchmark와 release note에서 성능·호환성 기대치 확인

## Bazel workflow

```bash
# target 탐색
./bazelw query '//max/kernels/...'
./bazelw query 'tests(//mojo/stdlib/...)'

# 좁은 target부터 검증
./bazelw test //path/to/package:test_name

# sanitizer와 반복 실행
./bazelw test --config=asan //path/to/package:target
./bazelw test --runs_per_test=10 //path/to/package:target
```

전체 `//...`는 매우 비싸므로 변경 경로의 target에서 시작해 영향 범위에 맞춰 넓힙니다.

## formatting과 test

- Mojo: `mojo format`
- repository format: `./bazelw run format`
- Python: repository의 Ruff/Black 설정 준수
- public API: docstring과 오류 계약 추가
- performance 변경: correctness test와 benchmark 함께 제공

## 기여 절차

1. 가장 가까운 `CONTRIBUTING.md`를 읽습니다.
2. 사소하지 않은 변경은 issue로 maintainer의 동의를 얻습니다.
3. `main`과 nightly pin을 동기화합니다.
4. 작은 단위로 구현하고 관련 test를 실행합니다.
5. AI 보조를 사용했다면 `AI_TOOL_POLICY.md` 방식으로 표시합니다.
6. commit은 sign-off하고 component tag를 사용합니다.

upstream은 compiler 자체와 일부 내부 영역에 외부 기여를 받지 않습니다. 구현 가능 여부와 기여 허용 여부는 별개의 문제입니다.

## 흔한 실패

| 증상 | 확인할 것 |
|---|---|
| Mojo syntax/API 오류 | stable/nightly 혼용, 현재 checkout의 release pin |
| Bazel target을 찾지 못함 | `./bazelw query`, 가장 가까운 `BUILD.bazel` |
| GPU test skip/fail | driver, device capability, test config |
| 성능 회귀 | warm-up, shape, dtype, device, synchronization 조건 |
| memory 오류 | ownership, buffer lifetime, host/device 위치, alignment |
| graph compile 오류 | input type, symbolic shape, device ref, operator support |

다음: [04. 고급 주제](04_advanced.md)
