<!-- rumdl-disable-file MD013 -->

# 04. 성능·배포·고급 확장

## 1. kernel 최적화

최적화 순서는 측정에서 시작합니다.

1. reference implementation과 tolerance를 고정합니다.
2. representative shape·dtype·device를 정의합니다.
3. compile, warm-up, transfer, execution 시간을 분리합니다.
4. memory access와 synchronization 병목을 먼저 확인합니다.
5. SIMD width, tile, thread/block shape를 조정합니다.
6. correctness와 benchmark를 같은 변경에 포함합니다.

peak throughput만 보고 작은 batch나 tail shape를 악화시키지 않도록 workload 분포를 함께 기록하세요.

## 2. hardware abstraction

device-agnostic API 아래에서 NVIDIA·AMD GPU, Intel·Apple CPU 등 target별 dispatch와 implementation이 선택됩니다. 확장 시 다음을 분리합니다.

- 공통 수학 계약
- target capability predicate
- layout과 memory space
- vendor library 사용 여부
- fallback과 unsupported 오류

fallback이 조용히 다른 dtype이나 느린 경로를 선택하면 정확성·SLO 문제가 숨을 수 있으므로 telemetry에 선택된 backend를 남기는 것이 좋습니다.

## 3. model architecture 추가

새 architecture는 weight naming만 연결하는 작업이 아닙니다.

- config와 tokenizer
- weight format와 adapter
- graph construction과 custom operator
- KV cache strategy
- prefill/decode 차이
- sampling과 output contract
- quantization과 distributed execution
- model-specific regression fixture

`max/python/max/pipelines/architectures`에서 가장 가까운 기존 architecture를 골라 registration부터 request 실행까지 추적하세요.

## 4. serving 운영

운영에서는 단일 token latency 외에 다음을 측정합니다.

- time to first token과 inter-token latency
- request concurrency, continuous batching, queue time
- prompt/decode token throughput
- KV cache 사용량과 eviction
- cancellation과 streaming disconnect
- readiness, backpressure, graceful shutdown
- model load 시간과 accelerator memory headroom

OpenAI 호환이라는 말은 모든 provider extension과 세부 오류가 동일하다는 뜻이 아닙니다. 사용하는 endpoint와 schema를 contract test로 고정하세요.

## 5. 보안과 공급망

- model repository와 revision을 pin하고 license를 확인합니다.
- 원격 custom code 실행을 기본값으로 허용하지 않습니다.
- authentication token과 model URL을 log에 노출하지 않습니다.
- container image, Python wheel, Conda/Pixi package와 driver version을 기록합니다.
- public server에는 authentication, rate limit, request size 제한과 audit log를 둡니다.
- prompt 내용과 생성 결과에 개인정보가 포함될 수 있음을 telemetry 설계에 반영합니다.

## 6. 다음 학습 경로

1. `mojo/docs/manual`에서 ownership, parameters, traits 학습
2. `mojo/stdlib/test`에서 API별 executable specification 읽기
3. `max/examples/custom_ops`로 Python Graph↔Mojo kernel 연결
4. `max/python/max/pipelines/architectures`에서 실제 model 추적
5. `max/python/max/serve`에서 scheduling·streaming 운영 흐름 확인
6. `max/kernels/benchmarks`에서 성능 측정 관행 학습

[가이드 홈](README.md)으로 돌아갑니다.
