import json


def report_file():
    try:
        with open('input.txt') as fh_i:
            data = list(fh_i)
            data1 = len(data)
            # print('Number of lines:', data1)
            data2 = ''.join(data)
            data22 = data2.count(' ')
            # print('Number of spaces:', data22)
            data3 = []
            for i in data:
                if len(i) > 0:
                    data3.append(len(i))
            data4 = sum(data3) / len(data3)
            # print('Average line length:', int(data4))
            lines = {'Number of lines': data1, 'Number of spaces:': data22, 'Average line length': int(data4)}
            record = json.dumps(lines)
            with open('output.json', 'w') as fh_o:
                fh_o.write(record)  # как в данном контексте при открытии output.json переместить курсор в начало?
    except IOError:
        print('File not found')
    return lines


print(report_file())





