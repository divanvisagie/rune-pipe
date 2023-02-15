import logging
import os
import urllib.request
import zipfile

origin_file_url = 'http://www.runforum.nordiska.uu.se/filer/srd2014.zip'
target_file = 'data/srd2014.zip'
logger = logging.getLogger(__name__)


def download_origin_file(url):
    if not os.path.exists(target_file):
        try:
            print("Downloading the origin file...")
            urllib.request.urlretrieve(url, target_file)
            print("Download complete!")
        except Exception as e:
            logger.error("Download failed: %s" % e)
    else:
        print("The origin file already exists!")


def unzip_origin_file(zip_file_path):
    output_folder_path = "data/rundata"

    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(output_folder_path)


if __name__ == '__main__':
    """ set logger formating"""
    logging.basicConfig(
        format='%(asctime)s %(levelname)s %(message)s', level=logging.DEBUG)

    download_origin_file(origin_file_url)
    unzip_origin_file(target_file)
