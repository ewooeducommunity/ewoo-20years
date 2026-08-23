# ewoo-20years

이우교육공동체 20년사의 온라인판. [MkDocs Material](https://squidfunk.github.io/mkdocs-material/) 로 만들어진 정적 사이트입니다.

- 라이브 사이트: https://ewooeducommunity.github.io/ewoo-20years/
- 소스 원본(HWPX, PDF): 저장소 밖에 별도 보관
- 현재 버전: **v1.0.0** (2026-08-23 정식 공개)

## 담긴 내용 (v1.0.0)

발간사부터 정관까지 20년사 전권이 온라인에 올라와 있습니다.

| 구성 | 분량 |
| --- | --- |
| 발간사 | 1편 |
| Part 1. 주제별 역사 | 19개 챕터 (인터뷰 2편 포함) |
| Part 2. 나와 공동체 | 23인 에세이 |
| Part 3. 역대 임원진 | 49명 |
| Part 4. 연대표 | 293건 |
| Part 8. 정관 | 1편 |
| 자료실 | 전체·파트별 원본 PDF |

본문 안에는 인물·사건을 서로 잇는 **크로스링크 34건(인물) + 18건(사건)** 이 자연스러운 문맥에 삽입되어 있습니다 (아래 [크로스링크 컨벤션](#크로스링크-컨벤션) 참고). 깨진 링크가 없는지는 `python scripts/check_links.py` 로 상시 검증합니다.

## 편집 워크플로

### 오탈자 한 줄 수정 (제일 간단)

1. 라이브 사이트에서 문제 페이지 열기
2. 우측 상단 연필 아이콘 클릭 → GitHub 편집기가 열림
3. 수정 → 커밋 메시지 입력 → "Propose changes" → PR 생성
4. 다른 관리자 리뷰 후 머지 → 1~2분 뒤 자동 반영

### 새 에세이 추가·큰 편집

1. 로컬로 저장소를 클론
   ```bash
   git clone https://github.com/ewooeducommunity/ewoo-20years
   cd ewoo-20years
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   mkdocs serve
   ```
2. `http://localhost:8000` 에서 실시간 프리뷰 하며 편집
3. 브랜치 생성 → 커밋 → push → PR

### HWPX/HWP 원본을 Markdown 으로 변환

두 단계로 처리합니다 (macOS Homebrew의 LibreOffice가 HWP 필터를 포함하지 않아 자동 변환이 안 됨):

1. **한글 오피스에서 원본을 DOCX로 저장** (`파일 → 다른 이름으로 저장 → Microsoft Word 문서(*.docx)`).
2. **DOCX를 Markdown으로 변환**:
   ```bash
   brew install pandoc               # 처음 한 번만
   python scripts/convert.py <원본.docx> -o /tmp/ewoo-convert
   ```

한글 오피스가 없는 환경이라면 원본 소유자에게 DOCX 변환본을 요청하세요.

## 파일·URL 컨벤션

- 파일명: 한글 그대로 사용 (예: `발간사.md`, `part1/01-개교의-배경.md`).
- URL: `use_directory_urls: true` 라서 확장자 없이 슬래시로 끝남 (`/part1/01-개교의-배경/`).
- 프론트매터: 모든 페이지 상단에 `title`, `tags` 최소 포함. Part 2 개인 에세이는 `authors` 추가.

## 크로스링크 컨벤션

인물·사건을 본문에서 참조할 때:

- 인물: `[홍길동](../part3/index.md#hong-gil-dong)`
  - 앵커는 국어 로마자 표기법(문화체육관광부 고시) 소문자·하이픈.
  - 실제 사용례 (`docs/part1/01-founding-preparation-meeting.md`): `[백희봉](../part3/index.md#baek-hui-bong), [이재철](../part3/index.md#i-jae-cheol), 이현영, [정광필](../part3/index.md#jeong-gwang-pil)을 비롯해 여섯 명이 모였다.`
- 사건/연도: `[2010년 개교기념식](../part4/index.md#2010-03)`
  - 앵커는 `YYYY-MM` (월 미상이면 `YYYY`, 같은 달에 여러 건이면 `YYYY-MM-N`).
  - 실제 사용례 (`docs/part1/03-community-founding-and-operation.md`): `[2001년 1월](../part4/index.md#2001-01) (가칭) '내일을 여는 학교 준비 모임'을 결성하고, [7월 1일](../part4/index.md#2001-07)엔 경기도 광주시...`
- 다른 에세이: `[김OO 에세이](../part2/kim-oo-first-graduation.md)`
- 강박적으로 다 걸지 말고, 본문 흐름상 자연스러운 곳에만.
- Part 1·2 본문 전체에 현재 인물 링크 34건, 사건 링크 18건이 걸려 있습니다. 새 페이지를 쓸 때도 이 밀도를 참고하세요.
- 인물 앵커의 소스는 `docs/part3/index.md`, 사건 앵커의 소스는 `docs/part4/index.md` 입니다. 새 인물·사건을 추가하면 두 인덱스에 먼저 앵커를 만든 뒤 본문에서 링크하세요.

## 커밋 메시지

접두어를 붙여 구분:

- `feat: <내용>` — 새 기능·페이지
- `docs: <내용>` — 콘텐츠 편집·오탈자
- `chore: <내용>` — 설정·의존성
- `ci: <내용>` — 워크플로
- `[part1] <내용>` — 특정 파트 콘텐츠 편집 시 파트 태그도 함께

## 이름 규칙

"이우"는 영어·식별자 표기 시 **`ewoo`** 로 통일 (예: 저장소 `ewoo-20years`, 파일 `ewoo-20years-full.pdf`).

## 배포

`main` 브랜치에 머지되면 GitHub Actions가 자동으로 gh-pages 브랜치를 갱신하고 GitHub Pages가 서빙합니다. 소요 시간 1~2분.

로컬 빌드 검증:

```bash
mkdocs build --strict
```

경고가 하나라도 뜨면 실패 처리됩니다.

## 롤백

문제 커밋을 되돌리려면:

1. GitHub에서 해당 커밋 페이지 열기
2. "Revert" 버튼 → PR 자동 생성 → 머지
3. 2분 뒤 사이트 복구

## 편찬위원회 확정 대기 항목

Plan 1~3 작업 중 편찬위원회의 최종 확정이 필요한 사항들을 [Issue #1](https://github.com/ewooeducommunity/ewoo-20years/issues/1) 에 모아뒀습니다 (추진위원·창립회원 명단 별도 게시 여부, 일부 인물 정보 확인 등). v1.0.0 공개 이후에도 계속 갱신됩니다.

## 관리자 연락

- Issues: 오탈자·개선 제보 (템플릿 없음, 자유 양식)
- Discussions: 게시·저작권 관련 논의
