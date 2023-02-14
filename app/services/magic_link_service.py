from jose import jwt
from requests import PreparedRequest
from app.schemas.magic_link import MagicLink, MagicLinkTokenPayload
from app.services.smtp_client import SMTPClient

class MagicLinkService:
    def __init__(self, email_client: SMTPClient, magic_link_base_url: str, jwt_secret: str, magic_link_from_email: str):
        self.email_client = email_client
        self.magic_link_base_url = magic_link_base_url
        self.jwt_secret = jwt_secret
        self.from_email = magic_link_from_email

    def generate_magic_link(self, payload = MagicLinkTokenPayload) -> MagicLink:
        token = jwt.encode(payload.dict(), self.jwt_secret, algorithm="HS256")
        req = PreparedRequest()
        req.prepare_url(self.magic_link_base_url, {"token": token})

        return MagicLink(
            url=req.url,
            token=token
        )

    def send_magic_link(self, email: str, magic_link: MagicLink) -> None:
        self.email_client.send_email(self.from_email, email, "Log in with Magic Link", f"Please use this link {magic_link.url} to log in into Cookbug.")