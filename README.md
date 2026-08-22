# ewoo-20years

이우교육공동체 20년사의 온라인판. [MkDocs Material](https://squidfunk.github.io/mkdocs-material/) 로 만들어진 정적 사이트입니다.

- 라이브 사이트: https://ewooeducommunity.github.io/ewoo-20years/
- 소스 원본(HWPX, PDF): 저장소 밖에 별도 보관

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

`scripts/convert.py` 를 사용:

```bash
brew install --cask libreoffice   # 처음 한 번만
brew install pandoc               # 처음 한 번만
python scripts/convert.py <원본.hwpx> -o /tmp/ewoo-convert
```

## 파일·URL 컨벤션

- 파일명: 한글 그대로 사용 (예: `발간사.md`, `part1/01-개교의-배경.md`).
- URL: `use_directory_urls: true` 라서 확장자 없이 슬래시로 끝남 (`/part1/01-개교의-배경/`).
- 프론트매터: 모든 페이지 상단에 `title`, `tags` 최소 포함. Part 2 개인 에세이는 `authors` 추가.

## 크로스링크 컨벤션

인물·사건을 본문에서 참조할 때:

- 인물: `[홍길동](../part3/index.md#hong-gil-dong)`
  - 앵커는 국어 로마자 표기법(문화체육관광부 고시) 소문자·하이픈.
- 사건/연도: `[2010년 개교기념식](../part4/index.md#2010-03)`
  - 앵커는 `YYYY-MM` (월 미상이면 `YYYY`).
- 다른 에세이: `[김OO 에세이](../part2/kim-oo-first-graduation.md)`
- 강박적으로 다 걸지 말고, 본문 흐름상 자연스러운 곳에만.

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

## 관리자 연락

- Issues: 오탈자·개선 제보 (템플릿 없음, 자유 양식)
- Discussions: 게시·저작권 관련 논의
