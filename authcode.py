# -*- Encoding: utf-8 -*-
import socket
from httplib2 import Http
import urllib

import ImageFile
from pytesseract import image_to_string


def recog(data, threshold = 140):
    p = ImageFile.Parser()
    p.feed(data)
    im = p.close()
    imgry = im.convert('L') 
    out = imgry.point(lambda i: 0 if i < threshold else 255)
    return image_to_string(out)


def get_authcode(url, method='GET'):
    h = Http(timeout=2)

    try:
        rsp, content = h.request(url, method)
    except socket.timeout:
        return None
    else:
        return rsp['set-cookie'], recog(content)


if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        url = sys.argv[1]
    else:
        url = raw_input(u'url_authcode: ')

    print get_authcode(url)
