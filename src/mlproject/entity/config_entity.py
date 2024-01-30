

from pathlib import Path
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_file_path: Path
    unzip_path: Path
    
    
@dataclass
class DataValidationConfig:
    root_dir: Path
    unzip_path: Path
    STATUS_file: str 
    all_schema: list
    