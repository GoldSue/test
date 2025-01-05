import os

def get_project_root():
    """
    获取项目的根目录
    :param marker_file: 标志文件，用于判断根目录
    :return: 根目录路径
    """
    current_path = os.path.dirname(os.path.abspath(__file__))
    while True:
        parent_path = os.path.abspath(os.path.join(current_path, os.pardir))
        if parent_path == current_path:
            return current_path
        current_path = parent_path

def create_file_in_root(filename, relative_path=''):
    """
    在项目根目录或指定相对路径下创建文件
    :param filename: 文件名
    :param relative_path: 相对路径
    """
    root_directory = get_project_root()
    file_path = os.path.join(root_directory, relative_path, filename)
    with open(file_path, 'w') as file:
        file.write("Hello, world!")

# 示例用法
if __name__ == "__main__":
    root_directory = get_project_root()
    print(f"项目根目录为：{root_directory}")

    # create_file_in_root("example.txt", "Template")
    # print("文件已创建：example.txt 在子文件夹 subfolder 中")
