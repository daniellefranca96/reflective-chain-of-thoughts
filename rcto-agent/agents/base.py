from typing import Sequence

from langchain.agents import ZeroShotAgent
from langchain.chains import LLMChain
from langchain.tools.base import BaseTool


class RCTOAgent(ZeroShotAgent):

    def __init(
            self,
            llm_chain: LLMChain,
            tools: Sequence[BaseTool]):
        super().__init__(llm_chain=llm_chain, tools=tools)

    @property
    def llm_prefix(self) -> str:
        """Prefix to append the llm call with."""
        return "Progress Check:"

