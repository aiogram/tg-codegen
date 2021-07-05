import pytest
from aiogram.api.methods import BanChatMember, Request
from tests.mocked_bot import MockedBot


@pytest.mark.skip
class TestBanChatMember:
    @pytest.mark.asyncio
    async def test_method(self, bot: MockedBot):
        prepare_result = bot.add_result_for(BanChatMember, ok=True, result=None)

        response: bool = await BanChatMember(
            chat_id=..., user_id=...,
        )
        request: Request = bot.get_request()
        assert request.method == "banChatMember"
        # assert request.data == {}
        assert response == prepare_result.result

    @pytest.mark.asyncio
    async def test_bot_method(self, bot: MockedBot):
        prepare_result = bot.add_result_for(BanChatMember, ok=True, result=None)

        response: bool = await bot.ban_chat_member(
            chat_id=..., user_id=...,
        )
        request: Request = bot.get_request()
        assert request.method == "banChatMember"
        # assert request.data == {}
        assert response == prepare_result.result
