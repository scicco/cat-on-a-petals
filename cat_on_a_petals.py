from cat.factory.llm import LLMSettings
from cat.mad_hatter.decorators import hook
from cat.mad_hatter.decorators import plugin
from cat.log import log
from typing import List, Type
from pydantic import ConfigDict
from langchain_community.llms import Petals
import os
import threading


class LLMPetalsConfig(LLMSettings):
    model_name: str
    huggingface_api_key: str
    # max_new_tokens: int = 256
    # top_p: float = 0.9
    # do_sample: bool = True
    # temperature: float = 0.8

    _pyclass: Type = Petals
    model_config = ConfigDict(
        json_schema_extra={
            "humanReadableName": "Petals",
            "description": "Configuration for Petals",
            "link": "https://github.com/bigscience-workshop/petals",
        }
    )


def install_dependencies():
    bash_command = """
    apt-get update && \
    apt-get install git -y && \
    python -m pip install --upgrade pip
    """

    os.system(bash_command)

    bash_command = """
    python -m pip install --no-cache-dir --upgrade fastembed==0.3.6 && \
    python -m pip install --no-cache-dir --upgrade typing-extensions>=4.9.0 && \
    python -m pip install --no-cache-dir --upgrade qdrant_client==1.11.0 && \
    python -m pip install --no-cache-dir --upgrade protobuf==4.25.5 && \
    python -m pip install --no-cache-dir --upgrade pydantic>=2.4.2 && \
    python -m pip install --no-cache-dir --upgrade huggingface-hub>=0.20.3 && \
    python -m pip install --no-cache-dir --upgrade unstructured>=0.12.6 && \
    python -m pip install --no-cache-dir git+https://github.com/bigscience-workshop/petals && \
    python -m pip install --no-cache-dir git+https://github.com/learning-at-home/hivemind.git@213bff98a62accb91f254e2afdccbf1d69ebdea9 && \
    python -m pip install --no-cache-dir --upgrade protobuf
    """
    os.system(bash_command)
    log.info("Finished installing dependencies for Petals")


@plugin
def activated(plugin):
    threads = []
    t = threading.Thread(target=install_dependencies)
    threads.append(t)

    log.info("Installing dependencies for Petals")

    for t in threads:
        t.start()
        t.join()


@hook
def factory_allowed_llms(allowed, cat) -> List:
    allowed.append(LLMPetalsConfig)
    return allowed
