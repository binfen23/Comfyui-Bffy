#从当前路径node文件夹的bffy.py中导入所有*类，也可以指定py文件内的某个类
from .node.bffy import *

# 需要创建唯一性，key为需要显示的名称，value为类名
NODE_CLASS_MAPPINGS = {
    "bffanyi": bffanyi,
}

# 名称映射，将bffanyi映射成想要的名称
NODE_DISPLAY_NAME_MAPPINGS = {
    "bffanyi": "缤纷翻译",

}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']