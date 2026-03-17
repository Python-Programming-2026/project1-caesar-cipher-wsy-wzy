def caesar_cipher(text, shift, mode='encrypt'):
    """
    凯撒密码实现
    :param text: 要处理的文本
    :param shift: 移位数量
    :param mode: 'encrypt' 加密 或 'decrypt' 解密
    :return: 处理后的文本
    """
    result = ""
    
    # 解密模式则移位取反
    if mode == 'decrypt':
        shift = -shift
    
    for char in text:
        if char.isupper():  # 大写字母
            result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        elif char.islower():  # 小写字母
            result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:  # 非字母字符
            result += char
    
    return result

def read_file(file_path):
    """读取文件内容"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"文件不存在：{file_path}")
        return None
    except Exception as e:
        print(f"读取文件失败：{e}")
        return None

def append_to_file(file_path, content):
    """追加内容到文件末尾"""
    try:
        with open(file_path, 'a', encoding='utf-8') as f:
            f.write('\n' + content)
        print(f"已追加到文件末尾：{file_path}")
        return True
    except Exception as e:
        print(f"追加文件失败：{e}")
        return False

def get_input_text():
    """
    获取输入文本（支持直接输入或读取文件）
    返回: 文d本内容, 是否来自文件, 文件路径
    """
    while True:
        print("\n请选择输入方式：")
        print("1. 直接输入文本")
        print("2. 从TXT文件读取")
        
        choice = input("请输入(1-2): ").strip()
        
        if choice == '1':
            text = input("请输入文本: ").strip()
            if text:
                return text, False, None
            else:
                print("文本不能为空！")
        
        elif choice == '2':
            path = input("请输入文件路径: ").strip()
            text = read_file(path)
            if text is not None:
                print(f"成功读取 {len(text)} 个字符")
                return text, True, path
        
        else:
            print("输入错误，请重新选择！")

def main():
    """主程序"""
    print("凯撒密码加密/解密工具")
    
    while True:
        print("\n请选择操作：")
        print("1. 加密")
        print("2. 解密")
        print("3. 退出")
        
        choice = input("请输入(1-3): ").strip()
        
        if choice == '3':
            print("感谢使用，再见！")
            break
            
        if choice not in ['1', '2']:
            print("输入错误！")
            continue
        
        # 获取输入文本
        text, is_from_file, file_path = get_input_text()
        if not text:
            continue
        
        # 获取移位值
        try:
            shift = int(input("请输入移位值: "))
            shift = shift % 26
        except ValueError:
            print("请输入有效数字！")
            continue
        
        # 执行加密/解密
        mode = 'encrypt' if choice == '1' else 'decrypt'
        result = caesar_cipher(text, shift, mode)
        
        print(f"\n结果：{result}")
        
        # 只有从文件读取时才询问是否保存
        if is_from_file:
            save = input("\n是否将结果追加到原文件？(y/n): ").lower()
            if save in ['y', 'yes']:
                append_to_file(file_path, result)

if __name__ == "__main__":
    main()