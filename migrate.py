import os

file_names = []
for (path, dirs, files) in os.walk('.'):
    for file_name in files:
        if 'accuracies' in file_name or '.tsv' not in file_name:
            continue
        
        file_names.append(path + '\\' +  file_name)

for file_name in file_names:
    lines = []
    header = []
    
    with open(file_name, 'r') as file:
        lines = file.readlines()
        header_len = len(lines[0].split('\t'))
    
    cont_attrs = ['c' for val in range(header_len - 1)] + ['d'] + ['\n']
    class_attr = ['' for val in range(header_len - 1)] + ['class'] + ['\n']
    
    lines.insert(1, '\t'.join(cont_attrs))
    lines.insert(2, '\t'.join(class_attr))

    with open(file_name.replace('.tsv', '.tab'), 'wt') as file:
        file.writelines(lines)     
