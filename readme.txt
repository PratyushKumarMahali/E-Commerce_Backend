Download pip
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py

Install pip
python get-pip.py

Install Virtual Environment
pip install virtualenv

Create Virtual Environment
virtualenv venv

Start Virtual Environment
source venv/scripts/activate (for Windows)
source venv/bin/activate (for Ubuntu and Mac)

Install Requirements
pip install -r requirement.txt

Change Interpreter in Visual Studio Code or any other platform
View -> Command Palette -> Python: Select Interpreter -> Enter Interpreter Path -> Find
venv -> Scripts -> python

Start Server
uvicorn main:app --reload