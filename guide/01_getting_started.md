<!-- rumdl-disable-file MD013 -->

# 01. 설치와 첫 실행

## 학습 목표

- stable과 nightly channel을 구분한다.
- Mojo 예제를 실행한다.
- MAX 설치와 OpenAI 호환 server의 최소 흐름을 이해한다.

## 지원 환경

- Linux: x86_64, aarch64
- macOS: Apple Silicon
- Windows: 직접 지원하지 않음. Windows 사용자는 WSL2 권장
- GPU: 기능에 따라 NVIDIA, AMD 또는 Apple accelerator와 호환 driver 필요

## Mojo 설치

가장 단순한 stable 설치 예시는 `uv`를 사용합니다.

```bash
uv init hello-mojo
cd hello-mojo
uv add mojo
uv run mojo --version
```

Pixi를 사용하려면:

```bash
pixi init hello-mojo \
  -c https://conda.modular.com/max/ -c conda-forge
cd hello-mojo
pixi add mojo
pixi run mojo --version
```

nightly가 필요하면 channel을 `https://conda.modular.com/max-nightly/`로 바꿉니다. 저장소 `main`을 개발할 때는 checkout이 pin한 nightly 버전과 맞추는 것이 중요합니다.

## 첫 Mojo 프로그램

```mojo
def square(value: Int) -> Int:
    return value * value


def main():
    print("7 squared =", square(7))
```

```bash
mojo run hello.mojo
mojo build hello.mojo -o hello
./hello
```

Mojo는 indentation 기반 문법을 제공하지만 Python script처럼 해석만 하는 언어가 아닙니다. 정적 type, compile-time parameter, ownership와 low-level memory control을 함께 제공합니다.

## MAX 설치와 serving

공식 문서의 현재 stable/nightly 명령을 먼저 확인하세요. 설치 후에는 다음처럼 OpenAI 호환 server를 실행할 수 있습니다.

```bash
max serve --model modularai/Llama-3.1-8B-Instruct-GGUF
```

```bash
curl http://localhost:8000/v1/chat/completions \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "modularai/Llama-3.1-8B-Instruct-GGUF",
    "messages": [{"role": "user", "content": "Hello"}]
  }'
```

실제 model의 license, 메모리 요구량, quantization 형식과 accelerator 지원 여부는 별도로 확인해야 합니다.

## 이 저장소 개발 환경

전체 monorepo는 일반 package 사용보다 요구 사항이 큽니다.

```bash
./bazelw query '//mojo/...'
./bazelw query '//max/...'
./bazelw test //path/to/changed:target
```

각 디렉터리에 `pixi.toml`이 있으면 해당 환경과 task를 우선합니다.

```bash
pixi install
pixi task list
pixi run test
```

다음: [02. 핵심 개념](02_core_concepts.md)
