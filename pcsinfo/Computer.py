import psutil
import os
import GPUtil
import cpuinfo

class Computer:
    def __init__(self):
        # RAM
        try:
            ram = psutil.virtual_memory()
            self.ram = round(ram.total / (1024**3), 2)
        except Exception as error:
            self.error1 = "\033[31m" + f"Error with get the RAM: {error}" + "\033[0m"
            print(self.error1)
            self.ram = None
        # DISK
        try:
            disk = psutil.disk_usage('/')
            self.disk = round(disk.total / (1024**3), 2)
        except Exception as error:
            self.error2 = "\033[31m" + f"Error with get the disk: {error}" + "\033[0m"
            print(self.error2)
            self.disk = None
        # GPU
        try:
            gpus = GPUtil.getGPUs()
            self.gpu = gpus[0].name
        except Exception as error:
            self.error3 = "\033[31m" + f"Error with get the GPU: {error}" + "\033[0m"
            print(self.error3)
            self.gpu = None
        # CPU
        try:
            processor = cpuinfo.get_cpu_info()
            self.processor = processor['brand_raw']
        except Exception as error:
            self.error4 = "\033[31m" + f"Error with get the CPU: {error}" + "\033[0m"
            print(self.error4)
            self.processor = None
        # CPU CORES
        try:
            self.cpu_cores = os.cpu_count()
        except Exception as error:
            self.error5 = "\033[31m" + f"Error with get the CPU cores: {error}" + "\033[0m"
            print(self.error5)
            self.cpu_cores = None
        #print(f"{self.ram}, {self.disk}, {self.processor}, {self.cpu_cores}, {self.gpu}, {self.processor}")
    def processor(self) -> str:
        if self.processor:
            return self.processor
        else:
            print(self.error4)
            return None
    
    def disk(self) -> float:
        if self.disk:
            return self.disk
        else:
            print(self.error2)
            return None
    
    def processor_cores(self) -> int:
        if self.cpu_cores:
            return self.cpu_cores
        else:
            print(self.error5)
            return None
    
    def videocard(self) -> str:
        if self.gpu:
            return self.gpu
        else:
            print(self.error3)
            return None
    
    def ram(self) -> float:
        if self.ram:
            return self.ram
        else:
            print(self.error1)
            return None
