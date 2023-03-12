echo [$(date)]: "START" 
echo [$(date)]: "creating env with python 3.7 version" 
conda create --prefix ./env python=3.7 -y
echo [$(date)]: "activating the environment" 
source activate ./env
echo [$(date)]: "installing the requirements" 
pip install -r requirements.txt
echo [$(date)]: "END"