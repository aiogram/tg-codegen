import pytest
from aiogram.api.methods import GetMyCommands, Request
from tests.mocked_bot import MockedBot


@pytest.mark.skip
class TestGetMyCommands:
    @pytest.mark.asyncio
    async def test_method(self, bot: MockedBot):
        prepare_result = bot.add_result_for(GetMyCommands, ok=True, result=None)

        response: List[BotCommand] = await GetMyCommands()
        request: Request = bot.get_request()
        assert request.method == "getMyCommands"
        # assert request.data == {}
        assert response == prepare_result.result

    @pytest.mark.asyncio
    async def test_bot_method(self, bot: MockedBot):
        prepare_result = bot.add_result_for(GetMyCommands, ok=True, result=None)

        response: List[BotCommand] = await bot.get_my_commands()
        request: Request = bot.get_request()
        assert request.method == "getMyCommands"
        # assert request.data == {}
        assert response == prepare_result.result
