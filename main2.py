import sys
import re
from pathlib import Path
import shutil

CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")

TRANS = {}
for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
    TRANS[ord(c)] = l
    TRANS[ord(c.upper())] = l.upper()


def normalize(name):
    name_file = re.sub('\.\w+', '', name)
    name_file = re.sub('\W', '_', name_file)
    name_file = name_file.translate(TRANS)
    return name_file


def sort_files_recursively(dir_path, folder_move):
    images_format = ['JPEG', 'PNG', 'JPG', 'SVG']
    video_format = ['AVI', 'MP4', 'MOV', 'MKV']
    documents_format = ['DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX']
    audio_format = ['MP3', 'OGG', 'WAV', 'AMR']
    archives_format = ['ZIP', 'GZ', 'TAR']
    others_format = []

    for folder in ['Images', 'Video', 'Documents', 'Audio', 'Archives', 'Others']:
        Path(folder_move, folder).mkdir(exist_ok=True)

    for file_path in dir_path.iterdir():
        if file_path.is_file():
            file_ext = file_path.suffix[1:].upper()
            if file_ext in images
                if file_ext in images_format:
                    shutil.move(file_path, Path(folder_move, 'Images', normalize(file_path.name)))
                elif file_ext in video_format:
                    shutil.move(file_path, Path(folder_move, 'Video', normalize(file_path.name)))
                elif file_ext in documents_format:
                    shutil.move(file_path, Path(folder_move, 'Documents', normalize(file_path.name)))
                elif file_ext in audio_format:
                    shutil.move(file_path, Path(folder_move, 'Audio', normalize(file_path.name)))
                elif file_ext in archives_format:
                    shutil.move(file_path, Path(folder_move, 'Archives', normalize(file_path.name)))
                else:
                    shutil.move(file_path, Path(folder_move, 'Others', normalize(file_path.name)))
            elif file_path.is_dir():
                sort_files_recursively(file_path, folder_move)
