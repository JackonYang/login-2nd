网站模拟登陆
============

介于用户直接登录与第三方登录之间, 姑且称之为 第 2 方登录. :)

翻译成普通话就是:
**模拟浏览器, 实现各网站的自动登陆**

本质为获取登录后的 cookie

## 网站列表

- [renren.com]()
- [易网通物流平台](http://mf.sealink.net.cn/)

## 用法

#### 自动登录

`config/` 目录下, 网站的配置文件，保存为 `website_name.json`

```shell
$ python login.py website_name
```

如: `python login.py renren`

#### 验证码自动识别

```python
$ python authcode.py htt://url/to/authcode
```

如:

```shell
$ python authcode.py http://mf.sealink.net.cn/authcode
# output: ('JSESSIONID=38F1DFB4AE861EFFB722FFA53DC50AA3.mqbak; Path=/', '9936')
$ python authcode.py http://newmf.szedi.com.cn/jsp/common/g_image.jsp
# output: ('JSESSIONID=12AE7574ADD763758232D6D25D8BB590; Path=/', '0828')
```

## 开发环境搭建

#### 依赖

自动登录模块, 使用 httplib2 处理 http 消息.

验证码识别, 依赖:

1. [PIL](http://effbot.org/imagingbook/pil-index.htm).
    Python Imaging Library, userd for noise reduction. workflow: RGB -> grayscale image -> binary image
2. [Tesseract-OCR](https://github.com/justin/tesseract-ocr). google OCR Engine
3. [pytesseract](https://github.com/madmaze/pytesseract). a wrapper for google's Tesseract-OCR


#### 安装

ubuntu, 执行 `./build_dev.sh` 即可, 脚本内容如下:

```shell
#!/bin/bash

# PIL
sudo apt-get update
sudo apt-get install libjpeg8-dev zlib1g-dev libfreetype6-dev

sudo ln -s /usr/lib/x86_64-linux-gnu/libjpeg.so /usr/lib
sudo ln -s /usr/lib/x86_64-linux-gnu/libfreetype.so /usr/lib
sudo ln -s /usr/lib/x86_64-linux-gnu/libz.so /usr/lib

sudo pip install PIL --allow-external PIL --allow-unverified PIL

sudo ln -s /usr/include/freetype2 /usr/include/freetype

# OCR engine from google
sudo apt-get install  tesseract-ocr

sudo pip install -r requirements.txt
```
