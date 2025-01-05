import os

def get_project_root(marker_file='requirements.txt', max_depth=10):
    """
    获取项目的根目录
    :param marker_file: 标志文件，用于判断根目录
    :param max_depth: 最大向上查找的层数
    :return: 根目录路径
    """
    if not isinstance(marker_file, str):
        raise ValueError("标志文件名称必须是字符串")
    if not isinstance(max_depth, int) or max_depth <= 0:
        raise ValueError("最大查找深度必须是正整数")

    current_path = os.path.dirname(os.path.abspath(__file__))
    depth = 0

    while not os.path.exists(os.path.join(current_path, marker_file)):
        parent_path = os.path.abspath(os.path.join(current_path, os.pardir))
        if parent_path == current_path or depth >= max_depth:
            raise FileNotFoundError(f"找不到标志文件 '{marker_file}'，已达到最大查找深度 {max_depth}")
        current_path = parent_path
        depth += 1

    return current_path

def find_file(file_name, file_path=''):
    root_path = get_project_root()
    target_path = os.path.join(root_path, file_path, file_name)

    if not os.path.exists(target_path):
        raise FileNotFoundError(f"文件 '{file_name}' 不存在于路径 '{target_path}'")
    return target_path

# 示例调用
a = find_file("test1.py", r"Template\aaa\aa")
print(a)
