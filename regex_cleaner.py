import re

with open('./NYTOccupy13-14.TXT','r') as input:
    text = input.read()

news_pieces = re.sub(pattern=r'[0-9]+ of [0-9]+ DOCUMENTS.*?HEADLINE:(.*?)BODY:(.*?)(?:\n{3}|\Z)',
                     repl=r'\n\1 \2\n\n\n\n', string=text, flags=re.DOTALL)

with open('./output.txt', 'w') as output:
    output.write(news_pieces)