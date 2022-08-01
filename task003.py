# 3. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

def encode_rle():
    with open('RLE_decoded.txt', 'r', encoding='utf-8') as data:
        text = data.read()
    print(f'Исходный текст:\n{text}')
    str_code = ''
    prev_char = ''
    count = 1
    for char in text:
        if char != prev_char:
            if prev_char:
                str_code += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    str_code += str(count) + prev_char
    with open('RLE_encoded.txt', 'w', encoding='utf-8') as data:
        data.write(str_code)
    return str_code

def decoding_rle():
    with open('RLE_encoded.txt', encoding='utf-8') as data:
        my_text = data.read()
    count = ''
    str_decode = ''
    for char in my_text:
        if char.isdigit():
            count += char
        else:
            str_decode += char * int(count)
            count = ''
    return str_decode


str_code = encode_rle()
print(f'\nСжатая версия текста: \n{str_code}')
str_decode = decoding_rle()
print(f'\nВосстановленная версия текста: \n{str_decode}')

