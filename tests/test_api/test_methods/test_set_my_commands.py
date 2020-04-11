import pytest
from aiogram.api.methods import Request, SetMyCommands
from tests.mocked_bot import MockedBot


@pytest.mark.skip
class TestSetMyCommands:
    @pytest.mark.asyncio
    async def test_method(self, bot: MockedBot):
        prepare_result = bot.add_result_for(SetMyCommands, ok=True, result=None)

        response: bool = await SetMyCommands(commands=...,)
        request: Request = bot.get_request()
        assert request.method == "setMyCommands"
        # assert request.data == {}
        assert response == prepare_result.result

    @pytest.mark.asyncio
    async def test_bot_method(self, bot: MockedBot):
        prepare_result = bot.add_result_for(SetMyCommands, ok=True, result=None)

        response: bool = await bot.set_my_commands(commands=...,)
        request: Request = bot.get_request()
        assert request.method == "setMyCommands"
        # assert request.data == {}
        assert response == prepare_result.result
