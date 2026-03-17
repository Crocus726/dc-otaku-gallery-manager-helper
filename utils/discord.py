import requests

def send_discord_message(sending_content, webhook_url):
    sending_data = {"content": sending_content}
    try:
        response = requests.post(webhook_url, json = sending_data)
        if response.status_code == 204:
            print("디스코드 메시지 전송 성공")
        else:
            print("디스코드 메시지 전송 실패")
            print(f"응답 내용: {response.text}")
    except Exception as e:
        print(f"디스코드 메시지 전송 오류: {e}")
