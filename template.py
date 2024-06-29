import os
from pathlib import Path #Path is a class
import logging
#logging string (instead of printing everywhere)
logging.basicConfig(level=logging.INFO,format='[%(asctime)s]:%(message)s:')#acsi time
project_name='KidneyTumorClassifier'
list_of_files=[
    ".github/workflow/.gitkeep",#empty folder wont be commited in github
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html"
]
for fp in list_of_files:
    fp=Path(fp) # Path is given to avoid error in windows (robust code)
    filedir,filename=os.path.split(fp)
    if filedir!="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating directory:{filedir} for the file:{filename}")
    if(not os.path.exists(fp)) or (os.path.getsize(fp)==0):
        with open(fp,"w") as f:
            pass
        logging.info(f"Creating empty file:{fp}")
    else:
        logging.info(f"{filename} is already exists")
        
    
    

