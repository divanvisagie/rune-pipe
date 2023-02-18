import logging
import os
import pandas as pd

logger = logging.getLogger(__name__)


def has_same_repeated_character(s):
    try:
        s = s.replace(' ', '')
        return s == s[0] * len(s)
    except Exception as e:
        logger.info("Error: %s" % e)
        return False


def get_list_of_signums(df: pd.DataFrame):
    try:
        # xls_file = pd.read_excel('data/rundata/RUNDATA.xls')
        # df = pd.DataFrame(xls_file)
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


if __name__ == '__main__':
    """ set logger formating"""
    root = 'data/processed'
    logging.basicConfig(
        format='%(asctime)s %(levelname)s %(message)s', level=logging.DEBUG)
    df_en = get_table_from_text('ENGLISH')
    create_folder_if_not_exists(root)
    df_en.to_csv(f'{root}/ENGLISH.csv', index=False)
