"""
Student code for Word Wrangler game
"""

import urllib2
import codeskulptor
import poc_wrangler_provided as provided

WORDFILE = "assets_scrabble_words3.txt"

# Functions to manipulate ordered word lists

def remove_duplicates(list1):
    
    new_list = []
    if len(list1) > 0:
        new_list.append(list1[0])
        for idx in range(len(list1) - 1):
            if list1[idx] != list1[idx + 1]:
                new_list.append(list1[idx + 1])
    return new_list

def intersect(list1, list2):
    
    intersect_list = []
    if len(list1) <= len(list2):
        shorter_list = list1
        other_list = list2
    else:
        shorter_list = list2
        other_list = list1
    for idx in range(len(shorter_list)):
        if shorter_list[idx] in other_list:
            intersect_list.append(shorter_list[idx])
    return intersect_list

# Functions to perform merge sort

def merge(list1, list2):
    
    merged_list = []
    list_one = list(list1)
    list_two = list(list2)
    
    if len(list_one) == 0 or len(list_two) == 0:
        merged_list.extend(list_one)
        merged_list.extend(list_two)
    else:    
        while len(list_one) > 0 and len(list_two) > 0:
            if list_one[0] <= list_two[0]:
                merged_list.append(list_one.pop(0))
            else:
                merged_list.append(list_two.pop(0))
        merged_list.extend(list_one)
        merged_list.extend(list_two)
    
    return merged_list
                
def merge_sort(list1):
    
    if len(list1) < 2:
        return list1
    else:
        mid = len(list1) / 2
        sublist_one = list1[:mid]
        sublist_two = list1[mid:]
        return merge(merge_sort(sublist_one), merge_sort(sublist_two))

# Function to generate all strings for the word wrangler game

def gen_all_strings(word):
    
    if len(word) == 0:
        return []
    elif len(word) == 1:
        start_list = []
        start_list.append(word)
        return start_list
    
    first = word[0]
    rest = word[1:]
    
    list_of_strings = []
    rest_strings = gen_all_strings(rest)
    list_of_strings.extend(rest_strings)
    
    for string in rest_strings:
        collect = []
        for idx in range(len(string) + 1):
            temp = list(string)
            temp.insert(idx, first)
            string_temp = ''.join(temp)
            collect.append(string_temp)
        list_of_strings.extend(collect)
    
    return list_of_strings

# Function to load words from a file

def load_words(filename):
    
    url = codeskulptor.file2url(filename)
    netfile = urllib2.urlopen(url)
    words_file = netfile.readlines()
    
    words = [word[:-2] for word in words_file]
    
    return words

def run():
    """
    Run game.
    """
    words = load_words(WORDFILE)
    wrangler = provided.WordWrangler(words, remove_duplicates, 
                                     intersect, merge_sort, 
                                     gen_all_strings)
    provided.run_game(wrangler)

# Uncomment when you are ready to try the game
run()

