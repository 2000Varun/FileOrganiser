import os
from pathlib import Path

driver_file = os.path.basename(__file__)

DIRECTORIES = {	"HTML FILES": [".html5", ".html", ".htm", ".xhtml"],
                "IMAGES": [".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg", "svg", ".heif", ".psd"],
                "VIDEOS": [".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob", ".mng",".qt", ".mpg", ".mpeg", ".3gp"],
                "DOCUMENTS": [".oxps", ".epub", ".pages", ".docx", ".doc", ".fdf", ".ods",".odt", ".pwi", ".xsn", ".xps", ".dotx", ".docm", ".dox",".rvg", ".rtf", ".rtfd", ".wpd", ".xls", ".xlsx", ".ppt",	"pptx"],
                              "ARCHIVES": [".a", ".ar", ".cpio", ".iso", ".tar", ".gz", ".rz", ".7z",
				".dmg", ".rar", ".xar", ".zip"],
                "AUDIO FILES": [".aac", ".aa", ".aac", ".dvf", ".m4a", ".m4b", ".m4p", ".mp3",".msv", "ogg", "oga", ".raw", ".vox", ".wav", ".wma"],
                "PLAINTEXT FILES": [".txt", ".in", ".out"],
                "PDF": [".pdf"],
                "PYTHON FILES": [".py"],
                "XML FILES": [".xml"],
                "EXE FILES": [".exe"],
                "SHELL FILES": [".sh"]
              }


FILE_FORMATS = {file_format: directory	for directory, file_formats in DIRECTORIES.items()  for file_format in file_formats}

def organize_junk():
    for entry in os.scandir():
        if entry.is_dir():
            continue
        file_path = Path(entry)
        if str(file_path)==driver_file:
            continue
        file_format = file_path.suffix.lower()
        if file_format in FILE_FORMATS:
            directory_path = Path(FILE_FORMATS[file_format])
            directory_path.mkdir(exist_ok=True)
            file_path.rename(directory_path.joinpath(file_path))
        for dir in os.scandir():
            try:
                os.rmdir(dir)
            except:
                pass
  
if __name__ == "__main__":
    organize_junk()
