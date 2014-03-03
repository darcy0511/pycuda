copy /Y siteconf_windows.py siteconf.py
python setup.py build --compiler=msvc
pip install --user -e .
