import yaml
from util.root_dir import find_file


class DataFile:

    def read_file(self,file_name,file_path='data'):
        full_file_path = find_file(file_name, file_path)
        with open(full_file_path,'r',encoding='utf8') as file:
            data = yaml.safe_load(file)
            return data

    def write_file(self,file_name,data,file_path='data'):
        full_file_path = find_file(file_name, file_path)
        with open(full_file_path,'w',encoding='utf8') as file:
            yaml.safe_dump(data,file)

    def append_fila(self):
        pass




a = DataFile()
data = {"channel":"alipay"}
a.write_file('data.yaml',data)
b = a.read_file('data.yaml')
print(b['channel'])