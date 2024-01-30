

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
    
@dataclass
class DataTransformationConfig:
    root_dir: Path
    data_path: Path
    
@dataclass
class ModelTrainerConfig:
    root_dir: Path
    train_data_path: Path
    test_data_path: Path
    model_name: str
    alpha: float
    l1_ratio: float
    target_column: str
    