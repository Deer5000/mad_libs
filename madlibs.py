#import shuffle
word_list = list()

def madlibs():
    adjective = input('Enter an adjective: ')#============
    word_list.append(adjective)
    adjective_1 = input('Enter an adjective: ')#============
    word_list.append(adjective_1)
    noun_0 = input('Enter an noun: ')#============
    word_list.append(noun_0)
    adjective_2 = input('Enter an adjective: ')#============
    word_list.append(adjective_2)
    adjective_3 = input('Enter an adjective: ')#============
    word_list.append(adjective_3)
    adjective_4 = input('Enter an adjective: ')#============
    word_list.append(adjective_4)
    noun_1 = input('Enter a noun: ')
    word_list.append(noun_1)
    verb = input('Enter a verb: ')
    word_list.append(verb)
    verb_1 = input('Enter a verb: ')
    word_list.append(verb_1)
    adjective_5 = input('Enter an adjective: ')
    word_list.append(adjective_5)
    noun_2 = input('Enter a noun: ')
    word_list.append(noun_2)
    adverb = input('Enter a adverb: ')
    word_list.append(verb_2)
    noun_3 = input('Enter a noun: ')
    word_list.append(noun_3)
    verb_3 = input('Enter a verb: ')
    word_list.append(verb_3)
    adjective_6 = input('Enter an adjective: ')
    word_list.append(adjective_6)

    print(" I walk through the tropical rainforest. I take out my \033[1;32m {} \033[0m flask. There's a \033[1;32m {} \033[0m Tiger with a {} in his mouth directly in front of me in the \033[1;32m {} \033[0m trees! I gaze at his \033[1;32m {} \033[0m {}. A sudden roar awakes me from my daydream! A panther {}'s in front of my face! I {} his {} breath. I remember I have a pocket full of {}'s that puts it to sleep! I {} it away from me in front of the {}. Yes he's ingesting it! I meet my brothers at the resort. Sheesh! Its been a thrilling day in the rainforest   ".format(adjective, adjective_1, noun_0, adjective_3, adjective_4, noun_1, verb, verb_1, adjective_5, noun_2, adverb, noun_3, verb_3, adjective_6))
#random.shuffle(adjective_1,adjective_3,adjective_5)
madlibs()
