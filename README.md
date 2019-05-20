# DiaBLa English-French dialogue corpus
(Dialogue BiLingue "Bilingual Dialogue")


## Use as a test set

- Source files: `diabla.en2fr_orig` and `diabla.fr2en_orig`.
- Reference files: `diabla.en2fr_ref` and `diabla.fr2en_ref`.
 
Each source file contains the entire dialogue, from the point of view of the speaker of the source language, i.e. containing their own original sentences but also the machine translated versions of the other speaker's utterances. This is important for  contextual translation, i.e. to have access to all context present when the source utterances were produced. 

The reference files contain only those sentences that should be evaluated (i.e. the sentences that were originally in the source language). Once you have translated the entire source file, filter your translations as follows:

`bash scripts/filter-sents-for-eval.sh <YOUR_TRANSLATION_FILE> diabla.{en2fr,fr2en}.eval-filter > OUT`






