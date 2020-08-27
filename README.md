# ViperTools

Viper upload tool for malicious samples developed based on Python, supporting Python calls.

使用Python开发的Viper恶意样本批量上传工具，支持Python调用。

https://github.com/viper-framework/viper



## Deployment:



Python3



## Install:



```shell
git clone git@github.com:Loveforkeeps/ViperTools.git
```



## Using:

Help：

```shell
↳ python viper.py -h
usage: viper.py [-h] -f FILE [-t TAGS] [-p PROJECT] [-c CONFIG] [-d]

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  Select upload file
  -t TAGS, --tags TAGS  Tags for Sample (comma separated)
  -p PROJECT, --project PROJECT
                        Project for Sample
  -c CONFIG, --config CONFIG
                        Config file for Viper
  -d, --debug           Debug model
```



Config file Demo：

```ini
[viper-web]
host = 127.0.0.1
port = 8080
token  = xxxxxxx
```



Python Demo:

```python
from viper import Viper
viper = Viper(url='https://127.0.0.1:8080', token='xxxxx')
viper.debug = True
viper.upload('Sample.exe', tags='Trojan', project='APT-12')
```





## Update:

* None



### Issue Log:

* None



### Todo List:

* None



## Running  screenshot:

* None



## License:

This project is licensed under the [MIT license](http://opensource.org/licenses/mit-license.php) 

## Acknowledgments：

* None