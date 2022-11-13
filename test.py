import re

route = '/about/[id]/[pid]'
url = '/about/69/walrus/people/01'

opening_braces = '\\(\\['
closing_braces = '\\)\\]'
non_greedy_wildcard = '.*?'

params = re.findall(f'[{opening_braces}]{non_greedy_wildcard}[{closing_braces}]', , route)
print(tuple([match.replace("[", "").replace("]", "") for match in params]))

#print(re.findall(matcher, url))