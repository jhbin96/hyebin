def decorator(func):
    def decorated(input_text):
        print('함수 시작!')
        func(input_text)
        print('함수 끝!')
    return decorated


@decorator
def hello_world(input_text):
    print(input_text)


hello_world('Hello World!')

def check_integer(func):
    def decorated(width, height):
        if width >= 0 and height >= 0:
            return func(width, height)
        else:
            raise ValueError('Input must be positive value')
        return decorated
