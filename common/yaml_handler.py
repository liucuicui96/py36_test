'''读取yaml文件'''
import yaml

def read_yaml(fpath):
    '''通过fpath文件路径读取yaml数据
    得到的是一个字典'''
    with open(fpath,encoding='utf-8') as f:
        data=yaml.load(f,Loader=yaml.SafeLoader)
    return data

# yaml_path=os.path.join(config_path,'config.yaml')
# yaml_config=read_yaml(yaml_path)
#
# user_path=os.path.join(config_path,'security.yaml')
# user_config=read_yaml(user_path)