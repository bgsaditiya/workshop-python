#Membuat lingkungan virtual dan menentukan direktori
python3 -m venv tutorial-env

#Mengaktifkan lingkungan virtual
tutorial-env\Scripts\activate.bat

$ source ~/envs/tutorial-env/bin/activate
(tutorial-env) $ python
Python 3.5.1 (default, May  6 2016, 10:59:36)
  ...
>>> import sys
>>> sys.path
['', '/usr/local/lib/python35.zip', ...,
'~/envs/tutorial-env/lib/python3.5/site-packages']
>>>

