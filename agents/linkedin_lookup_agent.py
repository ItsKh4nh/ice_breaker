import os
import re

from langchain import hub
from langchain.agents import (
    create_react_agent,
    AgentExecutor,
)
from langchain_core.tools import Tool
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from tools.tools import get_profile_url_tavily

load_dotenv()


def lookup(name: str) -> str:
    llm = ChatOpenAI(
        temperature=0,
        model_name="gpt-4o-mini",
        openai_api_key=os.environ["OPENAI_API_KEY"],
    )
    template = """given the full name {name_of_person} I want you to get me a link to their LinkedIn profile page. Your answer should contain only a LinkedIn profile URL in the format: https://www.linkedin.com/in/username/. Do NOT return LinkedIn post URLs (urls containing /posts/) or any other format. Only return the direct profile URL."""

    prompt_template = PromptTemplate(
        template=template, input_variables=["name_of_person"]
    )
    tools_for_agent = [
        Tool(
            name="Crawl Google 4 linkedin profile page",
            func=get_profile_url_tavily,
            description="useful for when you need to get the LinkedIn profile page URL (format: linkedin.com/in/username). Do NOT use for LinkedIn posts or other formats.",
        )
    ]

    react_prompt = hub.pull("hwchase17/react")
    agent = create_react_agent(llm=llm, tools=tools_for_agent, prompt=react_prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tools_for_agent, verbose=True)

    result = agent_executor.invoke(
        input={"input": prompt_template.format_prompt(name_of_person=name)}
    )

    linked_profile_url = result["output"]

    # Validate and clean the URL to ensure it's a proper LinkedIn profile URL
    validated_url = validate_linkedin_profile_url(linked_profile_url)
    if not validated_url:
        raise ValueError(f"Could not find a valid LinkedIn profile URL for {name}")

    return validated_url


def validate_linkedin_profile_url(url: str) -> str:
    """
    Validates and extracts a proper LinkedIn profile URL from the response.
    Returns the clean profile URL or empty string if not valid.
    """
    if not url:
        return ""

    # Extract LinkedIn profile URLs using regex
    # Look for /in/ pattern which indicates a profile URL
    profile_pattern = r"https://www\.linkedin\.com/in/[a-zA-Z0-9\-_%]+/?"
    matches = re.findall(profile_pattern, url)

    if matches:
        # Return the first valid profile URL found
        clean_url = matches[0].rstrip("/")
        # Ensure it doesn't contain /posts/ (which would be a post URL)
        if "/posts/" not in clean_url:
            return clean_url

    # If no /in/ URLs found, try to extract any linkedin.com URL and check if it's convertible
    general_pattern = r"https://www\.linkedin\.com/[^\s\)]+/?"
    general_matches = re.findall(general_pattern, url)

    for match in general_matches:
        # Skip post URLs
        if "/posts/" in match:
            continue
        # If it's a /pub/ URL, we can't easily convert it
        if "/pub/" in match:
            continue
        # If it's already a profile URL, return it
        if "/in/" in match:
            return match.rstrip("/")

    return ""
