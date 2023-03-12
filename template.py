import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s: ')

package_name = "housing"

list_of_files = [
   ".github/workflows/.gitkeep",
   f"{package_name}/__init__.py", 
   f"{package_name}/components/__init__.py",
   f"{package_name}/components/data_ingestion.py",
   f"{package_name}/components/data_validation.py",
   f"{package_name}/components/data_transformation.py",
   f"{package_name}/components/model_trainer.py",
   f"{package_name}/components/model_evaluation.py",
   f"{package_name}/components/model_pusher.py",
   f"{package_name}/util/__init__.py",
   f"{package_name}/util/util.py", 
   f"{package_name}/config/__init__.py",
   f"{package_name}/config/configuration.py", 
   f"{package_name}/pipeline/__init__.py",
   f"{package_name}/pipeline/pipeline.py", 
   f"{package_name}/entity/__init__.py",
   f"{package_name}/entity/artifact_entity.py",
   f"{package_name}/entity/config_entity.py",
   f"{package_name}/entity/experiment.py",
   f"{package_name}/entity/housing_predictor.py",
   f"{package_name}/entity/model_factory.py",
   f"{package_name}/exception/__init__.py",
   f"{package_name}/logger/__init__.py", 
   f"{package_name}/constants/__init__.py",
   "config/config.yaml",
   "config/schema.yaml",
   "init_setup.sh",#for creating enviormnet
   "requirements.txt", 
   "setup.py",#These three file are for setup project as python package
   "research/trials.ipynb", 
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)#This will return me 2 thing 1:dir path, 2:filename(x/y/z,t.txt)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass # create an empty file
            logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"{filename} already exists")