import re
from collections import Counter

def remove_whitespace(text):
    """
    移除字符串中的所有空格、制表符和换行符
    """
    return ''.join(text.split())

def capitalize_words(text):
    """
    将字符串中每个单词的首字母大写
    """
    return ' '.join(word.capitalize() for word in text.split())

def replace_substring(text, old, new):
    """
    替换字符串中的指定子字符串
    """
    return text.replace(old, new)

def reverse_string(text):
    """
    反转字符串
    """
    return text[::-1]

def is_numeric(text):
    """
    检查字符串是否只包含数字
    """
    return text.isdigit()

def is_palindrome(text):
    """
    检查字符串是否是回文（忽略大小写和空格）
    """
    cleaned_text = ''.join(text.lower().split())
    return cleaned_text == cleaned_text[::-1]

def extract_numbers(text):
    """
    提取字符串中的所有数字
    """
    return re.findall(r'\d+', text)

def to_snake_case(text):
    """
    将字符串转换为蛇形命名法（snake_case）
    """
    text = re.sub(r'(?<!^)(?=[A-Z])', '_', text).lower()
    return text.replace(" ", "_")

def word_count(text):
    """
    统计字符串中每个单词的出现次数
    """
    words = text.lower().split()
    return Counter(words)

# 测试所有封装方法
if __name__ == "__main__":
    sample_text = "Hello world! Python is great. Hello Python!"
    print("原始文本:", sample_text)

    # 1. 移除空格
    print("移除空格:", remove_whitespace(sample_text))

    # 2. 首字母大写
    print("首字母大写:", capitalize_words(sample_text))

    # 3. 替换子字符串
    print("替换 'Python' 为 'Programming':", replace_substring(sample_text, "Python", "Programming"))

    # 4. 反转字符串
    print("反转字符串:", reverse_string(sample_text))

    # 5. 检查是否为数字
    print("字符串是否为数字 ('12345'):", is_numeric("12345"))
    print("字符串是否为数字 ('123a45'):", is_numeric("123a45"))

    # 6. 检查是否为回文
    print("是否为回文 ('A man a plan a canal Panama'):", is_palindrome("A man a plan a canal Panama"))
    print("是否为回文 ('hello'):", is_palindrome("hello"))

    # 7. 提取数字
    print("提取数字 ('Order 123 costs $45 and arrives in 2 days'):", extract_numbers("Order 123 costs $45 and arrives in 2 days"))

    # 8. 转换为蛇形命名法
    print("转换为蛇形命名法 ('HelloWorld Example'):", to_snake_case("HelloWorld Example"))

    # 9. 统计单词出现次数
    print("统计单词出现次数:", word_count(sample_text))
