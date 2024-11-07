import os
import subprocess
import time

def unpack_gmpk_files(directory, tool_path):
    # 获取所有.gmpk文件的路径
    gmpk_files = [os.path.join(root, file)
                  for root, dirs, files in os.walk(directory)
                  for file in files if file.endswith('.gmpk')]

    total_files = len(gmpk_files)
    print(f"总共找到 {total_files} 个 .gmpk 文件。")

    # 遍历.gmpk文件并执行解包操作
    for index, gmpk_file in enumerate(gmpk_files, start=1):
        print(f"正在解包文件：{gmpk_file}")
        subprocess.run([tool_path, gmpk_file])
        print(f"已完成 {index}/{total_files} ({(index / total_files) * 100:.2f}%)")
        time.sleep(0.1)  # 稍作延迟，以便于观察进度

if __name__ == "__main__":
    directory_path = input("请输入一个有效的路径: ")
    tool_path = 'gust_gmpk.exe'  # 假设gmpk.exe在当前脚本执行的目录

    # 不再验证gust_gmpk.exe是否存在

    if os.path.isdir(directory_path):
        unpack_gmpk_files(directory_path, tool_path)
    else:
        print("输入的不是一个有效的路径。")