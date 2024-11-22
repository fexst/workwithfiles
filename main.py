import os

def initial():
    path = os.getcwd()
    file_data_all = []
    for file in os.listdir(path):
        if file.endswith('.txt') and file[0].isdigit():
            with open(file, encoding='UTF-8') as f:
                data = f.readlines()
                count_lines = len(data)
                files_data = (f.name, count_lines, data)
                file_data_all.append(files_data)
    sorted_files = sorted(file_data_all, key=lambda x: x[1])
    with open('result.txt', 'w', encoding='utf-8') as result_file:
                for file_name, count_lines, all_text in sorted_files:
                    result_file.write(f'{file_name}\n')
                    result_file.write(f'{count_lines}\n')
                    for text in all_text:
                        if text != all_text[-1]:
                            result_file.write(text)
                        else:
                            result_file.write(f'{text}\n')


initial()