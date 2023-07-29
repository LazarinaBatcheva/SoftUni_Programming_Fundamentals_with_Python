import re

word = input()
text = input()
pattern = r"\b[^.!?]* " + re.escape(word) + r" [^.!?]*\b"
sentences = re.findall(pattern, text)
if sentences:
    print("\n".join(sentences))