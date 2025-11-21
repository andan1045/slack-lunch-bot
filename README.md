# Slack Lunch Bot

점심 메뉴를 랜덤으로 추천해주는 Slack 봇입니다.

## 기능

- `/lunch` - 랜덤으로 점심 메뉴 추천
- `/lunch-add 메뉴이름` - 메뉴 추가
- `/lunch-remove 메뉴이름` - 메뉴 삭제
- `/lunch-list` - 전체 메뉴 목록 보기
- `/lunch-help` - 도움말 보기

## 배포 방법

### Render 배포

1. GitHub에 코드 푸시
2. Render.com에서 New Web Service 생성
3. GitHub 저장소 연결
4. 환경 변수 설정:
   - `SLACK_BOT_TOKEN`
   - `SLACK_APP_TOKEN`
5. Deploy

## 환경 변수

```
SLACK_BOT_TOKEN=xoxb-your-bot-token
SLACK_APP_TOKEN=xapp-your-app-token
```
