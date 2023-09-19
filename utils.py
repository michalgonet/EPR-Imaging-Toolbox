import os
import zipfile

import constants


def create_zip_of_sample_data():
    folder_to_zip = 'Example_data'
    zip_filename = constants.PATH_TO_SAMPLE_DATA
    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for folder_name, sub_folders, filenames in os.walk(folder_to_zip):
            for filename in filenames:
                file_path = os.path.join(folder_name, filename)
                arch_name = os.path.relpath(file_path, folder_to_zip)
                zipf.write(file_path, arcname=arch_name)
