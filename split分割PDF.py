import os
from pypdf import PdfReader, PdfWriter
import argparse # 新增导入

def split_pdf(input_pdf_path, num_parts):
    """
    将指定的 PDF 文件平均分割成 N 份。

    :param input_pdf_path: 输入 PDF 文件的路径。
    :param num_parts: 要分割的份数。
    """
    try:
        # 文件存在性检查移至主程序块，因为 argparse 会处理文件路径参数
        # num_parts > 0 的检查也移至主程序块

        reader = PdfReader(input_pdf_path)
        total_pages = len(reader.pages)

        if total_pages == 0:
            print("错误：PDF 文件中没有页面。")
            return
        
        if num_parts > total_pages:
            print(f"警告：分割的份数 ({num_parts}) 大于总页数 ({total_pages})。将为每一页创建一个文件。")
            num_parts = total_pages

        pages_per_part = total_pages // num_parts
        remaining_pages = total_pages % num_parts

        output_dir = "output_parts"
        # 获取输入 PDF 的文件名（不带扩展名），用于构造输出文件名
        base_name = os.path.splitext(os.path.basename(input_pdf_path))[0]
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
            print(f"创建输出目录: {output_dir}")

        current_page = 0
        for i in range(num_parts):
            writer = PdfWriter()
            
            pages_in_this_part = pages_per_part + (1 if i < remaining_pages else 0)
            
            if pages_in_this_part == 0:
                continue

            start_page_index = current_page
            end_page_index = current_page + pages_in_this_part
            
            for page_num in range(start_page_index, end_page_index):
                if page_num < total_pages:
                    writer.add_page(reader.pages[page_num])
            
            if len(writer.pages) > 0:
                # 构造输出文件路径：原文件名p{序号}.pdf
                output_filename = os.path.join(output_dir, f"{base_name}-p{i + 1}.pdf")
                with open(output_filename, "wb") as output_pdf:
                    writer.write(output_pdf)
                print(f"已创建: {output_filename} (包含 {len(writer.pages)} 页)")
            
            current_page = end_page_index
        
        print(f"\nPDF 文件已成功分割成 {num_parts} 份，保存在 '{output_dir}' 目录下。")

    except Exception as e:
        print(f"处理 PDF 时发生错误: {e}")

if __name__ == "__main__":
    # --- 使用 argparse 处理命令行参数 ---
    parser = argparse.ArgumentParser(description="将 PDF 文件平均分割成 N 份。")
    parser.add_argument("input_pdf_file", type=str, help="要分割的输入 PDF 文件的路径。")
    parser.add_argument("number_of_parts", type=int, help="要分割的份数 (必须是正整数)。")

    args = parser.parse_args()
    # --- 参数处理结束 ---

    # 检查输入文件是否存在和份数是否有效
    if not os.path.isfile(args.input_pdf_file):
        print(f"错误：找不到输入 PDF 文件 '{args.input_pdf_file}'。请确保文件路径正确。")
    elif args.number_of_parts <= 0:
        print("错误：分割的份数 'number_of_parts' 必须大于 0。")
    else:
        split_pdf(args.input_pdf_file, args.number_of_parts)