# utils/config_loader.py
import yaml
import os
from pathlib import Path
from typing import Dict, Any

class yaml_loader:
    _urls: Dict[str, Any] = None

    @classmethod
    def load(cls, urls_path: str = None) -> None:
        """加载 YAML 配置文件"""
        if not urls_path:
            # 默认从项目根目录的 config 文件夹读取
            base_dir = Path(__file__).resolve().parent.parent
            urls_path = os.path.join(base_dir, "config", "url.yaml")

        try:
            with open(urls_path, 'r', encoding='utf-8') as f:
                cls._config = yaml.safe_load(f)
        except FileNotFoundError:
            raise ValueError(f"文件不存在: {urls_path}")
        except yaml.YAMLError as e:
            raise ValueError(f"文件解析错误: {str(e)}")

    @classmethod
    def get(cls, key_path: str, default=None) -> Any:
        """通过点分路径获取配置值"""
        if cls._urls is None:
            cls.load()

        keys = key_path.split('.')
        value = cls._urls
        for key in keys:
            value = value.get(key)
            if value is None:
                return default
        return value