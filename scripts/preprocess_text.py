# This file needs to be run in the main folder
# %%
import text
from utils import read_lines_from_file
import os
from num2words import num2words


def check_file_extension(file_path, desired_extension):
    _, file_extension = os.path.splitext(file_path)
    if file_extension.lower() != desired_extension:
        raise ValueError(f'File does not end with {desired_extension}')


def process_text(bw_file_path , phonetics_file_path, splitter ):

    try:
        check_file_extension(bw_file_path, '.txt')
    except ValueError as e:
        print(e)

    try:
        check_file_extension(phonetics_file_path, '.txt')
    except ValueError as e:
        print(e)

    lines = read_lines_from_file(bw_file_path)
    new_lines_phonetic = []
    for line in lines:
        wav_name, utterance = line.split(splitter)
        wav_name, utterance = wav_name, utterance
        utterance = utterance.replace("a~", "~a") \
                            .replace("i~", "~i") \
                            .replace("u~", "~u") \
                            .replace(" - ", " ")

        utterance_arab = text.buckwalter_to_arabic(utterance)
        utterance_phon = text.buckwalter_to_phonemes(utterance)
        line_new_pho = f'"{wav_name}" "{utterance_phon}"'
        new_lines_phonetic.append(line_new_pho)

        with open(phonetics_file_path, mode='w', encoding='utf-8') as f:
            for i, line in enumerate(new_lines_phonetic):
                if i == len(lines)-1:
                    f.write(line)
                    break
                f.write(line + '\n')

    return "Phonetics file generated successfully "




def num_to_arabic_letters(text):
    text = text.split()
    sent = []
    for i in text:
        try:
            num = num2words(int(i), lang='ar')
            sent.append(num)
        except:
            sent.append(i)

    return ' '.join(sent) 



def infer_preprocess(input_text):
    modified_line = input_text.replace(',', '.')  # Remove commas from the line
    modified_line = modified_line.replace('،', '.')
    modified_line = modified_line.replace('-', ' ')
    modified_line = num_to_arabic_letters(modified_line)
    
    return modified_line


















