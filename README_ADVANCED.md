# 🍱 랜덤 점심 메뉴 선택 슬랙봇 (고급 버전)

점심 메뉴 고민 끝! 슬랙에서 메뉴 추가/삭제/조회까지 다 되는 완전체 버전!

## ✨ 주요 기능

- 🎲 **랜덤 메뉴 추천** - `/lunch`
- ➕ **메뉴 추가** - `/lunch-add 메뉴이름`
- ➖ **메뉴 삭제** - `/lunch-remove 메뉴이름`
- 📋 **메뉴 목록 보기** - `/lunch-list`
- ❓ **도움말** - `/lunch-help`

## 🚀 설치 및 실행 방법

### 1. 필요한 패키지 설치
```bash
pip install -r requirements.txt
```

### 2. Slack 앱 만들기

#### (1) Slack 앱 생성
1. https://api.slack.com/apps 접속
2. "Create New App" 클릭
3. "From scratch" 선택
4. 앱 이름 입력 (예: 점심메뉴봇)
5. 워크스페이스 선택

#### (2) Socket Mode 활성화
1. 좌측 메뉴에서 "Socket Mode" 클릭
2. "Enable Socket Mode" 토글 ON
3. 토큰 이름 입력하고 생성
4. **`xapp-`로 시작하는 토큰 복사** → 이게 `SLACK_APP_TOKEN`

#### (3) Bot Token 스코프 설정
1. 좌측 메뉴에서 "OAuth & Permissions" 클릭
2. "Scopes" → "Bot Token Scopes" 섹션으로 이동
3. 아래 권한 추가:
   - `commands` (슬래시 커맨드 사용)
   - `chat:write` (메시지 전송)
4. 페이지 상단에서 "Install to Workspace" 클릭
5. **`xoxb-`로 시작하는 Bot User OAuth Token 복사** → 이게 `SLACK_BOT_TOKEN`

#### (4) 슬래시 커맨드 생성 (5개 모두 만들어야 함!)

**중요: Request URL은 모두 아무거나 입력 (예: `https://example.com`)**

1. `/lunch`
   - Short Description: `랜덤 점심 메뉴 추천`

2. `/lunch-add`
   - Short Description: `메뉴 추가`
   - Usage Hint: `메뉴이름`

3. `/lunch-remove`
   - Short Description: `메뉴 삭제`
   - Usage Hint: `메뉴이름`

4. `/lunch-list`
   - Short Description: `전체 메뉴 목록 보기`

5. `/lunch-help`
   - Short Description: `도움말`

### 3. 환경 변수 설정

`.env.example`을 `.env`로 복사하고 토큰 입력:

```bash
cp .env.example .env
```

`.env` 파일 편집:
```
SLACK_BOT_TOKEN=xoxb-여기에-봇-토큰-입력
SLACK_APP_TOKEN=xapp-여기에-앱-토큰-입력
```

### 4. 봇 실행

```bash
# 환경변수 로드 (Linux/Mac)
export $(cat .env | xargs)

# 봇 실행
python slack_lunch_bot_advanced.py
```

Windows라면:
```cmd
set SLACK_BOT_TOKEN=xoxb-...
set SLACK_APP_TOKEN=xapp-...
python slack_lunch_bot_advanced.py
```

## 📝 사용 예시

### 1️⃣ 메뉴 추가하기
```
/lunch-add 🍜 회사 앞 라멘집
/lunch-add 🍕 빌딩 지하 피자
/lunch-add 🍔 골목 수제버거
```

### 2️⃣ 메뉴 목록 확인
```
/lunch-list
```

### 3️⃣ 랜덤 메뉴 뽑기
```
/lunch
```

### 4️⃣ 메뉴 삭제하기
```
/lunch-remove 🍜 회사 앞 라멘집
```

### 5️⃣ 도움말 보기
```
/lunch-help
```

## 💾 데이터 저장

- 메뉴는 `lunch_menus.json` 파일에 자동 저장됨
- 봇을 재시작해도 메뉴 데이터 유지됨
- 백업이 필요하면 `lunch_menus.json` 파일만 복사하면 됨

## 🎨 추가 기능 아이디어

현재 코드에 더 추가할 수 있는 기능들:

- [ ] 카테고리별 메뉴 관리 (한식/중식/일식/양식)
- [ ] 최근 먹은 메뉴 히스토리 (같은 메뉴 자주 안 나오게)
- [ ] 메뉴 투표 기능
- [ ] 날씨 API 연동해서 날씨별 추천
- [ ] 요일별 메뉴 제한 (금요일엔 치킨만!)
- [ ] 메뉴 평점/리뷰 시스템
- [ ] 팀원들이 가장 좋아하는 메뉴 통계

## 🔐 보안 팁

- `.env` 파일은 절대 git에 커밋하지 말 것!
- `.gitignore`에 `.env` 추가 권장
- 토큰이 노출되면 즉시 재발급

## 🐛 문제 해결

**"Invalid token" 에러**
- 토큰이 제대로 복사되었는지 확인
- Bot Token은 `xoxb-`로 시작
- App Token은 `xapp-`로 시작

**커맨드가 작동 안함**
- 봇이 실행 중인지 확인
- 5개 Slash Command가 모두 생성되었는지 확인
- 봇이 채널에 초대되었는지 확인

**메뉴가 저장 안됨**
- `lunch_menus.json` 파일 생성 권한 확인
- 파일 경로가 올바른지 확인

## 📌 참고

- Slack Bolt 공식 문서: https://slack.dev/bolt-python/
- Slack API 문서: https://api.slack.com/
