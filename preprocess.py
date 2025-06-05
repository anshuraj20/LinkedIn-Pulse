import json
import re
from llm_helper import llm
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException


def clean_text(text):
    """Removes surrogate Unicode characters that cause encoding errors."""
    return re.sub(r"[\ud800-\udfff]", "", text)


def process_posts(raw_file_path, processed_file_path=None):
    with open(raw_file_path, encoding='utf-8', errors='replace') as file:
        posts = json.load(file)
        enriched_posts = []
        for post in posts:
            post_text = clean_text(post['text'])  # Clean text before processing
            metadata = extract_metadata(post_text)
            post_with_metadata = post | metadata
            enriched_posts.append(post_with_metadata)

    unified_tags = get_unified_tags(enriched_posts)
    for post in enriched_posts:
        current_tags = post['tags']
        new_tags = {unified_tags.get(tag, tag) for tag in current_tags}  # Avoid KeyError
        post['tags'] = list(new_tags)

    with open(processed_file_path, mode="w", encoding="utf-8", errors="replace") as outfile:
        json.dump(enriched_posts, outfile, indent=4, ensure_ascii=False)


def extract_metadata(post):
    template = '''
    You are given a LinkedIn post. You need to extract number of lines, language of the post and tags.
    1. Return a valid JSON. No preamble. 
    2. JSON object should have exactly three keys: line_count, language and tags. 
    3. tags is an array of text tags. Extract maximum two tags.
    4. Language should be English or Hinglish (Hinglish means Hindi + English)
    
    Here is the actual post on which you need to perform this task:  
    {post}
    '''

    pt = PromptTemplate.from_template(template)
    chain = pt | llm
    response = chain.invoke({"post": post})

    try:
        json_parser = JsonOutputParser()
        res = json_parser.parse(response.content)
    except OutputParserException:
        raise OutputParserException("Context too big. Unable to parse metadata.")
    return res


def get_unified_tags(posts_with_metadata):
    unique_tags = set()
    for post in posts_with_metadata:
        unique_tags.update(post['tags'])  # Collect all tags

    unique_tags_list = ','.join(unique_tags)

    template = '''I will give you a list of tags. You need to unify tags with the following requirements:
    1. Tags are unified and merged to create a shorter list.
       Example 1: "Jobseekers", "Job Hunting" → "Job Search".
       Example 2: "Motivation", "Inspiration", "Drive" → "Motivation".
       Example 3: "Personal Growth", "Self Improvement" → "Self Improvement".
       Example 4: "Scam Alert", "Job Scam" → "Scams".
    2. Each tag should follow title case convention. Example: "Motivation", "Job Search".
    3. Output should be a JSON object with mapping of original tag to the unified tag.
    
    Here is the list of tags: 
    {tags}
    '''
    pt = PromptTemplate.from_template(template)
    chain = pt | llm
    response = chain.invoke({"tags": unique_tags_list})

    try:
        json_parser = JsonOutputParser()
        res = json_parser.parse(response.content)
    except OutputParserException:
        raise OutputParserException("Context too big. Unable to parse tags.")
    return res


if __name__ == "__main__":
    process_posts("data/raw_posts.json", "data/processed_posts.json")
