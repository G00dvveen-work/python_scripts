import os
import re
import csv
import pandas as pd


log_dir = '../files/logs/CALL'
output_dir = '../files/output'

call_regex = re.compile(r'''
(\d\d:\d\d.\d+)
-
(\d+)
.*
t:computerName=(\w+),
.*
Usr=(\w+),
.*
Context=(.*?),
.*
Memory=(\d+),
MemoryPeak=(\d+),
InBytes=(\d+),
OutBytes=(\d+)
''', re.VERBOSE)

if os.path.exists(log_dir) & os.path.exists(output_dir):
    output_file = open(os.path.join(output_dir, 'calls.csv'), 'a+', encoding='utf8')
    output_file.truncate()
    output_file.write('Time,Duration,Computer,User,Context,Memory,Memory_peak,In_bytes,Out_bytes\n')
    for root, dirs, files in os.walk(log_dir):
        dirs[:] = [d for d in dirs if d.startswith('rphost_')]
        for file in files:
            current_file = open(os.path.join(root, file), encoding='utf8')
            for line in current_file:
                #print(len(line))
                data_string = call_regex.search(line)
                if data_string:
                    output_file.write(data_string.group(1) + "," + data_string.group(2) + "," + data_string.group(3) + "," + data_string.group(4) + "," + data_string.group(5) + "," + data_string.group(6) + "," + data_string.group(7) + "," + data_string.group(8) + "," + data_string.group(9) + "\n")
                    #print(data_string.groups())
            current_file.close()
    output_file.close()
else:
    print('Path does not exist')

calls = pd.read_csv(os.path.join(output_dir, 'calls.csv'))
print(calls[calls.Memory_peak > 500000])