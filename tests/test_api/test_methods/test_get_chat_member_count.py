import pytest
from aiogram.api.methods import GetChatMemberCount, Request
from tests.mocked_bot import MockedBot


@pytest.mark.skip
class TestGetChatMemberCount:
    @pytest.mark.asyncio
    async def test_method(self, bot: MockedBot):
        prepare_result = bot.add_result_for(GetChatMemberCount, ok=True, result=None)

        response: int = await GetChatMemberCount(chat_id=...,)
        request: Request = bot.get_request()
        assert request.method == "getChatMemberCount"
        # assert request.data == {}
        assert response == prepare_result.result

    @pytest.mark.asyncio
    async def test_bot_method(self, bot: MockedBot):
        prepare_result = bot.add_result_for(GetChatMemberCount, ok=True, result=None)

        response: int = await bot.get_chat_member_count(chat_id=...,)
        request: Request = bot.get_request()
        assert request.method == "getChatMemberCount"
        # assert request.data == {}
        assert response == prepare_result.result
