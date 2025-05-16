import pandas as pd
import os
from math import ceil

def split_excel_file(file_path, chunk_size=10):
    """
    最终修正版Excel切割函数
    :param file_path: 原文件路径
    :param chunk_size: 每个子文件的数据行数（不含表头）
    """
    try:
        # 读取文件，明确首行为表头
        df = pd.read_excel(file_path, header=0)

        # 数据部分（排除表头）
        data = df.iloc[1:]  # ✅ 关键修正点：从第二行开始

        # 计算切割数量
        total_rows = len(data)
        num_chunks = ceil(total_rows / chunk_size)

        # 输出目录处理
        base_name = os.path.splitext(os.path.basename(file_path))[0]
        output_dir = os.path.dirname(file_path)

        for i in range(num_chunks):
            start = i * chunk_size
            end = min((i + 1) * chunk_size, total_rows)

            # 构建子DataFrame（自动继承表头）
            chunk_df = pd.concat(
                [df.head(0), data.iloc[start:end]],  # ✅ 正确引用表头
                ignore_index=True
            )

            # 写入文件
            output_path = os.path.join(
                output_dir,
                f"{base_name}_part{i + 1}.xlsx"
            )
            chunk_df.to_excel(
                output_path,
                index=False,
                engine='openpyxl'
            )

        print(f"切割完成，生成 {num_chunks} 个文件")

    except Exception as e:
        print(f"错误: {str(e)}")


if __name__ == "__main__":
    split_excel_file("D:/Git_project/bytenew_api_autotest/data/lg_bm_list_cases.xlsx", chunk_size=2)