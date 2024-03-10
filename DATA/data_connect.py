from dataclasses import dataclass

@dataclass
class URL:
    """url подключения к сайту"""
    url: str = "https://www.newegg.com/"
