# DiaBLa English-French dialogue corpus
(Dialogue BiLingue "Bilingual Dialogue")


## Use as a test set

The test set contains spontaneously produced dialogues by native speakers on a range of topics and can be used as a test set for evaluating machine translation (MT) outputs.

- The source files to be translated are `diabla.en2fr_orig` and `diabla.fr2en_orig`.
- The reference files are `diabla.en2fr_orig` and `diabla.fr2en_orig` respectively.
 
Each file contain both sides of each dialogue (i.e. all sentences). This is important for whole document translation, i.e. to have access to all context in the source language when translating. 

As such, each source file contains either original sentences (when the original language of the sentence corresponds to the source language) or a machine translation of the other language (when the original language of the sentence is the other language). When evaluating, you should only evaluate on those sentences that were originally in the source language. Once you have translated all source sentences, you can filter your translations using the following script:

`bash scripts/filter-sents-for-eval.sh <YOUR_TRANSLATION_FILE> diabla.{en2fr,fr2en}.eval-filter > OUT`





