<!-- rumdl-disable-file MD013 MD033 MD041 MD075 -->

<div align="center">
    <img src="https://modular-assets.s3.us-east-1.amazonaws.com/images/modular-banner-github.png">

[Modular 소개] | [MAX 문서] | [Mojo 문서] | [기여 안내]

</div>

---

# Modular Platform

[English](README.md) · **한국어** · [한국어 학습 가이드](guide/README.md)

이 저장소는 AI 개발과 배포를 하나로 연결하는 Modular Platform의 오픈 소스 구성 요소를 제공합니다. 주요 구성 요소는 **MAX Framework**🧑‍🚀와 **Mojo Language**🔥입니다.

## 시작하기

MAX Framework로 모델을 서비스하려면 [MAX 빠른 시작 가이드](https://max.modular.com/get-started)를 참고하세요.

Mojo 언어를 시작하려면 [Mojo 빠른 시작 가이드](https://mojolang.org/docs/manual/quickstart/)를 참고하세요.

한국어로 저장소 전체 구조와 설치·실습·고급 개발 흐름을 익히려면 [한국어 학습 가이드](guide/README.md)에서 시작하세요.

## 저장소 소개

Modular 팀은 Modular Platform의 더 많은 구성 요소를 지속해서 오픈 소스로 공개하고 있습니다. 이 저장소의 주요 구성은 다음과 같습니다.

- Mojo 컴파일러: [`/KGEN`](KGEN)
- Mojo 표준 라이브러리: [`/mojo/stdlib`](mojo/stdlib)
- MAX 가속기 라이브러리: [`/max/kernels`](max/kernels)
- MAX 추론 서버: [`/max/python/max/serve`](max/python/max/serve) — OpenAI 호환 endpoint 제공
- MAX 모델 pipeline: [`/max/python/max/pipelines`](max/python/max/pipelines) — Python 기반 graph 구성
- 코드 예제: [`/max/examples`](max/examples), [`/mojo/examples`](mojo/examples)

## 아키텍처 한눈에 보기

| 계층 | 대표 언어 | 역할 |
|---|---|---|
| Mojo/KGEN | C++, MLIR | Mojo compiler와 compiler infrastructure |
| Mojo 표준 라이브러리 | Mojo | 언어 기본 자료구조, 알고리즘, 시스템·GPU API |
| MAX kernels | Mojo | CPU·GPU용 고성능 연산 kernel |
| MAX Graph·runtime | Python, C++, Mojo | device 추상화, graph compile, 실행과 memory 관리 |
| MAX pipelines·serve | Python | 모델 구조, tokenization, KV cache, scheduling, OpenAI 호환 serving |

고수준 Python orchestration과 저수준 Mojo kernel을 분리하면서도 같은 compiler/runtime stack에서 연결하는 것이 핵심 설계입니다.

## 기여하기

현재 Mojo 표준 라이브러리, MAX accelerator library, MAX model architecture, 코드 예제와 문서 등의 기여를 받습니다. Mojo compiler 자체에는 아직 외부 기여를 받지 않습니다.

변경을 시작하기 전에 반드시 [기여 가이드](CONTRIBUTING.md)를 읽고, 작업 영역에서 가장 가까운 `CONTRIBUTING.md`와 다음 개발 문서를 확인하세요.

- [`/max/docs`](max/docs): MAX Framework codebase 개발 문서
- [`/mojo/stdlib/docs`](mojo/stdlib/docs): Mojo 표준 라이브러리 개발 문서

사소하지 않은 변경은 구현 전에 issue를 열어 maintainer와 방향을 합의해야 합니다. AI 보조 작업은 [AI 도구 사용 정책](AI_TOOL_POLICY.md)에 따라 명시하고 사람이 결과를 검토해야 합니다.

버그를 발견했다면 [issue 양식](https://github.com/modular/modular/issues/new/choose)으로 재현 방법, 환경, 영향 범위를 함께 제출해 주세요.

## 빌드와 테스트

monorepo 개발은 저장소 루트의 Bazel wrapper를 사용합니다.

```bash
./bazelw build //...
./bazelw test //...
./bazelw test //mojo/stdlib/...
./bazelw test //max/kernels/...
```

개별 예제는 해당 디렉터리의 `pixi.toml`이 제공하는 task를 우선 사용합니다.

```bash
pixi install
pixi task list
pixi run test
```

지원 환경은 Linux x86_64·aarch64와 macOS Apple Silicon입니다. Windows는 현재 직접 지원하지 않으므로 WSL2 또는 Linux 개발 환경을 사용하세요. GPU 기능은 vendor, driver와 accelerator availability에 따라 달라집니다.

## 라이선스

이 저장소와 기여 내용은 LLVM 예외가 포함된 Apache License v2.0으로 배포됩니다. 자세한 내용은 [LICENSE](LICENSE)를 확인하세요.

MAX의 사용과 배포에는 [Modular Community License](https://www.modular.com/legal/community)가 적용됩니다.

### 제3자 라이선스

Hugging Face 등에서 내려받는 관련 software, model, dataset의 제3자 라이선스를 확인하고 준수할 책임은 사용자에게 있습니다. 저장소 코드의 라이선스가 model weight의 재배포 권한까지 자동으로 부여하지는 않습니다.

## 커뮤니티와 행사

커뮤니티에 질문하거나 정기 모임과 지역 meetup에 참여할 수 있습니다.

| 채널 | 링크 |
|---|---|
| 💬 Discord | [discord.gg/modular][discord] |
| 💬 Forum | [forum.modular.com][forum] |
| 📅 Meetup Group | [meetup.com/modular-meetup-group][meetup-group] |
| 🎦 Community Meetings | [예정된 community call][public-com-meet-doc] |
| 📺 YouTube | [youtube.com/@modularinc][youtube] |

예정된 행사는 Meetup과 Discord에 게시되며 community meeting 녹화 영상은 YouTube에서 볼 수 있습니다.

## 기여자에게 감사드립니다

<a href="https://github.com/modular/modular/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=modular/modular" />
</a>

<!-- 링크 참조 -->
[Modular 소개]: https://www.modular.com/
[MAX 문서]: https://max.modular.com/
[기여 안내]: ./CONTRIBUTING.md
[Mojo 문서]: https://mojolang.org/docs/
[discord]: https://discord.gg/modular
[forum]: https://forum.modular.com/
[meetup-group]: https://www.meetup.com/modular-meetup-group/
[youtube]: https://www.youtube.com/@modularinc
[public-com-meet-doc]: https://modul.ar/community-meeting-doc
