import os


files = os.listdir(f'{os.getcwd()}/static/corpus')

for i, file in enumerate(files):
    os.rename(f'{os.getcwd()}/static/corpus/{file}', f'{os.getcwd()}/static/corpus/file_{i}.txt')
