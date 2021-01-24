import pytest
from aiogram.api.methods import Request, UnpinAllChatMessages
from tests.mocked_bot import MockedBot


@pytest.mark.skip
class TestUnpinAllChatMessages:
    @pytest.mark.asyncio
    async def test_method(self, bot: MockedBot):
        prepare_result = bot.add_result_for(UnpinAllChatMessages, ok=True, result=None)

        response: bool = await UnpinAllChatMessages(chat_id=...,)
        request: Request = bot.get_request()
        assert request.method == "unpinAllChatMessages"
        # assert request.data == {}
        assert response == prepare_result.result

    @pytest.mark.asyncio
    async def test_bot_method(self, bot: MockedBot):
        prepare_result = bot.add_result_for(UnpinAllChatMessages, ok=True, result=None)

        response: bool = await bot.unpin_all_chat_messages(chat_id=...,)
        request: Request = bot.get_request()
        assert request.method == "unpinAllChatMessages"
        # assert request.data == {}
        assert response == prepare_result.result
