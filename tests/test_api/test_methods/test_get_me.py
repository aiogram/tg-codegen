import pytest

from aiogram.api.methods import GetMe, Request
from tests.mocked_bot import MockedBot


@pytest.mark.skip
class TestGetMe:
    @pytest.mark.asyncio
    async def test_method(self, bot: MockedBot):
        prepare_result = bot.add_result_for(GetMe, ok=True, result=None)

        response: User = await GetMe()
        request: Request = bot.get_request()
        assert request.method == "getMe"
        # assert request.data == {}
        assert response == prepare_result.result

    @pytest.mark.asyncio
    async def test_bot_method(self, bot: MockedBot):
        prepare_result = bot.add_result_for(GetMe, ok=True, result=None)

        response: User = await bot.get_me()
        request: Request = bot.get_request()
        assert request.method == "getMe"
        # assert request.data == {}
        assert response == prepare_result.result
