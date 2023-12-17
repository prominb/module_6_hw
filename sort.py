import sys
import scan
import normalize
from pathlib import Path


def handle_file(path, root_folder, destinations):
    target_folder = root_folder/destinations
    target_folder.mkdir(exist_ok=True)
    path.replace(target_folder/normalize.normalize(path.name))


def remove_empty_folders(path):
    for item in path.iterdir():
        if item.is_dir():
            remove_empty_folders(item)

            try:
                item.rmdir()
            except OSError:
                pass


def main(folder_path):
    print(folder_path)
    scan.scan(folder_path)

    for file in scan.jpeg_files:
        handle_file(file, folder_path, "Pictures")

    for file in scan.png_files:
        handle_file(file, folder_path, "Pictures")

    for file in scan.jpg_files:
        handle_file(file, folder_path, "Pictures")

    for file in scan.svg_files:
        handle_file(file, folder_path, "Pictures")

    for file in scan.avi_files:
        handle_file(file, folder_path, "Video")

    for file in scan.mp4_files:
        handle_file(file, folder_path, "Video")

    for file in scan.mov_files:
        handle_file(file, folder_path, "Video")
    
    for file in scan.mkv_files:
        handle_file(file, folder_path, "Video")

    for file in scan.doc_files:
        handle_file(file, folder_path, "Documents")

    for file in scan.docx_files:
        handle_file(file, folder_path, "Documents")

    for file in scan.txt_files:
        handle_file(file, folder_path, "Documents")

    for file in scan.pdf_files:
        handle_file(file, folder_path, "Documents")

    for file in scan.xlsx_files:
        handle_file(file, folder_path, "Documents")

    for file in scan.pptx_files:
        handle_file(file, folder_path, "Documents")

    for file in scan.mp3_files:
        handle_file(file, folder_path, "Music")

    for file in scan.ogg_files:
        handle_file(file, folder_path, "Music")

    for file in scan.wav_files:
        handle_file(file, folder_path, "Music")

    for file in scan.amr_files:
        handle_file(file, folder_path, "Music")

    for file in scan.zip_files:
        handle_file(file, folder_path, "Archives")

    for file in scan.gz_files:
        handle_file(file, folder_path, "Archives")

    for file in scan.tar_files:
        handle_file(file, folder_path, "Archives")

    for file in scan.unknown_files:
        handle_file(file, folder_path, "Unknown")

    remove_empty_folders(folder_path)

if __name__ == '__main__':
    path = sys.argv[1]
    print(f'Start in {path}')

    folder = Path(path)
    main(folder.resolve())
