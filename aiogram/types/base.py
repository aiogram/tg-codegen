from pydantic import BaseConfig, BaseModel, Extra


class TelegramObject(BaseModel):
    class Config(BaseConfig):
        use_enum_values = True
        orm_mode = True
        extra = Extra.allow
