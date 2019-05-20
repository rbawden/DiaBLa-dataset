#!/usr/bin/python
import os, json, re

def get_users_from_filename(filename):
    usermatch = re.match('.*?_([^_]+)_([^_]+)_(\d+)_(\d+).json', filename)
    lang1 = usermatch.group(1)
    lang2 = usermatch.group(2)
    user1 = usermatch.group(3)
    user2 = usermatch.group(4)
    return lang1, lang2, user1, user2


def extract_file(dialogue_file, user_folder, 
                 en2fr_orig, en2fr_ref, en2fr_filter,
                 fr2en_orig, fr2en_ref, fr2en_filter, info):

    dialogue = json.load(open(dialogue_file))
    lang1, lang2, user1, user2 = get_users_from_filename(dialogue_file)

    fr_user = user1 if lang1 =='french' else user2
    en_user = user2 if lang1 =='french' else user1


    for utt_num in dialogue['utterances']:
        utt = dialogue['utterances'][utt_num]

        lang = utt['language']
        text = utt['original_text']
        mt = utt['postprocessed_text']
        ref = utt['reference_translation']
        norm = utt['normalised_version']
        user = fr_user if lang == 'french' else en_user

        write_time = utt['composition_time']
        preproc_begin = utt['preprocessing_begin']
        preproc_end = utt['preprocessing_end']
        translation_begin = utt['translation_begin']
        translation_end = utt['translation_end']
        sent_time = utt['sent_time']

        #print(utt)
        #input()
        # write text to files.
        # _orig files contain all sentences as seen by the speaker 
        # of the source langauge
        # _ref files contain all reference translations. If the source 
        # is a machine translation, then ref line prefixed by 'IGNORE' 
        # for evaluation purposes
        info_text = '\t'.join([lang, user, norm if norm != '' else 'None', 
                               write_time, sent_time, 
                               dialogue_file.split('/')[-1]]) + '\n'
        info.write(info_text)
        
        if lang == 'english':
            en2fr_orig.write(text + '\n')
            en2fr_ref.write(ref + '\n')
            fr2en_orig.write(mt + '\n')
            fr2en_filter.write('_IGNORE_FOR_EVAL_\n')

        elif lang == 'french':
            fr2en_orig.write(text + '\n')
            fr2en_ref.write(ref + '\n')
            en2fr_orig.write(mt + '\n')
            en2fr_filter.write('_IGNORE_FOR_EVAL_\n')

        else:
            print('There has been an error. ' + lang + ' is not a recognised language.')
            exit()


def extract_all(dialogue_folder, user_folder, output_folder):

    # open outputs files
    en2fr_orig = open(output_folder + '/diabla.en2fr.orig', 'w')
    en2fr_ref = open(output_folder + '/diabla.en2fr.ref', 'w')
    en2fr_filter = open(output_folder + '/diabla.en2fr.eval-filter', 'w')
    fr2en_orig = open(output_folder + '/diabla.fr2en.orig', 'w')
    fr2en_ref = open(output_folder + '/diabla.fr2en.ref', 'w')
    fr2en_filter = open(output_folder + '/diabla.fr2en.eval-filter', 'w')
    info = open(output_folder + '/diabla.info', 'w')

    # for each dialogue file, extract text and write to files
    for dialogue_file in os.listdir(dialogue_folder):
        if '.json' not in dialogue_file:
            continue
        extract_file(dialogue_folder + '/' + dialogue_file, user_folder,
                     en2fr_orig, en2fr_ref, en2fr_filter,
                     fr2en_orig, fr2en_ref, fr2en_filter, info)

    # close all files
    en2fr_orig.close(), en2fr_ref.close(), en2fr_filter.close()
    fr2en_orig.close(), fr2en_ref.close(), fr2en_filter.close(), info.close()


if __name__ == '__main__':

    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('dialogue_folder')
    parser.add_argument('user_folder')
    parser.add_argument('output_folder')
    args = parser.parse_args()
    
    extract_all(args.dialogue_folder, args.user_folder, args.output_folder)
