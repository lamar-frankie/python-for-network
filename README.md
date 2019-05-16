# python-for-network
A short workshop on the basics of Git Python and Ansible for Network Engineers

## Pre-work

### Windows

#### Installing Python

1. Open a web browser and navigate to [Python.org](https://www.python.org/downloads/windows/)
2. Choose the latest release
3. Click "Windows x86-64 executable installer"
4. Save the file
5. After the installer finishes downloading, open it.
6. Run the installer.

#### Installing Ansible

**Note:** If you already have cygwin installed **skip to step 11** 
1. Download [Cygwin](https://cygwin.com/install.html)
2. Run the Cygwin installation file.
3. When asked which download source you’d like to use, select “Install from Internet”.
4. Choose the default "C:\cygwin64" when asked to choose a root directory
5. Select a directory where you’d like to install your Cygwin packages
6. Select the method which suits your internet connection type. e.g If you’re not connecting from behind a proxy, select the “Direct Connection” option.
7. Select a mirror to download your packages from. Any option in the list will do
8. You’ll then be provided with a list of packages which you can download. **Don’t select anything**, just click “Next”. 
9. In reference to dependencies leave everything default and just click next. 
10. Double click on the “Cygwin64 Terminal” icon.
11. Set up an alias which points to the “setup-x86_64.exe” file you downloaded in Step 1: 
```bash
alias cyg-get="/cygdrive/d/path/to/cygwin/setup-x86_64.exe -q -P"
```

12. Install Ansible's dependencies:
```bash
curl cygwin32-gcc-g++ gcc-core gcc-g++ git libffi-devel nano openssl openssl-devel python-crypto python2 python2-devel python2-openssl python2-pip python2-setuptools tree
```

13. Install Ansible
```bash
pip install ansible
```

### **MacOS**

#### Installing Python

1. Install Homebrew
```bash
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```
2. Add Homebrew to your path
```bash
export PATH="/usr/local/opt/python/libexec/bin:$PATH"
```
 3. Install Python 3.X
 ```bash
 brew install python
 ```

#### Installing Ansible

1. Install Ansible
```bash
brew install ansible
```

### **Linux**

#### Installing Python

1. Update package manager repos
```bash
sudo apt update
```

2. Install Python
```bash
sudo apt install -y python
```

#### Installing Ansible

1. Update package manager repos
```bash
sudo apt update
```

2. Install Ansible
```bash
sudo apt install -y ansible
```



## Additional Resources

### Git

[Git Docs](https://git-scm.com/docs/gittutorial)

[Code Academy](https://www.codecademy.com/learn/learn-git)

[Git Cheat Sheet](https://education.github.com/git-cheat-sheet-education.pdf)


### Python

[Real Python](https://realpython.com/)

[Python for Everyone](https://www.coursera.org/specializations/python)

[Talk Python To Me](https://talkpython.fm/)

[100 Days of Python](https://training.talkpython.fm/courses/explore_100days_in_python/100-days-of-code-in-python)

