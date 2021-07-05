import pytest
from aiogram.api.methods import EditChatInviteLink, Request
from tests.mocked_bot import MockedBot


@pytest.mark.skip
class TestEditChatInviteLink:
    @pytest.mark.asyncio
    async def test_method(self, bot: MockedBot):
        prepare_result = bot.add_result_for(EditChatInviteLink, ok=True, result=None)

        response: ChatInviteLink = await EditChatInviteLink(
            chat_id=..., invite_link=...,
        )
        request: Request = bot.get_request()
        assert request.method == "editChatInviteLink"
        # assert request.data == {}
        assert response == prepare_result.result

    @pytest.mark.asyncio
    async def test_bot_method(self, bot: MockedBot):
        prepare_result = bot.add_result_for(EditChatInviteLink, ok=True, result=None)

        response: ChatInviteLink = await bot.edit_chat_invite_link(
            chat_id=..., invite_link=...,
        )
        request: Request = bot.get_request()
        assert request.method == "editChatInviteLink"
        # assert request.data == {}
        assert response == prepare_result.result
