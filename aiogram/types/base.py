from pydantic import BaseConfig, BaseModel


class TelegramObject(BaseModel):
    class Config(BaseConfig):
        use_enum_values = True
        orm_mode = True
