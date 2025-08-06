# from langchain_community.utilities import SerpAPIWrapper
# class CustomSerpAPIWrapper(SerpAPIWrapper):
#     def __init__(self):
#         super(CustomSerpAPIWrapper, self).__init__()
#
#     @staticmethod
#     def _process_response(res: dict) -> str:
#         """Process response from SerpAPI."""
#         if "error" in res.keys():
#             raise ValueError(f"Got error from SerpAPI: {res['error']}")
#         if "answer_box" in res.keys() and "answer" in res["answer_box"].keys():
#             toret = res["answer_box"]["answer"]
#         elif "answer_box" in res.keys() and "snippet" in res["answer_box"].keys():
#             toret = res["answer_box"]["snippet"]
#         elif (
#             "answer_box" in res.keys()
#             and "snippet_highlighted_words" in res["answer_box"].keys()
#         ):
#             toret = res["answer_box"]["snippet_highlighted_words"][0]
#         elif (
#             "sports_results" in res.keys()
#             and "game_spotlight" in res["sports_results"].keys()
#         ):
#             toret = res["sports_results"]["game_spotlight"]
#         elif (
#             "knowledge_graph" in res.keys()
#             and "description" in res["knowledge_graph"].keys()
#         ):
#             toret = res["knowledge_graph"]["description"]
#         elif "snippet" in res["organic_results"][0].keys():
#             toret = res["organic_results"][0]["link"]
#
#         else:
#             toret = "No good search result found"
#         return toret
#
#
# def get_profile_url(name: str):
#     """Searches for Linkedin Profile Page."""
#     search = CustomSerpAPIWrapper()
#     res = search.run(f"{name}")
#     return res

from langchain_community.tools.tavily_search import TavilySearchResults
import re


def get_profile_url_tavily(name: str):
    """Searches for Linkedin Profile Page."""
    search = TavilySearchResults()

    # First try specific profile search
    res = search.run(f"{name} site:linkedin.com/in/")

    # Extract and filter results to ensure we get profile URLs
    filtered_result = filter_linkedin_profile_results(res, name)

    if filtered_result:
        return filtered_result

    # If no results from profile search, try a broader search but filter results
    res = search.run(f"{name} LinkedIn profile")
    return filter_linkedin_profile_results(res, name)


def filter_linkedin_profile_results(search_results, name: str):
    """Filter search results to prioritize LinkedIn profile URLs."""
    if not search_results:
        return search_results

    # Convert to string if it's a list
    if isinstance(search_results, list):
        search_text = " ".join(str(item) for item in search_results)
    else:
        search_text = str(search_results)

    # Look for LinkedIn profile URLs (with /in/ pattern)
    profile_pattern = r"https://www\.linkedin\.com/in/[a-zA-Z0-9\-_%]+/?"
    profile_urls = re.findall(profile_pattern, search_text)

    # If we found profile URLs, prioritize them
    if profile_urls:
        # Return the search results but add emphasis on the profile URLs found
        return f"LinkedIn profile URLs found: {', '.join(profile_urls[:3])}. Original search results: {search_results}"

    # If no profile URLs found, return original results
    return search_results
