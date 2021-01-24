import pytest
from aiogram.api.methods import CopyMessage, Request
from tests.mocked_bot import MockedBot


@pytest.mark.skip
class TestCopyMessage:
    @pytest.mark.asyncio
    async def test_method(self, bot: MockedBot):
        prepare_result = bot.add_result_for(CopyMessage, ok=True, result=None)

        response: MessageId = await CopyMessage(
            chat_id=..., from_chat_id=..., message_id=...,
        )
        request: Request = bot.get_request()
        assert request.method == "copyMessage"
        # assert request.data == {}
        assert response == prepare_result.result

    @pytest.mark.asyncio
    async def test_bot_method(self, bot: MockedBot):
        prepare_result = bot.add_result_for(CopyMessage, ok=True, result=None)

        response: MessageId = await bot.copy_message(
            chat_id=..., from_chat_id=..., message_id=...,
        )
        request: Request = bot.get_request()
        assert request.method == "copyMessage"
        # assert request.data == {}
        assert response == prepare_result.result
