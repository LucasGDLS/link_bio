source venv/bin/activate
pip install --upgrade pip
pip install -r
reflex init
reflex export --frontend-only
rm -rf public
unzip frontend.zip -d public
rm -f frontend.zip 
deactivate