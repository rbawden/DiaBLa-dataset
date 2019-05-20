# DiaBLa English-French MT dialogue test set
(Dialogue BiLingue "Bilingual Dialogue")

English-French test set for the evaluation of Machine Translation (MT) for informal, written bilingual dialogue. 

The test set contains 5,700+ sentences from 144 spontaneous, written dialogues between English and French speakers. The dialogues are mediated by one of two neural MT systems (a baseline RNN and a lightly contextual RNN model that uses the previous sentence). Each dialogue is associated with one of twelve varied scenarios, which are listed [here](#scenarios).

Dialogue annotations:
 * fine-grained sentence-level judgments of MT quality, produced by the dialogue participants themselves
 * manually produced reference translations
 * manually normalised versions of source sentences


## Use as a test set

- Source files: `DiaBLa-corpus/diabla.en2fr_orig` and `DiaBLa-corpus/diabla.fr2en_orig`.
- Reference files: `DiaBLa-corpus/diabla.en2fr_ref` and `DiaBLa-corpus/diabla.fr2en_ref`.
- Info file: `DiaBLa-corpus/diabla.info`
 
Each source file contains the entire dialogue, from the point of view of the speaker of the source language (containing their own original sentences and the machine translated versions of the other speaker's utterances). This is important for contextual translation - to have access to all context present when the source utterances were produced. 

The reference files contain only those sentences that should be evaluated (i.e. the sentences that were originally in the source language). Once you have translated the entire source file, filter your translations as follows:

`bash scripts/filter-sents-for-eval.sh <YOUR_TRANSLATION_FILE> diabla.{en2fr,fr2en}.eval-filter > OUT`

Then evaluate the filtered sentences against the reference translations using your favourite metric.


## Citation

If you use this corpus, please cite:

```
@article{bawden_diabla2019,
    author = {Rachel Bawden and Sophie Rosset and Thomas Lavergne and Eric Bilinski},
    title = {DiaBLa: A Corpus of Bilingual Spontaneous Written Dialogues for Machine Translation},
    year = {2019},
    url = {http://arxiv.org/abs/...},
}
```


## Structure and content

### .json formatted corpus (containing all annotations)

The corpus also exists in `.json` format, containing all annotations and information. All dialogue files are found `dialogues/` and information for each user is found in `users/`.

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

Each utterance in the dialogue (ids start at 0) is structured as followed:

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

User files are structured as follows:

```
{
   "idnum": 1,
   "age": "35-44",
   "gender": "male",
   "english_ability": "poor|medium|good|near-native|native",
   "french_ability": "poor|medium|good|near-native|native",
   "otherlangs": <LIST OF OTHER LANGUAGES SPOKEN>,
   "worked_in_research": true|false,
   "worked_in_NLP": true|false,
   "agreed_to_terms_and_conditions": true
   "creation_date": <DATETIME>,
}
```

N.B. Historic changes concerning the evaluation of the machine translated sentences are logged (when sentences are evaluated and whether the pairticpants change their mind).




### Scenarios

There are 12 different scenarios (and 12 dialogues associated with each one, 6 for each translation model):

1. __You are both lost in a forest.__
  - Roles: N/A

2. __You are chefs preparing a meal.__
  - Role 1: You are the head chef and you are talking to your subordinate.
  - Role 2: You are the subordinate chef and you are talking to the head chef.


3. __You are in a classroom.__
  - Role 1: You are the teacher and you are talking to a student.
  - Role 2: You are the student and you are talking to your teacher.

4. __You are feeding the ducks by the pond.__
  - Roles: N/A

5. __You are both organising a party.__
  - Role 1: It's your party.
  - Role 2: It's their party.

6. __You are both stuck in a lift at work.__
  - Role 1: You are an employee and you are with your boss.
  - Role 2: You are the boss and are with an employee.

7. __You are in a retirement home.__
  - Role 1: You are visiting and talking to an old friend.
  - Role 2: You are a resident and you are talking with an old friend who is visiting you.

8. __You are in a bar.__
  - Role 1: You are the bartender and talking to a customer.
  - Role 2: You are a customer and are talking to the bartender.

9. __You are in an aeroplane.__
  - Role 1: You are scared and are speaking to the person sitting next to you.
  - Role 2: You are speaking to the person next to you, who is scared.

10. __You are at home in the evening.__
  - Role 1: You are telling your spouse about the awful day you had.
  - Role 2: You are listening to your spouse telling you about the awful day they had.

11. __You are in a psychiatrist's consulting room.__
  - Role 1: You are the psychiatrist and are with your patient.
  - Role 2: You are a patient and you are talking to your psychiatrist.

12. __You are on holiday by the pool.__
  - Role 1: You are trying to relax and the other person wants to do something else.
  - Role 2: You want to do something else and the other person is trying to relax.









