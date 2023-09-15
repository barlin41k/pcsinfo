import os
import sys
import subprocess
import getpass

class User:
    def __init__(self):
        # USERNAME
        try:
            self.username = getpass.getuser()
        except Exception as error:
            self.error1 = "\033[31m" + f"Error with get the username: {error}" + "\033[0m"
            print(self.error1)
            self.username = None
        # PLATFORM
        try:
            self.platform = sys.platform
        except Exception as error:
            self.error2 = "\033[31m" + f"Error with get the system platform: {error}" + "\033[0m"
            print(self.error2)
            self.platform = None
        # OS NAME
        try:
            self.os = os.name
        except Exception as error:
            self.error4 = "\033[31m" + f"Error with get the OS name: {error}" + "\033[0m"
            print(self.error3)
            self.os = None
        # HOME DIR
        try:
            self.homedir = os.path.expanduser("~")
        except Exception as error:
            self.error5 = "\033[31m" + f"Error with get the home dir: {error}" + "\033[0m"
            print(self.error4)
            self.homedir = None
        #print(f"{self.username}, {self.platform}, {self.os}, {self.homedir}")
    
    def system_username(self) -> str:
        if self.username:
            return self.username
        else:
            print(self.error1)
            return None
    
    def system_platform(self) -> str:
        if self.platform:
            return self.platform
        else:
            print(self.error2)
            return None
    
    def os_name(self) -> str:
        if self.os:
            return self.os
        else:
            print(self.error3)
            return None
    
    def home_dir(self) -> str:
        if self.homedir:
            return self.homedir
        else:
            print(self.error4)
            return None
