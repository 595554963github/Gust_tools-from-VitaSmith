import os
import subprocess

def export_g1t_files(directory):
    # 获取所有.g1t文件的路径
    g1t_files = [os.path.join(root, file)
                  for root, dirs, files in os.walk(directory)
                  for file in files if file.endswith('.g1t')]

    total_files = len(g1t_files)
    print(f"总共找到 {total_files} 个 .g1t 文件。")

    # 遍历.g1t文件并执行导出操作
    for index, g1t_file in enumerate(g1t_files, start=1):
        print(f"正在导出文件：{g1t_file}")
        subprocess.run(['gust_g1t.exe',  g1t_file])
        print(f"已完成 {index}/{total_files} ({(index / total_files) * 100:.2f}%)")

if __name__ == "__main__":
    directory_path = input("请输入一个有效的路径: ")
    if os.path.isdir(directory_path):
        export_g1t_files(directory_path)
    else:
        print("输入的不是一个有效的路径。")
