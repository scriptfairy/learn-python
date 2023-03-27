# learn-python

## Required software

1- Git which can be downloaded for Windows from [here](https://git-scm.com/downloads).
You only need Git if you are planning on committing your project into a Git repo.

2- VScode IDE with [Python externsion](https://marketplace.visualstudio.com/items?itemName=ms-python.python)

3- Pytest library which can be installed from the command line on Windows or Mac using pip3 package manager. After installing Pytest, type `pytest -h` on the command line to make sure it is working 

You might get a warning after installing pytest "WARNING: The scripts py.test.exe and pytest.exe are installed in 'C:\User........ bla bla bla"

You will need to add the directory where paytest installed into PATH on Window 10. To add a new path to Windows PATH, you can follow the instructions on [this page](https://www.architectryan.com/2018/03/17/add-to-the-path-on-windows-10/).

## Setup VS Code Workspace

Workspace is a container of files and one or multiple root folders with a configuration file called .code-workspace

Suppose we have a folder called "development" where we do all our coding. Inside development there is a folder called lean-python which is our weekly examples app. In VS Code open the folder "lean-python" then do 

file --> Save Workspace As 

And save the workspace file in the parent directory "development" not in lean-python. A file called learn-python.code-workspace will be saved in development. It is better to save the file outside the project code if we are going to use Git. This way it will not be committed to the repo because it is related to your setup environment.

When we start working with VS Code and there are no files open, go to:

file --> Open Workspace (from File menu) 

and navigate to learn-python.code-workspace to open.

## Create the App

When asked ChatGPT 

![ChatGPT](images/chatgpt_01.PNG)

Her answer was

my_project/  
├── app/  
│   ├── \_\_init__.py  
│   ├── module1.py  
│   └── module2.py  
└── tests/  
    ├── \_\_init__.py  
    ├── test_module1.py  
    └── test_module2.py  

In this example, we have an app/ directory for our application code, and a tests/ directory for our test code. Each test file (test_module1.py and test_module2.py) corresponds to a module in our app/ directory (module1.py and module2.py, respectively). 

By default, pytest will also discover and run any test functions that are defined in files with names that start with test_, so it's a good convention to use when naming your test files.

I noticed a file called \_\_init__.py" in each folder, I asked chatGPT again

![ChatGPT](images/chatgpt_02.PNG)

And this was the answer

*In Python, \_\_init__.py files are used to mark a directory as a Python package. When the Python interpreter encounters a directory that contains an \_\_init__.py file, it treats the directory as a package and allows you to import modules from it using Python's import statement.*

In our app we will not need to import modules so we will just create an empty \_\_init__.py in each folder for now.





