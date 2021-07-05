import pytest
from aiogram.api.methods import DeleteMyCommands, Request
from tests.mocked_bot import MockedBot


@pytest.mark.skip
class TestDeleteMyCommands:
    @pytest.mark.asyncio
    async def test_method(self, bot: MockedBot):
        prepare_result = bot.add_result_for(DeleteMyCommands, ok=True, result=None)

        response: bool = await DeleteMyCommands()
        request: Request = bot.get_request()
        assert request.method == "deleteMyCommands"
        # assert request.data == {}
        assert response == prepare_result.result

    @pytest.mark.asyncio
    async def test_bot_method(self, bot: MockedBot):
        prepare_result = bot.add_result_for(DeleteMyCommands, ok=True, result=None)

        response: bool = await bot.delete_my_commands()
        request: Request = bot.get_request()
        assert request.method == "deleteMyCommands"
        # assert request.data == {}
        assert response == prepare_result.result
