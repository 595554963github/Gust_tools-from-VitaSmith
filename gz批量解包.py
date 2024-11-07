import os
import subprocess

def extract_gz(gz_file_path):
    # 构建解压命令，假设gust_elixir在系统环境变量中的路径是正确的
    command = f"gust_elixir {os.path.basename(gz_file_path)}"
    # 执行解压命令
    subprocess.run(command, cwd=os.path.dirname(gz_file_path), check=True)

def convert_files_in_directory(directory_path):
    if not os.path.isdir(directory_path):
        print("输入的路径不是一个有效的目录。")
        return

    gz_files = []
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if file.lower().endswith('.gz'):
                gz_files.append(os.path.join(root, file))

    total_gz_files = len(gz_files)
    print(f"找到 {total_gz_files} 个 .gz 文件。")

    for index, gz_file in enumerate(gz_files, start=1):
        print(f"正在解压 ({index}/{total_gz_files}): {gz_file}")
        extract_gz(gz_file)
        progress_percentage = (index / total_gz_files) * 100
        print(f"解压进度: {progress_percentage:.2f}%")

if __name__ == "__main__":
    directory_path = input("请输入一个有效的路径: ")
    convert_files_in_directory(directory_path)