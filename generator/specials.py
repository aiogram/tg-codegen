METHODS_EXTRA = {
    "answerInlineQuery": """prepare_parse_mode(bot, data["results"])
return Request(method="answerInlineQuery", data=data)""",
    "editMessageMedia": """prepare_parse_mode(bot, data["media"])
files: Dict[str, InputFile] = {}
prepare_media_file(data=data, files=files)

return Request(method="editMessageMedia", data=data, files=files)""",
    "sendMediaGroup": """prepare_parse_mode(bot, data["media"])

files: Dict[str, InputFile] = {}
prepare_input_media(data, files)

return Request(method="sendMediaGroup", data=data, files=files)"""
}


EXTRA = {
    'methods': METHODS_EXTRA
}
