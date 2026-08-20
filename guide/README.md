<!-- rumdl-disable-file MD013 -->

# Modular Platform 한국어 학습 가이드

[원본 README](../README.md) · [한국어 README](../README_kor.md)

이 가이드는 Mojo 문법만 소개하는 데 그치지 않고, Mojo kernel에서 MAX Graph와 OpenAI 호환 serving까지 이어지는 Modular Platform의 전체 흐름을 단계적으로 설명합니다.

## 학습 순서

1. [01. 설치와 첫 실행](01_getting_started.md)
2. [02. Mojo와 MAX 핵심 개념](02_core_concepts.md)
3. [03. 저장소 구조와 개발 흐름](03_repository_workflow.md)
4. [04. 성능·배포·고급 확장](04_advanced.md)
5. [실습 예제](examples/README.md)

## 로드맵

| 단계 | 결과물 | 권장 실습 |
|---|---|---|
| 입문 | Mojo 프로그램을 실행하고 value semantics를 설명 | `01_mojo_basics.mojo` |
| 기초 | SIMD 연산이 lane 단위로 수행되는 원리를 확인 | `02_simd_math.mojo` |
| 응용 | Python에서 MAX Graph를 구성·compile·execute | `03_max_graph.py` |
| 고급 | kernel, graph, pipeline, serving의 경계를 추적 | 저장소 공식 예제와 선택적 Bazel test |

## 플랫폼을 한 문장으로 설명하면

```text
Python model/pipeline/serve
        ↓ graph 구성
MAX compiler + runtime
        ↓ device별 lowering·dispatch
Mojo kernels
        ↓
CPU / NVIDIA GPU / AMD GPU / Apple Silicon
```

Mojo는 Python과 비슷한 생산성을 목표로 하면서 compile-time parameter, ownership, SIMD와 accelerator programming을 제공합니다. MAX는 이 kernel을 graph, model pipeline, runtime, serving 계층으로 연결합니다.

## 버전 주의

이 저장소의 `main`은 nightly release와 함께 움직이며 Mojo/MAX API도 빠르게 바뀔 수 있습니다. 학습 자료보다 다음 항목을 최종 기준으로 삼으세요.

1. 현재 checkout의 `pixi.lock`, `MODULE.bazel`, release note
2. 실행한 `mojo --version`, `max --version`
3. 현재 source와 가장 가까운 공식 example·test
4. stable/nightly 중 실제 설치한 channel의 공식 문서

## 라이선스와 기여 경계

repository code는 Apache-2.0 with LLVM Exceptions이지만 MAX와 외부 model에는 별도 조건이 있을 수 있습니다. 또한 AI 보조 기여는 `AI_TOOL_POLICY.md`에 따라 표시하고 사람이 직접 검토해야 합니다. upstream 기여를 계획한다면 사소하지 않은 변경은 먼저 issue에서 maintainer 승인을 받으세요.
