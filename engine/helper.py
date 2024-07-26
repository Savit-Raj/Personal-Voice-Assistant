import re


def extract_yt_term(command):
    # To find song
    pattern = r'(?:play\s+)?(.*?)\s+on\s+youtube'
    match = re.search(pattern, command, re.IGNORECASE)
    return match.group(1) if match else None

def extract_g_term(command):
    # To search name
    pattern = r'(?:search\s+)?(.*?)\s+on\s+google'
    match = re.search(pattern, command, re.IGNORECASE)
    return match.group(1) if match else None