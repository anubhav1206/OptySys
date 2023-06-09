from enum import Enum

from bson import ObjectId

"""
JSON Friendly ObjectId
"""


class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")


"""
Access level for an organization member (Enum)
"""


class Role(str, Enum):
    ADMIN = "admin"
    MEMBER = "member"


class SocialLinks(str, Enum):
    RESUME = "resume"
    LINKEDIN = "linkedin"
    GITHUB = "github"
    TWITTER = "twitter"
    BEHANCE = "behance"
    DRIBBLE = "dribble"


class Experience(str, Enum):
    TITLE: str
    COMPANY: str
    DESCRIPTION: str