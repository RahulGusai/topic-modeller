from pydantic import BaseModel


class RequestItem(BaseModel):
    url: str
    num_topics: int = 5  # Default value of 5
