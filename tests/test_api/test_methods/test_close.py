import pytest
from aiogram.api.methods import Close, Request
from tests.mocked_bot import MockedBot


@pytest.mark.skip
class TestClose:
    @pytest.mark.asyncio
    async def test_method(self, bot: MockedBot):
        prepare_result = bot.add_result_for(Close, ok=True, result=None)

        response: bool = await Close()
        request: Request = bot.get_request()
        assert request.method == "close"
        # assert request.data == {}
        assert response == prepare_result.result

    @pytest.mark.asyncio
    async def test_bot_method(self, bot: MockedBot):
        prepare_result = bot.add_result_for(Close, ok=True, result=None)

        response: bool = await bot.close()
        request: Request = bot.get_request()
        assert request.method == "close"
        # assert request.data == {}
        assert response == prepare_result.result
