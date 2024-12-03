main_word = ['the house that Jack built.', 'the malt', 'the rat', 'the cat', 'the dog', 'the cow with the crumpled horn', 'the maiden all forlorn', 'the man all tattered and torn', 'the priest all shaven and shorn', 'the rooster that crowed in the morn', 'the farmer sowing his corn', 'the horse and the hound and the horn']

added_word = ['that lay in', 'that ate', 'that killed', 'that worried', 'that tossed', 'that milked', 'that kissed', 'that married', 'that woke', 'that kept', 'that belonged to']

def recite(start_verse, end_verse):
    result = []
    for verse in range(start_verse - 1, end_verse):
        sentence = "This is " + main_word[verse]
        for i in range(verse - 1, -1, -1):
            sentence += " " + added_word[i] + " " + main_word[i]
        result.append(sentence)
    return result
