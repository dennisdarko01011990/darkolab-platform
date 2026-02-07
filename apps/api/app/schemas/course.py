from __future__ import annotations

from datetime import datetime
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field


class ModuleCreate(BaseModel):
    course_id: int
    title: str
    position: int = 1


class ModuleRead(BaseModel):
    id: int
    course_id: int
    title: str
    position: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class CourseCreate(BaseModel):
    title: str
    slug: str
    level: Literal["beginner", "intermediate", "advanced"] = "beginner"
    description: str | None = None
    is_published: bool = False


class CourseRead(BaseModel):
    id: int
    title: str
    slug: str
    level: Literal["beginner", "intermediate", "advanced"]
    description: str | None = None
    is_published: bool
    created_at: datetime
    updated_at: datetime
    modules: list[ModuleRead] = Field(default_factory=list)

    model_config = ConfigDict(from_attributes=True)
