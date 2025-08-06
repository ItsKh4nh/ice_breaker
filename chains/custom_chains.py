from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence
from langchain_openai import ChatOpenAI


from output_parsers import summary_parser, ice_breaker_parser, topics_of_interest_parser

llm = ChatOpenAI(temperature=0, model_name="gpt-4o-mini")
llm_creative = ChatOpenAI(temperature=1, model_name="gpt-4o-mini")


def get_summary_chain() -> RunnableSequence:
    summary_template = """
         Given the information about a person from linkedin {information}, I want you to create:
         1. a short summary
         2. two interesting facts about them
         
         IMPORTANT: You must respond with ONLY a valid JSON object in this exact format (no additional text):
         {{
             "summary": "your summary here",
             "facts": ["fact 1", "fact 2"]
         }}
     """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"],
        template=summary_template,
    )

    return summary_prompt_template | llm | summary_parser


def get_interests_chain() -> RunnableSequence:
    interesting_facts_template = """
         Given the information about a person from linkedin {information}, I want you to create:
         3 topics that might interest them
         
         IMPORTANT: You must respond with ONLY a valid JSON object in this exact format (no additional text):
         {{
             "topics_of_interest": ["topic 1", "topic 2", "topic 3"]
         }}
     """

    interesting_facts_prompt_template = PromptTemplate(
        input_variables=["information"],
        template=interesting_facts_template,
    )

    return interesting_facts_prompt_template | llm | topics_of_interest_parser


def get_ice_breaker_chain() -> RunnableSequence:
    ice_breaker_template = """
         Given the information about a person from linkedin {information}, I want you to create:
         2 creative ice breakers with them that are derived from their activity on Linkedin
         
         IMPORTANT: You must respond with ONLY a valid JSON object in this exact format (no additional text):
         {{
             "ice_breakers": ["ice breaker 1", "ice breaker 2"]
         }}
     """

    ice_breaker_prompt_template = PromptTemplate(
        input_variables=["information"],
        template=ice_breaker_template,
    )

    return ice_breaker_prompt_template | llm | ice_breaker_parser
