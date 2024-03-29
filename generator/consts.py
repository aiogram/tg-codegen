import re
from typing import List, Dict

DOCS_URL = "https://core.telegram.org/bots/api"

RE_FLAGS = re.IGNORECASE
ANCHOR_HEADER_PATTERN = re.compile(r"^h([34])$")
RETURN_PATTERNS = [
    re.compile(
        r"(?P<type>[a-z]+) is returned, otherwise (?P<other>[a-zA-Z]+) is returned",
        flags=RE_FLAGS,
    ),
    re.compile(
        r"returns the edited (?P<type>[a-z]+), otherwise returns (?P<other>[a-zA-Z]+)",
        flags=RE_FLAGS,
    ),
    re.compile(
        r"On success, the stopped (?P<type>[a-z]+) with the final results is returned",
        flags=RE_FLAGS,
    ),
    re.compile(
        r"On success, an (?P<type>array of [a-z]+)s that were sent is returned", flags=RE_FLAGS
    ),
    re.compile(r"Returns the (?P<type>[a-z]+) of the sent message on success", flags=RE_FLAGS),
    re.compile(r"(?P<type>Array of [a-z]+) objects", flags=RE_FLAGS),
    re.compile(r"Returns (?P<type>Array of [a-z]+) on success", flags=RE_FLAGS),
    re.compile(r"a (?P<type>[a-z]+) object", flags=RE_FLAGS),
    re.compile(r"Returns (?P<type>[a-z]+) on success", flags=RE_FLAGS),
    re.compile(r"(?P<type>[a-z]+) on success", flags=RE_FLAGS),
    re.compile(r"(?P<type>[a-z]+) is returned", flags=RE_FLAGS),
    re.compile(r"Returns the [a-z ]+ as (?P<type>[a-z]+) object", flags=RE_FLAGS),
    re.compile(r"Returns (?P<type>[a-z]+)", flags=RE_FLAGS),
]
ALIASED_TYPES = {
    "ChatMember": "Union[ChatMemberOwner, ChatMemberAdministrator, ChatMemberMember,"
    " ChatMemberRestricted, ChatMemberLeft, ChatMemberBanned]"
}
ALIASED_TYPES_PATTERNS: Dict[re.Pattern, str] = {
    re.compile(f"(\\W|^)(ChatMember)(\\W|$)", flags=RE_FLAGS): value
    for key, value in ALIASED_TYPES.items()
}

BUILTIN_TYPES = {
    "String": "str",
    "Integer": "int",
    "Int": "int",
    "Float": "float",
    "Boolean": "bool",
}
READ_MORE_PATTERN = re.compile(
    r" ((More info on|More about)([\W\w]+»)|»)", flags=re.MULTILINE & re.IGNORECASE
)
SYMBOLS_MAP = {"“": "'", "”": "'"}

SPECIAL_CLIENT_SUBTYPES = {
    "InlineQueryResult": "type",
    "InputMedia": "type",
    "PassportElementError": "source",
    "BotCommandScope": "type",
    "ChatMember": "status",
}
SPECIAL_CLIENT_SUBTYPES_EXCLUDE = {"ChatMemberUpdated"}

SPECIAL_SERVER_SUBTYPES = {("Input", "MessageContent"): "InputMessageContent"}

TELEGRAM_TYPE_PATTERN = r"(^|\[| ){type}(\]|$|,)"


REF_LINKS = {
    "#sending-files": "sending-files",
}
