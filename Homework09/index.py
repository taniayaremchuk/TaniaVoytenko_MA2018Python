"""
Planner for Yahtzee
Simplifications:  only allow discard and roll, only score against upper level
"""
import random
import codeskulptor
codeskulptor.set_timeout(20)

def gen_all_sequences(outcomes, length):
    answer_set = set([()])
    for dummy_idx in range(length):
        temp_set = set()
        for partial_sequence in answer_set:
            for item in outcomes:
                new_sequence = list(partial_sequence)
                new_sequence.append(item)
                temp_set.add(tuple(new_sequence))
        answer_set = temp_set
    return answer_set

def gen_all_permutations(outcomes, length):      
    ans = set([()])
    for dummy_idx in range(length):
        temp = []
        for seq in ans:
            for item in outcomes:
                if item not in seq or seq.count(item) < outcomes.count(item):
                    new_seq = list(seq)
                    new_seq.append(item)
                    temp.append(tuple(new_seq))
        ans = temp
    return ans

def score(hand):
    possible_scores = [hand.count(value) * value for value in hand]
            
    
    return max(possible_scores)


def expected_value(held_dice, num_die_sides, num_free_dice):
    all_rolls = gen_all_sequences((range(1,(num_die_sides+1))),num_free_dice)
    all_possible_hands = [hand + held_dice for hand in all_rolls]
    
    number_of_outcomes = float(len(all_rolls))
    expected = 0
    
    for hand in all_possible_hands:
        expected += (1/number_of_outcomes)*score(hand)
    return expected


def gen_all_holds(hand):
    all_holds = set([()]) 
    for length in range(len(hand)+1):
        all_permutations = gen_all_permutations(hand, length)
        all_combinations = [tuple(sorted(sequence)) for sequence in all_permutations]
        all_holds.update(all_combinations)
    return all_holds



def strategy(hand, num_die_sides):
    temp_all_holds = gen_all_holds(hand)
    all_holds = list(temp_all_holds)
    largest_value = 0
    expected_value_list = []
    for hold in all_holds:
        expected_value_number = expected_value(hold,num_die_sides,len(hand)-len(hold))
        expected_value_list.append(expected_value_number)
        if expected_value_number > largest_value:
            largest_value = expected_value_number
    hold_choice = []  
    for value in range(len(expected_value_list)):
        if expected_value_list[value] == largest_value:
            hold_choice.append(all_holds[value])  
    return (largest_value, random.choice(hold_choice))


def run_example():
    num_die_sides = 6
    hand = (1, 1, 1, 5, 6)
    hand_score, hold = strategy(hand, num_die_sides)
    print "Best strategy for hand", hand, "is to hold", hold, "with expected score", hand_score

run_example()
    
#import poc_holds_testsuite
#poc_holds_testsuite.run_suite(gen_all_holds)
