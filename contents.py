from pathlib import Path

import yaml
from pydantic import BaseModel, AnyUrl


class Github(BaseModel):
    username: str
    url: AnyUrl


class Contact(BaseModel):
    email: str
    phone: str


class BioSection(BaseModel):
    name: str
    location: str
    nationality: str
    contact: Contact
    github: Github


class LanguageItem(BaseModel):
    name: str
    level: str


class EducationItem(BaseModel):
    institution: str
    degree: str
    years: str


class WorkItem(BaseModel):
    company: str
    title: str
    years: str
    description: str


class SkillListItem(BaseModel):
    label: str
    items: list[str]


class CVContents(BaseModel):
    bio: BioSection
    language: list[LanguageItem]
    education: list[EducationItem]
    work: list[WorkItem]
    skills: list[SkillListItem]


def load_cv(contents_yaml_path: Path) -> CVContents:
    with open(contents_yaml_path) as f:
        return CVContents.model_validate(yaml.safe_load(f))
