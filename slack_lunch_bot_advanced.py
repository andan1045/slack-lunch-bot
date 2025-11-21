import os
import random
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

# Slack 앱 초기화
app = App(token=os.environ.get("SLACK_BOT_TOKEN"))

# /lunch - 랜덤 메뉴 선택
@app.command("/lunch")
def lunch_command(ack, command, respond):
    ack()

    # 입력된 텍스트 확인
    input_text = command['text'].strip()

    # 입력된 메뉴가 있으면 쉼표로 분리
    if input_text:
        # 쉼표로 분리하고 공백 제거
        menus = [menu.strip() for menu in input_text.split(',') if menu.strip()]

        if not menus:
            respond("❌ 메뉴를 입력해주세요!\n사용법: `/lunch 메뉴1, 메뉴2, 메뉴3`\n예시: `/lunch 🍜 라면, 🍕 피자, 🍔 햄버거`")
            return

        selected_menu = random.choice(menus)

        # 채널 전체에 공개 (response_type을 in_channel로 설정)
        respond(
            response_type="in_channel",
            blocks=[
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": f"🎲 *오늘의 점심 메뉴는...*"
                    }
                },
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": f"# {selected_menu}"
                    }
                },
                {
                    "type": "context",
                    "elements": [
                        {
                            "type": "mrkdwn",
                            "text": f"맛있게 드세요! 🍽️ ({len(menus)}개 메뉴 중에서 선택)"
                        }
                    ]
                }
            ]
        )
    else:
        # 입력이 없으면 사용법 안내 (본인에게만)
        respond("❌ 메뉴를 입력해주세요!\n\n💡 *사용법*\n`/lunch 메뉴1, 메뉴2, 메뉴3`\n\n*예시*\n`/lunch 🍜 라면, 🍕 피자, 🍔 햄버거`")

# /lunch-help - 도움말
@app.command("/lunch-help")
def lunch_help_command(ack, command, respond):
    ack()

    respond(
        response_type="in_channel",
        blocks=[
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "*🍱 점심 메뉴 봇*"
                }
            },
            {
                "type": "divider"
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": (
                        "*📌 사용법*\n\n"
                        "`/lunch 메뉴1, 메뉴2, 메뉴3`\n"
                        "입력한 메뉴 중에서 하나를 랜덤으로 선택해드립니다.\n\n"
                        "*💡 예시*\n"
                        "`/lunch 된장찌개, 김치찌개, 순두부찌개`\n"
                        "`/lunch 중식, 한식, 일식, 양식`\n\n"
                        "*✨ 팁*\n"
                        "• 메뉴는 쉼표(,)로 구분해주세요\n"
                        "• 메뉴 개수는 제한이 없어요\n"
                    )
                }
            }
        ]
    )

# 앱 시작
if __name__ == "__main__":
    handler = SocketModeHandler(app, os.environ.get("SLACK_APP_TOKEN"))
    print("⚡️ 점심 메뉴 봇이 실행되었습니다!")
    handler.start()
