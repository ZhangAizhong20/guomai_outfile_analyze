import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
import pandas as pd
import os

# 自定义的下载函数
OUTFILE_FLODER = 'E:\项目\GUOMAI_OUTFILE'
def download_file(file_link,file_name):
    try:
        # 发送请求
        response = requests.get(file_link)
        response.raise_for_status()  # 检查请求是否成功
        # 保存文件
        file_store_path = os.path.join(OUTFILE_FLODER,file_name)
        with open(file_store_path, 'wb') as file:
            file.write(response.content)

        print(f"下载成功: {file_name}")

    except Exception as e:
        print(f"下载失败: {file_link}，错误信息: {e}")

# 需要下载的文件列表，包含URL和文件名
target_df = pd.read_excel('download_name.xlsx')

# 定义多线程下载的函数
def download_files_concurrently(target_df):
    with ThreadPoolExecutor(max_workers=10) as executor:  # 设置最大线程数
        futures = []
        for index,row in target_df.iterrows():
            file_url = row["fileurl"]
            file_name = row["filename"]
            # 提交下载任务到线程池
            futures.append(executor.submit(download_file, file_url, file_name))

        # 等待任务完成
        for future in as_completed(futures):
            future.result()  # 如果需要捕捉错误，可以处理异常

# 调用多线程下载函数
if __name__ == "__main__":
    download_files_concurrently(target_df)
    