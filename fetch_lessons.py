#!/usr/bin/env python3
import os, sys

src_dir = "{}/src/".format(os.path.dirname(os.path.realpath(__file__)) )
sys.path.insert(1, src_dir)

from you_get import common

def get_lessons_list(url):
    """get lessons url list"""

    html = common.get_content(url)

    print(html)


get_lessons_list("http://v.ucas.ac.cn/course/getplaytitle.do?menuCode=2&code=49198&classcode=1&classid=GptTtpMKjbVrbKPQhR&sectionNumber=3&sectionDisplay=1")
