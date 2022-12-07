import requests
import consts


class SlackService:

    def _send_slack_webhook(self, webhook_url: str, blocks: dict) -> None:
        payload = {"blocks": blocks}
        response = requests.post(webhook_url, json=payload)
        print(response.text)

    def _make_block_payload(self, message: str) -> dict:
        return {"type": "section", "text": {"type": "mrkdwn", "text": message}}

    def _make_header_payload(self, message: str) -> dict:
        return {"type": "header", "text": {"type": "plain_text", "text": message, "emoji": True}}

    def _make_driver_payload(self) -> dict:
        return {"type": "divider"}
    
    def _make_footer_payload(self) -> dict:
        return {
            "type": "context", 
            "elements": [
                {"type": "image", "image_url": consts.APP_LOGO_IMAGE_URL, "alt_text": consts.APP_NAME},
                {"type": "mrkdwn", "text": f"<https://github.com/croquiscom/{consts.APP_NAME}|{consts.APP_NAME}> • Github Actions"}
            ]
    }