# zamienianie znakow w stringu


text = ' Artificial intelligence (AI), sometimes called machine intelligence, \
is intelligence demonstrated by machines, \
in contrast to the natural intelligence displayed by humans and other animals. \
In computer science AI research is defined as the study of "intelligent agents":\
 any device that perceives its environment and takes actions that maximize its chance of successfully achieving \
 its goals.[1] Colloquially, the term "artificial intelligence" \
 is applied when a machine mimics "cognitive" functions that \
 humans associate with other human minds, such as "learning" and "problem solving".'



new_text = text.replace("a","@").replace("i","&")

print(new_text)