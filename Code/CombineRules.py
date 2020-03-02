#!/usr/bin/env python3

'''
The purpose of this tool is to combine separate rules by merging their variables
Author: Lucas M. Tabajara
Email: lucasmt@rice.edu
Date: 6 February 2020
**Under Development**
'''

# Imports
import sys
import random
import re

# Get the usage string
def usage():
    usage = "----------------- Usage ----------------\n"
    usage += "./CombineRules.py <random seed> <number of rules> <number of variables> <output directory> *<rule files>"
    return usage

def generate_rule(rule_file, number_of_variables, output_file):
    with open(rule_file, 'r') as file:
        with open(output_file, 'w') as out:
            line = file.readline()

            while line and not line.startswith("DFA for formula with free variables:"):
                out.write(line)
                line = file.readline()

            old_vars = line.rstrip().split(": ")[1].split(" ")
            new_vars = ['I%d' % i for i in range(number_of_variables)]
            
            new_var_sample = random.sample(new_vars, len(old_vars))

            out.write("DFA for formula with free variables: " + " ".join(new_var_sample) + "\n")

            line = file.readline()
            
            while line:
                out.write(line)
                line = file.readline()

# Entry point
if __name__ == '__main__':

    # Check the correct number of command line arguments
    if len(sys.argv) < 5:
        print(usage())
        exit(-1)

    random_seed = int(sys.argv[1])
    number_of_rules = int(sys.argv[2])
    number_of_variables = int(sys.argv[3])
    output_directory = sys.argv[4]
    rule_files = sys.argv[5:]

    random.seed(random_seed)
    
    for i in range(number_of_rules):
        print("Rule %d" % i)
        rule_file = rule_files[random.randrange(len(rule_files))]
        generate_rule(rule_file, number_of_variables, output_directory + '/rule' + str(i) + '.out')
