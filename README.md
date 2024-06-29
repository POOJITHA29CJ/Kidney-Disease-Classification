## STEP 1:
Github link
Take git hub link and clone it 
## STEP 2:
Create template.py to structure folder and files
## STEP 3 :
Commit changes in github
```bash 
git add . 
```
```bash  
git commit -m "message here"
```
```bash
git push origin main
```
## STEP 4:
Mention requirements i need in requirements.txt(works well in testing)
## Create virtual environment
```bash
conda create -n kidney python=3.8
```
## Activate the virtual environment
```bash
conda activate kidney
```
## Install the requirements
```bash
pip install -r requirements.txt
```
# PROJECT WORKFLOW
1. Update config.yaml
2. Update secrets.yaml[Optional]
3. Update params.yaml
4. Update entity
5. Update the configuration manager in src config
6. Update the components
7. Update pipeline
8. Update main.py
9. Update the dvc.yaml
10. app.py


