source_word="silent"
target_word="listen"

sort_sourcew=sorted(source_word)
sort_targetw=sorted(target_word)

print("anagram" if sort_sourcew==sort_targetw else "not anagram")