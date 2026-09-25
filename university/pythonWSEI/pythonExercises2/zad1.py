import os
import shutil

def create_copy_folder(base_dir):
    copy_dir = os.path.join(base_dir, 'kopie')
    if not os.path.exists(copy_dir):
        os.makedirs(copy_dir)
    return copy_dir

def copy_and_rename_files(src_dir, dest_dir):
    files = [f for f in os.listdir(src_dir) if f.lower().endswith(('.jpg', '.png'))]
    print(f"\n{os.path.basename(src_dir)}: ")

    for i, file in enumerate(files):
        print(file)
        src_path = os.path.join(src_dir, file)
        dest_name = f"{os.path.basename(src_dir)}_{i}" + os.path.splitext(file)[1].lower()
        dest_path = os.path.join(dest_dir, dest_name)
        shutil.copy2(src_path, dest_path)

def generate_report(base_dir):
    report_file = os.path.join(base_dir, 'raport.txt')

    with open(report_file, 'w') as report:
        for folder in os.listdir(base_dir):
            if(folder != 'kopie'):
                folder_path = os.path.join(base_dir, folder)

                if os.path.isdir(folder_path):
                    report.write(f"\n{folder_path}\n")

                    files = [f for f in os.listdir(folder_path) if f.lower().endswith(('.jpg', '.png'))]
                    for file in files:
                        report.write(f"{file}\n")

def main():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    base_dir = os.path.abspath(os.path.join(current_dir, '..', 'katalogBazowy'))
    copy_dir = create_copy_folder(base_dir)
    dirs_to_copy = ['wakacje', 'zima', 'wyjazd']

    for folder in os.listdir(base_dir):
        if folder in dirs_to_copy:
            folder_path = os.path.join(base_dir, folder)

            if os.path.isdir(folder_path):
                copy_and_rename_files(folder_path, copy_dir)

    generate_report(base_dir)

if __name__ == "__main__":
    main()