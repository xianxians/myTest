class ShortInputError(Exception):
    def __init__(self, length, min_len):
        self.length = length
        self.min_len = min_len

    def __str__(self):
        return f'长度{self.length},密码{self.min_len}'

def main():
    try:
        password = input('请输入密码:')
        if len(password) < 3:
            raise ShortInputError(len(password), 3)
    except Exception as result:
        print(result)
    else:
        print('正常')

main()