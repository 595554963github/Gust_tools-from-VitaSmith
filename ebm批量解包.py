import os
import subprocess

def extract_ebm(ebm_file_path):
    json_file_path = ebm_file_path.replace('.ebm', '.json')
    ebm_dir = os.path.dirname(ebm_file_path)
    # 构建解压命令，假设gust_ebm在系统环境变量中的路径是正确的
    command = f"gust_ebm {os.path.basename(ebm_file_path)}"
    # 执行解压命令
    subprocess.run(command, cwd=ebm_dir, check=True)
    return json_file_path

def convert_files_in_directory(directory_path):
    if not os.path.isdir(directory_path):
        print("输入的路径不是一个有效的目录。")
        return

    ebm_files = []
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if file.endswith('.ebm'):
                ebm_files.append(os.path.join(root, file))

    total_ebm_files = len(ebm_files)
    print(f"找到 {total_ebm_files} 个 .ebm 文件。")

    for index, ebm_file in enumerate(ebm_files, start=1):
        print(f"正在解压 ({index}/{total_ebm_files}): {ebm_file}")
        json_file = extract_ebm(ebm_file)
        print(f"已解压到: {json_file}")
        progress_percentage = (index / total_ebm_files) * 100
        print(f"解压进度: {progress_percentage:.2f}%")

if __name__ == "__main__":
    directory_path = input("请输入一个有效的路径: ")
    convert_files_in_directory(directory_path)