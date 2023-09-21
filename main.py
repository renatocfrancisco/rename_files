import os
import shutil
import time


def create_new_folder():
    try:
        if os.path.exists("./new"):
            shutil.rmtree("./new")
        os.mkdir("./new")
    except Exception as e:
        print(e.args)
        raise Exception("Error deleting or creating new folder")


def copy_paste_folder(old_folder_path):
    old_folder = os.listdir(old_folder_path)

    for file in old_folder:
        shutil.copy(f"{old_folder_path}/{file}", "./new")


def rename_files(text):
    new_folder = os.listdir("./new")
    for file in new_folder:
        file_extension = file.split(".")[1]
        date = os.path.getmtime(f"./old/{file}")
        date = time.gmtime(date)

        day = "{:02d}".format(date.tm_mday)
        month = "{:02d}".format(date.tm_mon)
        year = str(date.tm_year)

        renamed = False
        d = 1
        while not renamed:
            try:
                if d == 1:
                    os.rename(
                        f"./new/{file}",
                        f"./new/{text}{year}{month}{day}.{file_extension}",
                    )
                else:
                    os.rename(
                        f"./new/{file}",
                        f"./new/{text}{year}{month}{day}({d}).{file_extension}",
                    )
                renamed = True
                d = 1
            except Exception as e:
                d += 1


create_new_folder()
placeholder_name = input("Enter placeholder name: ")
copy_paste_folder("./old")
rename_files(placeholder_name)
