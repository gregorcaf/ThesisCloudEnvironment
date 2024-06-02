from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class PutDataRequest(_message.Message):
    __slots__ = ("key", "value")
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    key: str
    value: str
    def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...

class PutDataResponse(_message.Message):
    __slots__ = ("key", "responseCode", "responseMessage")
    KEY_FIELD_NUMBER: _ClassVar[int]
    RESPONSECODE_FIELD_NUMBER: _ClassVar[int]
    RESPONSEMESSAGE_FIELD_NUMBER: _ClassVar[int]
    key: str
    responseCode: int
    responseMessage: str
    def __init__(self, key: _Optional[str] = ..., responseCode: _Optional[int] = ..., responseMessage: _Optional[str] = ...) -> None: ...

class GetDataRequest(_message.Message):
    __slots__ = ("key",)
    KEY_FIELD_NUMBER: _ClassVar[int]
    key: str
    def __init__(self, key: _Optional[str] = ...) -> None: ...

class GetDataResponse(_message.Message):
    __slots__ = ("key", "value", "responseCode", "responseMessage")
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    RESPONSECODE_FIELD_NUMBER: _ClassVar[int]
    RESPONSEMESSAGE_FIELD_NUMBER: _ClassVar[int]
    key: str
    value: str
    responseCode: int
    responseMessage: str
    def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ..., responseCode: _Optional[int] = ..., responseMessage: _Optional[str] = ...) -> None: ...
