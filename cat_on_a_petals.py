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


@hook
def factory_allowed_llms(allowed, cat) -> List:
    allowed.append(LLMPetalsConfig)
    return allowed


# def install_dependencies():
#     bash_command = """
#     apt-get update && \
#     apt-get install git -y && \
#     python -m pip install --upgrade pip
#     mv /app/pyproject.toml /app/pyproject.toml.original && \
#     cp /app/cat/plugins/cat_on_a_petals/patches/pyproject.toml /app/pyproject.toml
#     """
#
#     os.system(bash_command)
#
#     bash_command = """
#     pip install -U pip && \
#     cd /app && \
#     pip install --force-reinstall --no-cache-dir . && \
#     pip install --no-cache-dir --ignore-installed --upgrade protobuf==5.28.3
#     """
#     os.system(bash_command)
#
#     log.info("Finished installing dependencies for Petals")


# @plugin
# def activated(plugin):
#     threads = []
#     t = threading.Thread(target=install_dependencies)
#     threads.append(t)
#
#     log.info("Installing dependencies for Petals")
#
#     for t in threads:
#         t.start()
#         t.join()


# @plugin
# def deactivated(plugin):
#     bash_command = """
#     mv /app/pyproject.toml.original /app/pyproject.toml
#     """
#     os.system(bash_command)
#
#     bash_command = """
#     pip install -U pip && \
#     cd /app && \
#     pip uninstall protobuf -y && \
#     pip install --force-reinstall --no-cache-dir .
#     """
#     os.system(bash_command)
#
#     log.info("Finished uninstalling dependencies for Petals")
