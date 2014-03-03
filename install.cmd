copy /Y siteconf_windows.py siteconf.py
python setup.py build --compiler=msvc
call pip install --user -e .
