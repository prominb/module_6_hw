import sys
from pathlib import Path


dir_names = ('Archives', 'Video', 'Audio', 'Documents', 'Images', 'Others')
jpeg_files = list()
png_files = list()
jpg_files = list()
svg_files = list()

avi_files = list()
mp4_files = list()
mov_files = list()
mkv_files = list()

doc_files = list()
docx_files = list()
txt_files = list()
pdf_files = list()
xlsx_files = list()
pptx_files = list()

mp3_files = list()
ogg_files = list()
wav_files = list()
amr_files = list()

zip_files = list()
gz_files = list()
tar_files = list()

unknown = set()
unknown_files = list()

extensions = set()
folders = list()

registered_extensions = {
    'JPEG': jpeg_files, 'PNG': png_files, 'JPG': jpg_files, 'SVG': svg_files,
    'AVI': avi_files, 'MP4': mp4_files, 'MOV': mov_files, 'MKV': mkv_files,
    'DOC': doc_files, 'DOCX': docx_files, 'TXT': txt_files, 'PDF': pdf_files, 'XLSX': xlsx_files, 'PPTX': pptx_files,
    'MP3': mp3_files, 'OGG': ogg_files, 'WAV': wav_files, 'AMR': amr_files,
    'ZIP': zip_files, 'GZ': gz_files, 'TAR': tar_files
}


def get_extensions(file_name):
    return Path(file_name).suffix[1:].upper()


def scan(folder):
    for item in folder.iterdir():
        if item.is_dir():
            if item.name not in dir_names:
                folders.append(item)
                scan(item)
            continue

        extension = get_extensions(file_name=item.name)
        new_file_name = folder/item.name

        if not extension:
            unknown_files.append(new_file_name)
        else:
            try:
                container = registered_extensions[extension]
                extensions.add(extension)
                container.append(new_file_name)
            except KeyError:
                unknown.add(extension)
                unknown_files.append(new_file_name)


if __name__ == '__main__':
    path = sys.argv[1]
    print(f"Start in folder name: {path}")
    folder = Path(path)
    scan(folder)
    # print(scan(folder))

    # print("*"*15)
    # print(f"jpeg: {jpeg_files}")
    # print(f"png: {png_files}")
    # print(f"jpg: {jpg_files}")
    # print(f"svg: {svg_files}")
    # print("*"*15)
    # print(f"avi: {avi_files}")
    # print(f"mp4: {mp4_files}")
    # print(f"mov: {mov_files}")
    # print(f"mkv: {mkv_files}")
    # print("*"*15)
    # print(f"doc: {doc_files}")
    # print(f"docx: {docx_files}")
    # print(f"txt: {txt_files}")
    # print(f"pdf: {pdf_files}")
    # print(f"xlsx: {xlsx_files}")
    # print(f"pptx: {pptx_files}")
    # print("*"*15)
    # print(f"zip archive: {zip_files}")
    # print(f"gz archive: {gz_files}")
    # print(f"tar archive: {tar_files}")
    # print("*"*15)
    # print(f"unkown files: {unknown_files}")
    # print("*"*15)
    # print(f"All extensions: {extensions}")
    # print(f"Unknown extensions: {unknown}")
    # print("*"*15)
    # print(f"Folder: {folders}")
