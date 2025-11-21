# 🍱 Slack Lunch Bot

점심 메뉴를 랜덤으로 추천해주는 간단한 Slack 봇입니다.

## ✨ 기능

- `/lunch 메뉴1, 메뉴2, 메뉴3` - 입력한 메뉴 중 랜덤으로 하나 선택
- `/lunch-help` - 도움말 보기

## 📖 사용 예시

```
/lunch 🍜 라면, 🍕 피자, 🍔 햄버거, 🍱 김밥
/lunch 된장찌개, 김치찌개, 순두부찌개
/lunch 중식, 한식, 일식, 양식
```

## 🚀 Render 배포 방법

### 1. Slack 앱 설정

1. https://api.slack.com/apps 접속
2. "Create New App" → "From scratch" 선택
3. 앱 이름 입력 후 워크스페이스 선택

#### Socket Mode 활성화
1. 좌측 메뉴 "Socket Mode" 클릭
2. "Enable Socket Mode" 토글 ON
3. 토큰 생성 → `SLACK_APP_TOKEN` (xapp-로 시작)

#### Bot Token 설정
1. 좌측 메뉴 "OAuth & Permissions" 클릭
2. "Bot Token Scopes"에 다음 권한 추가:
   - `commands`
   - `chat:write`
3. "Install to Workspace" 클릭
4. Bot Token 복사 → `SLACK_BOT_TOKEN` (xoxb-로 시작)

#### Slash Commands 생성
1. 좌측 메뉴 "Slash Commands" 클릭
2. "/lunch" 명령어 생성
   - Command: `/lunch`
   - Short Description: `점심 메뉴 랜덤 선택`
   - Request URL: `https://example.com` (아무거나)
3. "/lunch-help" 명령어 생성
   - Command: `/lunch-help`
   - Short Description: `도움말`
   - Request URL: `https://example.com` (아무거나)

### 2. Render 배포

1. https://render.com 접속 (GitHub 계정으로 로그인)
2. "New +" → **"Background Worker"** 선택 (Web Service 아님!)
3. GitHub 저장소 연결
4. 설정:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python slack_lunch_bot_advanced.py`
5. Environment 탭에서 환경 변수 추가:
   - `SLACK_BOT_TOKEN` = `xoxb-...`
   - `SLACK_APP_TOKEN` = `xapp-...`
6. "Create Background Worker" 클릭

### 3. 완료!

배포가 완료되면 봇이 24시간 작동하며, 워크스페이스의 모든 사람이 사용할 수 있습니다.

## 🛠️ 로컬 실행 (개발용)

```bash
# 패키지 설치
pip install -r requirements.txt

# 환경 변수 설정
export SLACK_BOT_TOKEN=xoxb-your-token
export SLACK_APP_TOKEN=xapp-your-token

# 실행
python slack_lunch_bot_advanced.py
```
