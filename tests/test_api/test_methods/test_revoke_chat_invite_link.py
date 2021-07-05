import pytest
from aiogram.api.methods import Request, RevokeChatInviteLink
from tests.mocked_bot import MockedBot


@pytest.mark.skip
class TestRevokeChatInviteLink:
    @pytest.mark.asyncio
    async def test_method(self, bot: MockedBot):
        prepare_result = bot.add_result_for(RevokeChatInviteLink, ok=True, result=None)

        response: ChatInviteLink = await RevokeChatInviteLink(
            chat_id=..., invite_link=...,
        )
        request: Request = bot.get_request()
        assert request.method == "revokeChatInviteLink"
        # assert request.data == {}
        assert response == prepare_result.result

    @pytest.mark.asyncio
    async def test_bot_method(self, bot: MockedBot):
        prepare_result = bot.add_result_for(RevokeChatInviteLink, ok=True, result=None)

        response: ChatInviteLink = await bot.revoke_chat_invite_link(
            chat_id=..., invite_link=...,
        )
        request: Request = bot.get_request()
        assert request.method == "revokeChatInviteLink"
        # assert request.data == {}
        assert response == prepare_result.result
