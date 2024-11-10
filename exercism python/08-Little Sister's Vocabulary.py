"""Functions for creating, transforming, and adding prefixes to strings."""


def add_prefix_un(word):
    return "un" + word


def make_word_groups(vocab_words):
    prefix = vocab_words[0]
    return f"{prefix} :: " + " :: ".join([prefix + word for word in vocab_words[1:]])


def remove_suffix_ness(word):
    root = word[:-4]
    if root[-1] == 'i':
        return root[:-1] + 'y'
    else:
        return root

    
def adjective_to_verb(sentence, index):
    words = sentence.split()
    adjective = words[index].rstrip(".!?")
    verb = adjective + "en"
    return verb