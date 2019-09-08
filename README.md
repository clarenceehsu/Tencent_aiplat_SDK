# Tencent_aiplat_SDK 腾讯AI平台SDK


这是**基于 Python3**的**第三方SDK库**

由于平台只提供了文档以及简单的 Python2 样例，所以我读了一下文档，写了这个 SDK ，从而简化操作，后续只用考虑调用以及使用部分。

~~有时间的话我会继续完善成一个完整方便的 SDK ，如果有问题欢迎 issue 。~~

该 SDK 已经基本完善，如有问题欢迎 issue 。

后续计划将这个包加入 ``pypi`` ，以及添加更多的使用细则以快速上手。

## 使用方法

可见 ``test.py`` 。

登录腾讯AI平台，新建或打开已有的项目并获取 ``APPID`` 以及 ``APPKEY`` ，然后写入代码进行实例化；

对应的功能可以查看官方文档，或者库中的 ``__init__.py`` ；返回的字典，具体请翻阅文档的数据返回部分，然后取出对应数据使用即可。

---

## 更新日志

### 9/5/2019

- 对文件结构进行了修改。

### 8/1/2019
- 添加了其他的功能方法，目前功能方面已经基本完善；
- 改变了文件结构，使其更接近标准；
- 将不同的功能进行了拆分，方便后续进行不同功能的调试和部署；
- 改善了业务逻辑。

### 8/1/2019
- 对代码的结构进行了标准化，减少了调用次数，增加了错误值返回；
- 函数名遵从平台命名进行规范，防止误操作；
- 抛弃了以往图使用方便的“开箱即用”的风格。现在调用方法将直接返回字典，方便后续进行自定义调整。

### 5/28/2019

- 对目前的每一个功能进行了测试，并且对代码结构进行了精简；添加了一段示例代码方便测试。

---

**Python3 Only**

SDK for Tencent AI Platform. Issue and commit if any error occours.