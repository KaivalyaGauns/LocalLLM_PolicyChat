import re
def add_space(text):
    # Add space between number and digit
    text = re.sub(r'\n', ' ', text)
    text = re.sub(r'([a-zA-Z])(\d)', r'\1 \2', text)
    text = re.sub(r'(\d)([a-zA-Z])', r'\1 \2', text)
    text = re.sub(r'([^\d.,/ ])(?=\d)', r'\1 ', text)
    text = re.sub(r'(?<![0-9/])([^\d., ])(?=\d)(?!/)', r'\1 ', text)
    return text