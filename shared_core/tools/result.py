from typing import Any

from pydantic import BaseModel


class ToolResult(BaseModel):

    success: bool

    message: str

    data: Any | None = None