# DiaBLa English-French dialogue corpus
(Dialogue BiLingue "Bilingual Dialogue")


## Use as a test set

- Source files: `diabla.en2fr_orig` and `diabla.fr2en_orig`.
- Reference files: `diabla.en2fr_ref` and `diabla.fr2en_ref`.
 
Each source file contains the entire dialogue, from the point of view of the speaker of the source language (containing their own original sentences and the machine translated versions of the other speaker's utterances). This is important for contextual translation - to have access to all context present when the source utterances were produced. 

The reference files contain only those sentences that should be evaluated (i.e. the sentences that were originally in the source language). Once you have translated the entire source file, filter your translations as follows:

`bash scripts/filter-sents-for-eval.sh <YOUR_TRANSLATION_FILE> diabla.{en2fr,fr2en}.eval-filter > OUT`

Then evaluate the filtered sentences against the reference translations using your favourite metric.


## .json formatted corpus (containing all annotations)

The corpus also exists in `.json` format, with extra annotations for each dialogue and each utterance.

Each dialogue file has the following dialogue-level information:
 
 ```
  "start_time": <DATETIME>,
  "end_time": <ENDTIME>,
  "scenario": [
             [SCENARIO DESCRIPTION (IN ENGLISH), SCENARIO DESCRIPTION (IN FRENCH)],
             [ROLE 1 (IN ENGLISH), ROLE 2 (IN FRENCH)],
             [ROLE 2 (IN ENGLISH), ROLE 2 (IN FRENCH)]
            ],
  "user1": {
     "turn_number": 1 OR 2,
     "role": [TEXT DESCRIPTION OF ROLE (IN ENGLISH), TEXT DESCRIPTION OF ROLE (IN FRENCH)],
     "lang": "french or "english"
     }
   "user2": {
     "turn_number": 1 OR 2,
     "role": [TEXT DESCRIPTION OF ROLE (IN ENGLISH), TEXT DESCRIPTION OF ROLE (IN FRENCH)],
     "lang": "french or "english"
     }
  "translation_model": "baseline" or "contextual",
  "utterances": {
     "0": {...},
     "1": {...},
      ...
     }
 ```

Each utterance (ids start at 0) is structured as followed:

```
id : {
  "language": "english/french",
  "original_text": <ORIGINAL TEXT>,
  "normalised_version": <NORMALISED TEXT (IF NECESSARY)>,
  "preprocessed_text": <PREPROCESSED TEXT>,
  "translated_text": <TRANSLATED TEXT>,
  "postprocessed_text": <TRANSLATED, PREPROCESSED TEXT>,
  "reference_translation": <HUMAN TRANSLATION>,
  "composition_time": <DATETIME>, # message is entered
  "preprocessing_begin": <DATETIME>,
  "preprocessing_end": <DATETIME>,
  "translation_begin": <DATETIME>,
  "translation_end": <DATETIME>,
  "postprocessing_begin": <DATETIME>,
  "postprocessing_end": <DATETIME>,
  "sent_time": TRANSLATION SENT,
  "eval": {
     "judgment": "poor/medium/perfect",
     "judgment history": [
       ["poor/medium/perfect", <DATETIME>], [...]
     ]
     "verbatim": <FREE EVALUATION COMMENT>,
     "verbatim_history": [
       [<VERBATIM>, <DATETIME>], [...]
     ], 
     "problems": ["word choice", "grammaticality", "coherence", "style"], # list of problems present (if any)
     "problem_history": [
         [<PROBLEM>, <DATETIME>, true/false], [...]
      ]
     
   }
```
















