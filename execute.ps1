$Folder = './env/'
if (!(Test-Path -Path $Folder)){
  py -m venv env
  ./env/Scripts/activate
  pip install -r ./requirements.txt
  cd ./src/
  py main.py

} else {
  # environment exists!
  ./env/Scripts/activate
   cd ./src/
   py main.py
}
