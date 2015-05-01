# -*- Encoding: utf-8 -*-
import os
import json


CFG_PATH = os.path.join(os.path.dirname(__file__), 'config')


def default_error(website, err_no, err_msg):
    print 'ERROR %s | website=%s | %s' % (err_no, website, err_msg)


def load_config(website, err_hdlr=default_error):
    """load config from file.
    
    json by default.
    """
    cfg_file = os.path.join(CFG_PATH, '%s.json' % website)
    try:
        with open(cfg_file, 'r') as f:
            cfg = json.load(f)
    except IOError:
        err_no, err_msg = 1, 'config file not found'
        err_hdlr(website, err_no, err_msg)
    except ValueError:
        err_no, err_msg = 2, 'config file format error'
        err_hdlr(website, err_no, err_msg)
    else:
        return cfg

    return None  # error




if __name__ == '__main__':
    print load_config('renren')
    print load_config('example.com')
