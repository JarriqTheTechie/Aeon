import re

route = '/'
url = '/about/69/walrus/people/01'

opening_braces = '\\(\\['
closing_braces = '\\)\\]'
non_greedy_wildcard = '.*?'

matcher = str(re.sub(f'[{opening_braces}]{non_greedy_wildcard}[{closing_braces}]', '.*', route))

#print(url)
print(matcher)
#x = re.compile(matcher)
#print(x)
#print(re.findall(matcher, url))