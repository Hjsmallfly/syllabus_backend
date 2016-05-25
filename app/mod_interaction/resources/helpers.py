# coding=utf-8
__author__ = 'smallfly'

from datetime import datetime
from copy import deepcopy
import config
import os
import json

def clean_arguments(args, accepted):
    """
    清除不在 accepted 列表内的 键值对
    :param args: 原来的字典
    :param accepted: 允许的字段
    :return: None
    """
    args_for_iteration = deepcopy(args)
    for arg in args_for_iteration:
        if arg not in accepted:
            # assert isinstance(args, dict)
            args.pop(arg)


def timestamp_to_string(timestamp, format="%Y-%m-%d %H:%M:%S"):
    """
    将timestamp转换成时间
    :param timestamp:
    :return:
    """
    try:
        time_string = datetime.fromtimestamp(int(timestamp))
        time_string = time_string.strftime(format)
    except TypeError as e:
        print("timestamp_to_string: ", timestamp)
        return None
    return time_string


base_dir = os.path.dirname(__file__)
VERSION_FILE = "version.txt"
filename = os.path.join(config.config["VERSION_DIR"], VERSION_FILE)
# print(filename)
def load_version():
    if os.path.exists(filename):
        with open(filename, encoding="utf-8") as f:
            json_obj = json.load(f, encoding='utf-8')
        return json_obj
    return None

NOTIFICATION_FILE_PATH = os.path.join(config.config["BANNER_DIR"], "banner.txt")

def get_notification():
    if os.path.exists(NOTIFICATION_FILE_PATH):
        with open(NOTIFICATION_FILE_PATH, encoding='utf-8') as f:
            return json.load(f, encoding='utf-8')
    return None


def make_notification(urls, links, descs):
    """
    成功返回True, 否则 False
    :param urls: 所有图片url
    :param links: 所有跳转url
    :param descs: 所有描述
    :return:
    """
    if (len(urls) != len(links) or len(urls) != len(descs)):

        return False
