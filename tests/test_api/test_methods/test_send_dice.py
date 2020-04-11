import pytest
from aiogram.api.methods import Request, SendDice
from tests.mocked_bot import MockedBot


@pytest.mark.skip
class TestSendDice:
    @pytest.mark.asyncio
    async def test_method(self, bot: MockedBot):
        prepare_result = bot.add_result_for(SendDice, ok=True, result=None)

        response: Message = await SendDice(chat_id=...,)
        request: Request = bot.get_request()
        assert request.method == "sendDice"
        # assert request.data == {}
        assert response == prepare_result.result

    @pytest.mark.asyncio
    async def test_bot_method(self, bot: MockedBot):
        prepare_result = bot.add_result_for(SendDice, ok=True, result=None)

        response: Message = await bot.send_dice(chat_id=...,)
        request: Request = bot.get_request()
        assert request.method == "sendDice"
        # assert request.data == {}
        assert response == prepare_result.result
