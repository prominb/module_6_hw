import sys
import scan
import shutil
import normalize
from pathlib import Path


dir_for_sorted = {
    'Archives': [],
    'Video': [],
    'Audio': [],
    'Documents': [],
    'Images': [],
    'Others': [],
}


def handle_file(path, root_folder, destinations):
    target_folder = root_folder/destinations
    target_folder.mkdir(exist_ok=True)
    target_item = path.replace(target_folder/normalize.normalize(path.name))
    if destinations == 'Archives':
        dir_for_sorted.get('Archives').append(target_item.name)
    elif destinations == 'Video':
        dir_for_sorted.get('Video').append(target_item.name)
    elif destinations == 'Audio':
        dir_for_sorted.get('Audio').append(target_item.name)
    elif destinations == 'Documents':
        dir_for_sorted.get('Documents').append(target_item.name)
    elif destinations == 'Images':
        dir_for_sorted.get('Images').append(target_item.name)
    elif destinations == 'Others':
        dir_for_sorted.get('Others').append(target_item.name)


def handle_archive(path, root_folder, destinations):
    target_folder = root_folder/destinations
    target_folder.mkdir(exist_ok=True)

    new_name = normalize.normalize(path.stem)
    archive_folder = target_folder/new_name
    archive_folder.mkdir(exist_ok=True)

    try:
        shutil.unpack_archive(str(path.resolve()), str(archive_folder.resolve()))
    except shutil.ReadError:
        archive_folder.rmdir()
        return
    except FileNotFoundError:
        archive_folder.rmdir()
        return
    
    path.unlink()


def remove_empty_folders(path):
    for item in path.iterdir():
        if item.is_dir():
            remove_empty_folders(item)

            try:
                item.rmdir()
            except OSError:
                # print("Not Empty")
                pass


def write_to_file(folder_path):
    with open(str(folder_path)+'/log_file', 'w') as fh:
        for key, value in dir_for_sorted.items():
            fh.write(f"{key}: {value}\n")


def main(folder_path):
    scan.scan(folder_path)

    # for file in scan.zip_files:
        # handle_file(file, folder_path, "Archives")
    for file in scan.zip_files:
        handle_archive(file, folder_path, "Archives")

    # for file in scan.gz_files:
        # handle_file(file, folder_path, "Archives")
    for file in scan.gz_files:
        handle_archive(file, folder_path, "Archives")

    # for file in scan.tar_files:
        # handle_file(file, folder_path, "Archives")
    for file in scan.tar_files:
        handle_archive(file, folder_path, "Archives")

    for file in scan.jpeg_files:
        handle_file(file, folder_path, "Images")

    for file in scan.png_files:
        handle_file(file, folder_path, "Images")

    for file in scan.jpg_files:
        handle_file(file, folder_path, "Images")

    for file in scan.svg_files:
        handle_file(file, folder_path, "Images")

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
        handle_file(file, folder_path, "Audio")

    for file in scan.ogg_files:
        handle_file(file, folder_path, "Audio")

    for file in scan.wav_files:
        handle_file(file, folder_path, "Audio")

    for file in scan.amr_files:
        handle_file(file, folder_path, "Audio")

    for file in scan.unknown_files:
        handle_file(file, folder_path, "Others")

    remove_empty_folders(folder_path)

    write_to_file(folder_path)

if __name__ == '__main__':
    path = sys.argv[1]
    print(f'Start in folder name: {path}')

    folder = Path(path)
    main(folder.resolve())
