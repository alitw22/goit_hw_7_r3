# main.py
from pathlib import Path
import shutil
import sys
import clean_folder.file_parser as parser
from clean_folder.normalize import normalize


def handle_media(filename: Path, target_folder: Path):
    target_folder.mkdir(exist_ok=True, parents=True)
    filename.replace(target_folder / normalize(filename.name))


def handle_other(filename: Path, target_folder: Path):
    target_folder.mkdir(exist_ok=True, parents=True)
    filename.replace(target_folder / normalize(filename.name))


def handle_archive(filename: Path, target_folder: Path):
    # Make archive folder
    target_folder.mkdir(exist_ok=True, parents=True)
    # Make archive unpacking folder
    # File name remove suffix
    folder_for_file = target_folder / normalize(filename.name.replace(filename.suffix, ''))

    # Make folder for the archive with folder name == file name
    folder_for_file.mkdir(exist_ok=True, parents=True)
    try:
        shutil.unpack_archive(str(filename.resolve()),
                              str(folder_for_file.resolve()))
    except shutil.ReadError:
        print(f'Це не архів {filename}!')
        folder_for_file.rmdir()
        return None
    filename.unlink()


def handle_folder(folder: Path):
    try:
        folder.rmdir()
    except OSError:
        print(f'Помилка видалення папки {folder}')


def main(folder: Path):
    parser.scan(folder)
    for file in parser.JPEG_IMAGES:
        # pathjoin(str(folder), 'images', 'JPEG')
        handle_media(file, folder / 'images' / 'JPEG')
    for file in parser.JPG_IMAGES:
        handle_media(file, folder / 'images' / 'JPG')
    for file in parser.PNG_IMAGES:
        handle_media(file, folder / 'images' / 'PNG')
    for file in parser.SVG_IMAGES:
        handle_media(file, folder / 'images' / 'SVG')
    for file in parser.MP3_AUDIO:
        handle_media(file, folder / 'audio' / 'MP3')

    for file in parser.MY_OTHER:
        handle_other(file, folder / 'MY_OTHER')  # Щоб не було помилки
    for file in parser.ARCHIVES:
        handle_archive(file, folder / 'archives')

    # Make list revers to remove empty folders
    for folder in parser.FOLDERS[::-1]:
        handle_folder(folder)


def start():

    if len(sys.argv) != 2:       
        sys.exit(0)
    else:          
        folder_for_scan = Path(sys.argv[1])
        # print(f'Starting in folder {folder_for_scan.resolve()}')
        main(folder_for_scan.resolve())

        
if __name__ == '__main__':

    if len(sys.argv) != 2:
        print("Сommand prompt should be: <clean_folder garbage>")
        sys.exit(0)
    else:
        start()

