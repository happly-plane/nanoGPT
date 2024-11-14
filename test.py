import pandas as pd
import os

file_extensions = '.jsonl'
data_path = 'TinyStoriesAdv-zh/train_data'


# image_files = [os.path.join(root, file) 
#                for root, dirs, files in os.walk(data_path) 
#                for file in files 
#                if file.lower().endswith(image_extensions)]
# keywords                                                  唱,官员,差
# text_format                                                   故事
# text
def merge_data(path):
    data_files = [os.path.join(root, file) 
               for root, dirs, files in os.walk(path) 
               for file in files 
               if file.lower().endswith(image_extensions)]
    for data_file in data_files:
        df = pd.read_json(data_file,lines=True)
        column_name = 'keywords'
        text_column = 'keyword'
        export_cloumn = ['keyword','text']
        new_column_names = {'keywords': 'keyword'}
        if column_name in df.columns:
            print(data_file,1)
            df = df.rename(columns=new_column_names)
            df = df[export_cloumn]
        elif text_column not in df.columns:
            print(data_file,2)
            value_to_fill = 'math'
            df = df.assign(**{text_column: value_to_fill})
        else:
            print(data_file,3)
            df = df[export_cloumn]
        df.to_csv(f'{data_file}.txt', sep=' ', index=False)
