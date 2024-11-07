import os
import subprocess

def extract_pak(pak_file_path):
    pak_dir = os.path.dirname(pak_file_path)
    # 假设gust_pak在系统环境变量中的路径是正确的，或者指定了完整的路径
    command = f"gust_pak {os.path.basename(pak_file_path)}"
    subprocess.run(command, cwd=pak_dir, check=True)
    extracted_dir = os.path.join(pak_dir, os.path.splitext(os.path.basename(pak_file_path))[0])
    return extracted_dir

def convert_files_in_directory(directory_path):
    if not os.path.isdir(directory_path):
        print("请输入一个有效的路径。输入的路径不是一个有效的目录。")
        return

    pak_files = []
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            # 将文件扩展名转换为小写后检查是否为'.pak'
            if os.path.splitext(file.lower())[1] == '.pak':
                pak_files.append(os.path.join(root, file))

    total_pak_files = len(pak_files)
    print(f"找到 {total_pak_files} 个 .pak 文件。")

    for index, pak_file in enumerate(pak_files, start=1):
        print(f"正在解包 ({index}/{total_pak_files}): {pak_file}")
        extracted_dir = extract_pak(pak_file)
        print(f"已解包到: {extracted_dir}")
        progress_percentage = (index / total_pak_files) * 100
        print(f"解包进度: {progress_percentage:.2f}%")

if __name__ == "__main__":
    directory_path = input("请输入目录路径: ")
    convert_files_in_directory(directory_path)