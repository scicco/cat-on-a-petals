from cat.factory.llm import LLMSettings
from cat.mad_hatter.decorators import hook
from typing import List, Type
from pydantic import ConfigDict
from langchain_community.llms import Petals


class LLMPetalsConfig(LLMSettings):
    model_name: str
    huggingface_api_key: str
    #max_new_tokens: int = 256
    #top_p: float = 0.9
    #do_sample: bool = True
    #temperature: float = 0.8

    _pyclass: Type = Petals
    model_config = ConfigDict(
        json_schema_extra={
            "humanReadableName": "Petals",
            "description": "Configuration for Petals",
            "link": "https://github.com/bigscience-workshop/petals",
        }
    )


@hook
def factory_allowed_llms(allowed, cat) -> List:
    allowed.append(LLMPetalsConfig)
    return allowed
