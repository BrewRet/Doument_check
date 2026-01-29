from datetime import date
from typing import Optional
from pydantic import BaseModel, Field, field_validator
from re import compile, match

class DocumentSend(BaseModel):
    """Схема для отправления документа на сервер"""


    date_of_birth: str = Field(
        description="Дата рождения", examples=["22.08.1977"]
    )
    doc_number: str = Field(
        description="Номер документа", examples=["0525 185673"]
    )
    mrz: str = Field(
        description="МЧЗ строка", examples=["""PNRUS<<IVANOV<<IVAN<<IVANOVICH<<<<<<<<<<<<<<
                                            \\n0521856730RUS7708220M4510220<<<<<<<<<<<<<<44"""]
    )

    @field_validator("date_of_birth")
    @classmethod
    def date_of_birth_is_valid(cls, v: str) -> str:
        try:
            date.strftime(v, "%d.%m.%Y")
            return v
        except ValueError:
            raise ValueError("Некорректная дата")
        

    @field_validator("mrz")
    @classmethod
    def mrz_is_valid(cls, v: str) -> str:
        mrz_pattern = compile(r"[A-Z<2-46-9]{44}\n[0-9]{10}RUS[0-9]{7}(M|F)[0-9]{7}[0-9<]{16}")
        if v is not mrz_pattern.match(v):
            raise ValueError("Некорректная МЧЗ")
        return v
    

    @field_validator("doc_number")
    @classmethod
    def doc_number_is_valid(cls, v: str) -> str:
        doc_number_pattern = compile(r"[0-9]{4} [0-9]{6}")
        if v is not doc_number_pattern.match(v):
            raise ValueError("Некоррктный номер документа")
        return v
    