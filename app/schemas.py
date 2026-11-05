from pydantic import BaseModel, HttpUrl
from datetime import datetime

class MonitorBase(BaseModel):
    url: HttpUrl
    name: str
    interval_seconds: int = 60
    timeout_ms: int = 5000

class MonitorCreate(MonitorBase):
    pass

class MonitorOut(MonitorBase):
    id: int
    created_at: datetime

    model_config = {"from_attributes" : True}