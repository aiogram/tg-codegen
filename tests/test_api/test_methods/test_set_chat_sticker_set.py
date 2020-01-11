import pytest
from aiogram.api.methods import Request, SetChatStickerSet
from tests.mocked_bot import MockedBot


@pytest.mark.skip
class TestSetChatStickerSet:
    @pytest.mark.asyncio
    async def test_method(self, bot: MockedBot):
        prepare_result = bot.add_result_for(SetChatStickerSet, ok=True, result=None)

        response: bool = await SetChatStickerSet(
            chat_id=..., sticker_set_name=...,
        )
        request: Request = bot.get_request()
        assert request.method == "setChatStickerSet"
        # assert request.data == {}
        assert response == prepare_result.result

    @pytest.mark.asyncio
    async def test_bot_method(self, bot: MockedBot):
        prepare_result = bot.add_result_for(SetChatStickerSet, ok=True, result=None)

        response: bool = await bot.set_chat_sticker_set(
            chat_id=..., sticker_set_name=...,
        )
        request: Request = bot.get_request()
        assert request.method == "setChatStickerSet"
        # assert request.data == {}
        assert response == prepare_result.result
