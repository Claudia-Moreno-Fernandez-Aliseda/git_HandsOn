#!/usr/bin/env python

import sys, re
from argparse import ArgumentParser

parser = ArgumentParser(description = 'Classify a sequence as DNA or RNA')
parser.add_argument("-s", "--seq", type = str, required = True, help = "Input sequence")
parser.add_argument("-m", "--motif", type = str, required = False, help = "Motif")

if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)

args = parser.parse_args()
args.seq = args.seq.upper()

#if re.search('^[ACGTU]+$', args.seq): # This pattern allows both T and U in the same sequence, which is incorrect
 #   if re.search('T', args.seq):
 #       print ('The sequence is DNA') 
 #   elif re.search('U', args.seq):
 #       print ('The sequence is RNA')
 #   else:
 #       print ('The sequence can be DNA or RNA')
#else:
 #   print ('The sequence is not DNA nor RNA')
def search_DNA_RNA(seq):
	if 'T' and 'U' in seq:
		return "The sequence cannot contain both T and U"
	elif 'T' in seq:
		return "The sequence is DNA"
	elif 'U' in seq:
		return "The sequence is RNA"
	elif re.fullmatch(r'^[ACG]+$', seq): # This is ambigous because it does not contain either T or U
		return "I am not sure...The sequence can be either DNA or RNA"
	else: # If there are numbers... or other symbol
		return "The sequence is not DNA nor RNA"
print(search_DNA_RNA(args.seq))

if args.motif:
    args.motif = args.motif.upper()
    print(f'Motif search enabled: looking for motif "{args.motif}" in sequence "{args.seq}"... ', end = '')
    if re.search(args.motif, args.seq):
        print("FOUND! CONGRATS")
    else:
        print("NOT FOUND. SORRY")


