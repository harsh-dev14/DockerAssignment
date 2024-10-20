# scripts/scripts.py

import os
import re
from collections import Counter
import socket

def read_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        return file.read()

def count_words(text):
    words = re.findall(r'\b\w+\b', text.lower())
    return len(words), words

def top_n_words(words, n=3):
    counter = Counter(words)
    return counter.most_common(n)

def handle_contractions(text):
    text = re.sub(r"(\w+)\'(\w+)", r"\1 \2", text)
    return text

def get_ip_address():
    hostname = socket.gethostname()
    try:
        ip_address = socket.gethostbyname(hostname)
    except:
        ip_address = 'Unable to determine IP'
    return ip_address

def main():
    # Use the DATA_DIR environment variable
    data_dir = os.getenv('DATA_DIR', '/home/data')
    output_dir = os.path.join(data_dir, 'output')
    os.makedirs(output_dir, exist_ok=True)
    result_file = os.path.join(output_dir, 'result.txt')

    # Process IF.txt
    if_text = read_file(os.path.join(data_dir, 'IF.txt'))
    if_word_count, if_words = count_words(if_text)
    if_top3 = top_n_words(if_words)

    # Process AlwaysRememberUsThisWay.txt
    aru_text = read_file(os.path.join(data_dir, 'AlwaysRememberUsThisWay.txt'))
    aru_text = handle_contractions(aru_text)
    aru_word_count, aru_words = count_words(aru_text)
    aru_top3 = top_n_words(aru_words)

    # Grand total
    grand_total = if_word_count + aru_word_count

    # IP Address
    ip_address = get_ip_address()

    # Prepare result
    result = f"""
Word Count in IF.txt: {if_word_count}
Word Count in AlwaysRememberUsThisWay.txt: {aru_word_count}
Grand Total Word Count: {grand_total}

Top 3 Words in IF.txt:
"""
    for word, count in if_top3:
        result += f"{word}: {count}\n"

    result += "\nTop 3 Words in AlwaysRememberUsThisWay.txt (after handling contractions):\n"
    for word, count in aru_top3:
        result += f"{word}: {count}\n"

    result += f"\nIP Address of the Container: {ip_address}\n"

    # Write to result.txt
    with open(result_file, 'w', encoding='utf-8') as file:
        file.write(result.strip())

    # Print to console
    print(result.strip())

if __name__ == "__main__":
    main()
