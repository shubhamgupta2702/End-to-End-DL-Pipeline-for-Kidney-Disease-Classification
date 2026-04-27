import os
import sys
import yaml
import json
import joblib
import yaml
import base64
from pathlib import Path
from typing import Any
from box import ConfigBox
from ensure import ensure_annotations
from src.logger.logger import logger
from src.exception.exception import CustomException

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Reads a YAML file and returns its contents as ConfigBox.

    Args:
        path_to_yaml (Path): Path to yaml file.

    Returns:
        ConfigBox: YAML content with dot notation access.

    Raises:
        FileNotFoundError: If YAML file does not exist.
        ValueError: If YAML file is empty.
        Exception: For YAML parsing or unexpected errors.
    """
    
    try:
        if not path_to_yaml.exists():
            raise FileNotFoundError(f"YAML file not found at: {path_to_yaml}")

        with open(path_to_yaml, "r") as yaml_file:
            content = yaml.safe_load(yaml_file)

            if content is None:
                raise ValueError("YAML file is empty")

            return ConfigBox(content)

    except yaml.YAMLError as e:
        raise Exception(f"Error parsing YAML file: {e}")

    except Exception as e:
        raise e
      
    
@ensure_annotations
def save_json(path: Path, data: dict):
    """save json data

    Args:
        path (Path): path to json file
        data (dict): data to be saved in json file
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

    logger.info(f"json file saved at: {path}")


@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """load json files data

    Args:
        path (Path): path to json file

    Returns:
        ConfigBox: data as class attributes instead of dict
    """
    with open(path) as f:
        content = json.load(f)

    logger.info(f"json file loaded succesfully from: {path}")
    return ConfigBox(content)
  

def decodeImage(imgstring, fileName):
    imgdata = base64.b64decode(imgstring)
    with open(fileName, 'wb') as f:
        f.write(imgdata)
        f.close()
        
        
def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath, "rb") as f:
        return base64.b64encode(f.read())
      
def get_size(path: Path) -> str:
    """get size in KB

    Args:
        path (Path): path of the file

    Returns:
        str: size in KB
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"


@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """create list of directories

    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")
