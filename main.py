with open('1.txt', encoding='UTF-8') as f1:
    data1 = f1.readlines()
    count_lines1 = len(data1)
    files_data1 = (f1.name, count_lines1, data1)
    with open('2.txt', encoding='UTF-8') as f2:
        data2 = f2.readlines()
        count_lines2 = len(data2)
        files_data2 = (f2.name, count_lines2, data2)
        with open('3.txt', encoding='UTF-8') as f3:
            data3 = f3.readlines()
            count_lines3 = len(data3)
            files_data3 = (f3.name, count_lines3, data3)
            file_data_all = [files_data1, files_data2, files_data3]
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



                

