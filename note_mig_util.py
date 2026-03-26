# -*- coding: utf-8 -*-
import os
import re

def rename_items_with_uuid_suffix(root_dir):
    """
    遍历指定目录（包括子目录），重命名符合特定模式的 Markdown 文件。
    重命名规则：移除名称末尾的 '+UUID' 部分。
    例如：'笔记+123e4567-e89b-12d3-a456-426614174000.md' -> '笔记.md'

    :param root_dir: 要处理的根目录路径。
    """
    # 定义 UUID 的正则表达式模式，包括前面的 '+' 号
    # UUID 格式: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx (8-4-4-4-12)
    uuid_pattern_str = r'\+[0-9a-fA-F]{8}-(?:[0-9a-fA-F]{4}-){3}[0-9a-fA-F]{12}'

    # 使用 os.walk 遍历目录树
    for dirpath, dirnames, filenames in os.walk(root_dir):
        # 处理文件 (仅限 Markdown 文件)
        for filename in filenames:
            name_part, ext_part = os.path.splitext(filename)
            
            # 检查是否为 Markdown 文件
            if ext_part.lower() == '.md':
                # 检查文件名（不含扩展名）的末尾是否匹配 '+UUID' 模式
                match = re.search(uuid_pattern_str + r'$', name_part)
                if match:
                    # 构建新的文件名（移除 '+UUID' 部分）
                    new_name_part = name_part[:match.start()]
                    # 替换文件名中英文之间的 '+' 为空格
                    # 使用正则表达式确保只替换英文单词之间的 '+'
                    new_name_part_cleaned = re.sub(r'([a-zA-Z])\+([a-zA-Z])', r'\1 \2', new_name_part)
                    new_filename = new_name_part_cleaned + ext_part
                    
                    old_filepath = os.path.join(dirpath, filename)
                    new_filepath = os.path.join(dirpath, new_filename)
                    
                    try:
                        # 执行重命名
                        os.rename(old_filepath, new_filepath)
                        print(f"重命名 Markdown 文件: '{old_filepath}' 为 '{new_filepath}'")
                    except OSError as e:
                        print(f"重命名 Markdown 文件 '{old_filepath}' 失败: {e}")

if __name__ == "__main__":
    # 获取用户输入的目标目录
    target_directory = r'D:\Downloads\15.心理学'
    
    # 校验路径是否为有效目录
    if os.path.isdir(target_directory):
        print(f"开始处理目录: {target_directory}\n")
        rename_items_with_uuid_suffix(target_directory)
        print("\n处理完成。")
    else:
        print(f"错误: '{target_directory}' 不是一个有效的目录路径。")