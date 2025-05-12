# data_extractor.py
from typing import Union, Dict, List, Any
def extract_nested_ids(data: Union[Dict, List], key: str = 'id') -> List[Any]:
    """
    递归提取嵌套结构中的指定键值

    Args:
        data: 包含嵌套结构的字典/列表
        key: 要提取的键名 (默认: 'id')

    Returns:
        List[Any]: 找到的所有键值列表 (可能包含None)

    Examples:
        >>> data = {'a': {'id': 1}, 'b': [{'c': {'id': 2}}]}
        >>> extract_nested_ids(data)
        [1, 2]
    """
    ids = []

    # 处理字典类型
    if isinstance(data, dict):
        # 提取当前层级键值
        if key in data:
            ids.append(data.get(key))
        # 递归处理所有值
        for value in data.values():
            ids.extend(extract_nested_ids(value, key))

    # 处理列表类型
    elif isinstance(data, list):
        for item in data:
            ids.extend(extract_nested_ids(item, key))

    return [item for item in ids if item is not None]  # 过滤空值