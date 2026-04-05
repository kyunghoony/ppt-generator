# INSTRUCTION: renderer.py 퀄리티 업그레이드

## 현재 상태 진단

현재 renderer.py의 출력물을 분석한 결과, 아래 문제들이 확인됨:

### 치명적 문제
1. **Metrics 슬라이드: 시각적 위계 없음.** label, value, delta가 전부 동일한 폰트 크기(14pt). value는 36-44pt 볼드, label은 12pt, delta는 14pt 컬러(green/red)로 분리해야 함.
2. **Comparison 슬라이드: 빈 슬라이드.** 타이틀만 있고 내용 없음. left/right 컬럼 + 아이템 리스트 렌더링 구현 필요.
3. **Blank 슬라이드: 빈 슬라이드.** 구현 안 됨.
4. **config.yaml 컬러/폰트가 실제 렌더링에 반영 안 됨.** FV 프리셋의 컬러가 적용되지 않고 기본 검정색만 사용.

### 디자인 문제
5. **배경색 없음.** 전체 슬라이드 흰색. Title 슬라이드는 primary 컬러 배경 + 흰색 텍스트 필요.
6. **카드/박스 UI 없음.** Metrics, Comparison 등은 rounded rect 카드 안에 내용을 넣어야 함.
7. **Content 슬라이드 bullet 미구현.** 일반 텍스트로만 나열됨. bullet marker + indent 필요.
8. **Footer 미구현.** config.yaml에 footer 설정 있지만 렌더링 안 됨.
9. **차트 컬러가 프리셋과 무관.** 기본 Excel 차트 팔레트 사용 중.

---

## 수정 지시

### 1. renderer.py — Metrics 슬라이드 수정

MetricSlide 렌더링 시 각 metric을 카드 형태로 렌더링:

```
┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐
│   ARR            │  │   Burn Rate      │  │   Runway         │
│   ₩2.4B          │  │   ₩180M/mo       │  │   14 months      │
│   +42% YoY  ▲    │  │                  │  │                  │
└─────────────────┘  └─────────────────┘  └─────────────────┘
```

각 metric 텍스트 박스 내부:
- **label**: 12pt, secondary color, regular weight
- **value**: 40pt, bold, primary color
- **delta**: 14pt, bold, 양수면 accent_positive(#16A34A), 음수면 accent_negative(#DC2626)

각 metric 뒤에 rounded rectangle 배경 도형 추가:
- fill: light gray (#F5F5F7) 또는 프리셋의 card_background
- corner radius: 0.15 inches
- 도형을 먼저 추가하고 텍스트를 그 위에 배치 (z-order)

### 2. renderer.py — Title 슬라이드 수정

Title 슬라이드는 Blank 레이아웃 사용하고 직접 그리기:
- 슬라이드 전체 배경: primary color
- title: 44pt, bold, white (#FFFFFF), 수직 중앙 약간 위
- subtitle: 18pt, regular, text_light 또는 white 70% opacity
- 로고: config에 logo.path 있으면 우측 하단에 삽입

### 3. renderer.py — Section Divider 수정

- 배경: secondary color
- title: 36pt, bold, white
- subtitle: 16pt, white 70% opacity
- 수직 중앙 정렬

### 4. renderer.py — Content 슬라이드 수정

- title: 28pt, bold, primary color, 좌측 정렬
- body text: 16pt, text_primary
- bullet이 있으면:
  - bullet marker: "•" 문자, accent color
  - indent: 0.3 inches
  - line spacing: 1.5

### 5. renderer.py — Comparison 슬라이드 구현

```
┌──── Left Label ────┐   ┌──── Right Label ────┐
│  • item 1           │   │  • item 1            │
│  • item 2           │   │  • item 2            │
│  • item 3           │   │  • item 3            │
└─────────────────────┘   └──────────────────────┘
```

- 좌측: accent color 배경 카드, white 텍스트
- 우측: light gray 배경 카드, primary 텍스트
- 각 카드 width: 슬라이드 폭의 45%, gap: 슬라이드 폭의 4%

### 6. renderer.py — Two Column 슬라이드 수정

- 좌/우 컬럼 사이 구분선 (1pt, light gray) 또는 적절한 gap
- 각 컬럼 width: 47%
- 좌측 컬럼 좌측 정렬, 우측 컬럼 좌측 정렬

### 7. renderer.py — Timeline 슬라이드 구현

- 수평 또는 수직 타임라인
- 각 이벤트: 원형 마커(accent color) + 날짜(bold) + 설명
- 마커 사이 연결선 (1pt, secondary color)

### 8. renderer.py — Table 슬라이드 수정

python-pptx의 Table shape 사용:
- 헤더 행: primary color 배경, white 텍스트, bold
- 데이터 행: 짝수/홀수 행 색상 교차 (zebra striping)
- 셀 padding: 0.1 inches
- 테이블 폰트: 12pt

### 9. renderer.py — Footer 구현

모든 슬라이드 하단(title, section_divider 제외)에:
- 좌측: footer text (config에서 로드)
- 우측: 페이지 번호
- 폰트: 9pt, text_secondary color
- 위치: 슬라이드 하단 0.3 inches

### 10. renderer.py — 차트 컬러

charts.py에서 차트 생성 시 프리셋 config의 컬러 팔레트 적용:
- chart_colors: [primary, accent, secondary, ...] 순서로 시리즈 컬러 지정
- python-pptx의 ChartData + chart.series 컬러 직접 설정

### 11. styles.py — config.yaml 확장

config.yaml에 아래 키 추가 (없으면 기본값 사용):

```yaml
colors:
  # 기존 + 추가
  card_background: "#F5F5F7"
  accent_positive: "#16A34A"
  accent_negative: "#DC2626"
  divider: "#E5E7EB"
  
chart_colors:
  - "#1a1a2e"
  - "#0f3460"
  - "#16213e"
  - "#e94560"
  - "#533483"
```

FV config.yaml도 동일하게 확장.

---

## 검증 조건

수정 후 아래를 반드시 확인:

1. `python examples/generate_sample.py` 실행 — 에러 없이 두 파일 생성
2. generic_sample.pptx:
   - Slide 1: 컬러 배경 + 흰색 타이틀
   - Slide 3 (Metrics): 카드 UI, value 큰 폰트, delta 컬러 분리
   - Slide 4 (Chart): 프리셋 컬러 적용
   - Slide 5 (Comparison): 두 컬럼 카드에 내용 있음
   - 모든 content 슬라이드에 footer 표시
3. fv_sample.pptx:
   - FV 프리셋 컬러 적용됨 (generic과 다른 색상)
   - 한글 텍스트 정상 렌더링 (₩ 기호 포함)
   - Pretendard 폰트 적용됨
4. `pytest` 통과

---

## 작업 순서

의존성 고려하여 아래 순서로 작업:

1. styles.py — config.yaml 확장 키 로드 + 기본값 처리
2. presets/default/config.yaml, presets/fv/config.yaml — 새 키 추가
3. renderer.py — Title 슬라이드 수정
4. renderer.py — Metrics 슬라이드 수정
5. renderer.py — Content 슬라이드 수정 (bullet)
6. renderer.py — Comparison 슬라이드 구현
7. renderer.py — Table 슬라이드 수정
8. renderer.py — Timeline 슬라이드 구현
9. renderer.py — Footer 구현
10. charts.py — 프리셋 컬러 적용
11. examples/sample_input.json — Comparison, Timeline 예시 데이터 추가
12. 전체 테스트 실행 + 결과물 시각 확인
