
from pydantic import BaseModel


class ProfileSummary(BaseModel):

    name: str

    headline: str

    location: str


class ProfileStatistics(BaseModel):

    followers: int

    connections: int

    posts: int


class ProfileReport(BaseModel):

    summary: ProfileSummary

    statistics: ProfileStatistics