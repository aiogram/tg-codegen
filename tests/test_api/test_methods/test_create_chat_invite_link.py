import pytest
from aiogram.api.methods import CreateChatInviteLink, Request
from tests.mocked_bot import MockedBot


@pytest.mark.skip
class TestCreateChatInviteLink:
    @pytest.mark.asyncio
    async def test_method(self, bot: MockedBot):
        prepare_result = bot.add_result_for(CreateChatInviteLink, ok=True, result=None)

        response: ChatInviteLink = await CreateChatInviteLink(chat_id=...,)
        request: Request = bot.get_request()
        assert request.method == "createChatInviteLink"
        # assert request.data == {}
        assert response == prepare_result.result

    @pytest.mark.asyncio
    async def test_bot_method(self, bot: MockedBot):
        prepare_result = bot.add_result_for(CreateChatInviteLink, ok=True, result=None)

        response: ChatInviteLink = await bot.create_chat_invite_link(chat_id=...,)
        request: Request = bot.get_request()
        assert request.method == "createChatInviteLink"
        # assert request.data == {}
        assert response == prepare_result.result
