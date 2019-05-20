#!/bin/sh

[ "$#" -ne 2 ] && echo "USAGE: $0 <CANDIDATE_FILE> <FILTER_FILE>" && exit

candidate=$1 # candidate translation file
filter=$2 # diabla.en2fr.eval-filter or diabla.fr2en.eval-filter

# filter out these lines containing _IGNORE_FOR_EVAL_
paste $filter $candidate | grep -v '_IGNORE_FOR_EVAL_' | perl -pe 's/^\t//g'
