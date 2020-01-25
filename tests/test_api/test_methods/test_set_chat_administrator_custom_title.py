import pytest
from aiogram.api.methods import Request, SetChatAdministratorCustomTitle
from tests.mocked_bot import MockedBot


@pytest.mark.skip
class TestSetChatAdministratorCustomTitle:
    @pytest.mark.asyncio
    async def test_method(self, bot: MockedBot):
        prepare_result = bot.add_result_for(SetChatAdministratorCustomTitle, ok=True, result=None)

        response: bool = await SetChatAdministratorCustomTitle(
            chat_id=..., user_id=..., custom_title=...,
        )
        request: Request = bot.get_request()
        assert request.method == "setChatAdministratorCustomTitle"
        # assert request.data == {}
        assert response == prepare_result.result

    @pytest.mark.asyncio
    async def test_bot_method(self, bot: MockedBot):
        prepare_result = bot.add_result_for(SetChatAdministratorCustomTitle, ok=True, result=None)

        response: bool = await bot.set_chat_administrator_custom_title(
            chat_id=..., user_id=..., custom_title=...,
        )
        request: Request = bot.get_request()
        assert request.method == "setChatAdministratorCustomTitle"
        # assert request.data == {}
        assert response == prepare_result.result
