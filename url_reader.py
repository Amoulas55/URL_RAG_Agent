# url_reader.py

import trafilatura

def extract_article_text(url: str) -> str:
    """
    Downloads and extracts the main content from a web article using trafilatura.
    Returns cleaned text or empty string if extraction fails.
    """
    downloaded = trafilatura.fetch_url(url)
    if downloaded:
        article_text = trafilatura.extract(downloaded, include_comments=False, include_tables=False)
        return article_text.strip() if article_text else ""
    else:
        return ""
