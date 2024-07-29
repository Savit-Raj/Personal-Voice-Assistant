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

def removeWords(input_string, words_to_remove):
    words = input_string.split()
    filtered_words = [word for word in words if word.lower() not in words_to_remove]
    result_string = ' '.join(filtered_words)
    return result_string

# imput_string = 'make a phone call to papa'
# words_to_remove = ['make','a','to','phone','call','send','message','whatsapp','']
# result = removeWords(imput_string, words_to_remove)
# print(result)