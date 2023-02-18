from functools import partial
import spacy
import logging
import os
import pandas as pd

logger = logging.getLogger(__name__)
# Load the English language model in spaCy
nlp = spacy.load('en_core_web_sm')


def has_same_repeated_character(s):
    try:
        s = s.replace(' ', '')
        return s == s[0] * len(s)
    except Exception as e:
        logger.info("Error: %s" % e)
        return False


def get_list_of_signums(df: pd.DataFrame):
    try:
        filtered_df = df[df['Plats'].notnull()]
        sigs = filtered_df['Signum'].values
        return sigs
    except Exception as e:
        logger.error("Error: %s" % e)


def get_dataframe_from_excel():
    xls_file = pd.read_excel('data/rundata/RUNDATA.xls')
    df = pd.DataFrame(xls_file)
    return df


def get_table_from_text(file_name):
    df_ex = get_dataframe_from_excel()
    sigs = get_list_of_signums(df_ex)
    try:
        with open("data/rundata/{}".format(file_name), "r", encoding='utf-8') as f:
            lines = f.readlines()

        df = pd.DataFrame(columns=['Signum', 'Text'])

        for line in lines:
            for signum in sigs:
                if line.find(signum) != -1:
                    parts = line.split(signum)
                    text = parts[1].strip()
                    # logger.info("line: %s" % line)
                    # logger.info("parts: %s" % parts)
                    if text.isspace() or has_same_repeated_character(text):
                        continue
                    new_df = pd.DataFrame(
                        {'Signum': signum, 'Text': text},
                        index=[0]
                    )
                    df = pd.concat([df, new_df], ignore_index=True)

        return df
    except Exception as e:
        logger.error("Error: %s" % e)


def create_folder_if_not_exists(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)


def extract_token_instances_from_text(search_token: str, text: str) -> list[str]:
    """Extracts all instances of a token from a text."""
    if type(text) != str:
        return []
    try:
        doc = nlp(text)
        return [token.text for token in doc if token.text.lower() == search_token.lower()]
    except Exception as e:
        logger.error("Error: %s" % e)
        return []


def text_contains(search_token: str, text: str) -> bool:
    if type(text) != str:
        return False
    """Checks entire string for ocurrence of substring."""
    return text.find(search_token) != -1


if __name__ == '__main__':
    """ set logger formating"""
    root = 'data/processed'
    logging.basicConfig(
        format='%(asctime)s %(levelname)s %(message)s', level=logging.DEBUG)
    extract_token_instances_from_text("test", "test test test")
