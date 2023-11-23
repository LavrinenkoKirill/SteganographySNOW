from lxml.builder import unicode
					  	 	 import snow
							  	 import re
					  	 	 import os


def utf8len(s):
    return len(s.encode('utf-8'))


def count_sentences(filename):
    txt = open(filename)
    data = txt.read()
    txt.close()
    count = 0
    for letter in data:
        if letter == '.' or letter == '!' or letter == '?':
            count += 1

    return count


def encode_bytes(source_filename, messages):
    if ".txt" in source_filename:
        txt = open(source_filename)
        data = txt.read()
        txt.close()
        lst = list(messages)
        length = len(lst)
        code_list = list()
        data_list = list()
        for letter in data:
            if letter == '.':
                index = data.find('.')
                data_list.append(data[:index + 1])
                data = data[index + 1:]
            elif letter == '!':
                index = data.find('!')
                data_list.append(data[:index + 1])
                data = data[index + 1:]
        for i in range(length):
            code_list.append(encode(data_list[i], lst[i]))
        f = open(source_filename, 'w')
        for i in range(len(code_list)):
            f.write(code_list[i])
        for i in range(len(data_list) - len(code_list)):
            f.write(data_list[len(code_list) + i])
        f.close()
    elif ".html" in source_filename:
        txt = open(source_filename)
        data = txt.read()
        txt.close()
        lst = list(messages)
        length = len(lst)
        code_list = list()
        data_list = list()
        for letter in data:
            if re.search('\n', data):
                sub = re.search('\n', data)
                index = sub.span()
                data_list.append(data[:index[0] + 1])
                data = data[index[0] + 1:]
        for i in range(length):
            code_list.append(encode(data_list[i], lst[i]))
        f = open(source_filename, 'w')
        for i in range(len(code_list)):
            f.write(code_list[i])
        for i in range(len(data_list) - len(code_list)):
            f.write(data_list[len(code_list) + i])
        f.close()
    else:
        txt = open(source_filename)
        data = txt.read()
        txt.close()
        lst = list(messages)
        length = len(lst)
        code_list = list()
        data_list = list()
        for letter in data:
            if re.search('\n', data):
                sub = re.search('\n', data)
                index = sub.span()
                data_list.append(data[:index[0] + 1])
                data = data[index[0] + 1:]
        for i in range(length):
            code_list.append(encode(data_list[i], lst[i]))
        f = open("encoded_main.py", 'w')
        for i in range(len(code_list)):
            f.write(code_list[i])
        for i in range(len(data_list) - len(code_list)):
            f.write(data_list[len(code_list) + i])
        f.close()


def decode_bytes(encoded_filename, result_filename):
    if ".txt" in encoded_filename:
        txt = open(encoded_filename)
        data = txt.read()
        txt.close()
        data_list = list()
        answer_list = list()
        for letter in data:
            if re.search('.' + '\t\t\t', data):
                sub = re.search('.' + '\t\t\t', data)
                index = sub.span()
                data_list.append(data[:index[0] + 13])
                data = data[index[0] + 13:]
            elif re.search('!' + '\t\t\t', data):
                sub = re.search('!' + '\t\t\t', data)
                index = sub.span()
                data_list.append(data[:index[0] + 13])
                data = data[index[0] + 13:]
        for i in range(len(data_list)):
            answer_list.append(decode(data_list[i]))
        f = open(result_filename, 'w')
        for i in range(len(answer_list)):
            f.write(answer_list[i])
        f.close()
    elif ".html" in encoded_filename:
        txt = open(encoded_filename)
        data = txt.read()
        txt.close()
        data_list = list()
        answer_list = list()
        for letter in data:
            if re.search('\n\t\t\t', data):
                sub = re.search('\n\t\t\t', data)
                index = sub.span()
                data_list.append(data[:index[0] + 13])
                data = data[index[0] + 13:]
        for i in range(len(data_list)):
            answer_list.append(decode(data_list[i]))
        f = open(result_filename, 'w')
        for i in range(len(answer_list)):
            f.write(answer_list[i])
        f.close()
    else:
        txt = open("encoded_main.py")
        data = txt.read()
        txt.close()
        data_list = list()
        answer_list = list()
        for letter in data:
            if re.search('\n\t\t\t', data):
                sub = re.search('\n\t\t\t', data)
                index = sub.span()
                data_list.append(data[:index[0] + 13])
                data = data[index[0] + 13:]
        for i in range(len(data_list)):
            answer_list.append(decode(data_list[i]))
        f = open(result_filename, 'w')
        for i in range(len(answer_list)):
            f.write(answer_list[i])
        f.close()


def encode(unencoded_string, msg, binary=False, replacements=None, delimiter=None):
    if not delimiter:
        delimiter = '\t\t\t'
    code = snow.encode(msg, character_set=replacements, binary=binary)
    return unencoded_string + delimiter + code


def decode(encoded_string, binary=False, replacements=None, delimiter=None):
    if not delimiter:
        delimiter = '\t\t\t'
    regex = "{}(.+)$".format(delimiter)
    m = re.search(regex, encoded_string)
    code = m.groups()[0]
    return snow.decode(code, character_set=replacements, binary=binary)


# message = "SOS"
# msg_size = utf8len(message)
#
# sentences = count_sentences('example.txt')
# empty_file_size = os.path.getsize('example.txt')
#
# file_encode('example.txt', message)
# file_size = os.path.getsize('example.txt')
#
# print('File size:', file_size, 'bytes')
#
# cs = (msg_size / file_size)
# ic = (sentences / file_size)
# ic_2 = (empty_file_size / file_size)
# print("Coefficient of hiding: " + str(cs))
# print("Informational capacity: " + str(ic))
# print("Informational capacity v2: " + str(ic_2))
# file_decode('example.txt', 'result.txt', a)


message = "SOS"
encode_bytes('main.py', message)
decode_bytes('main.py', 'result.txt')
