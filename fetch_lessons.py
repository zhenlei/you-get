#!/usr/bin/env python3
import os, sys, re
import argparse
import logging
import subprocess
from bs4 import BeautifulSoup

src_dir = "{}/src/".format(os.path.dirname(os.path.realpath(__file__)) )
sys.path.insert(1, src_dir)

import you_get
from you_get import common

def get_lessons_dict(url):
    """get lessons url list"""

    html = common.get_content(url)
    soup = BeautifulSoup(html)
    div = soup.find('div', "b-courselist m-coursebox  ")
    lis = div.find_all('li')

    lessons = {}
    for li in lis:
        # print("-----------------")
        # print(li.span.string)
        lesson_str = li.span.string.strip()
        if li.a:
            print(li.a.get('href'))
            lessons[lesson_str]=li.a.get('href')
        else:
            lessons[lesson_str + "_空"]=None
    return lessons

# list = get_lessons_dict("http://v.ucas.ac.cn/course/getplaytitle.do?menuCode=2&code=49198&classcode=1&classid=GptTtpMKjbVrbKPQhR&sectionNumber=3&sectionDisplay=1")
# print(list)

def main():
    """the main entry point"""

    parser = argparse.ArgumentParser(
        prog='fetch_lessons',
        usage='fetch_lessons.py [OPTION]... URL...',
        description='A tiny downloader that scrapes the web',
        add_help=False,
    )

    parser.add_argument("-V" "--version", dest='version', action='store_true',
                        help="print version info")
    parser.add_argument("-o" "--output", dest='output', metavar='DIR', default='.',
                        help="print version info")
    parser.add_argument("URL", nargs='*', help=argparse.SUPPRESS)

    args = parser.parse_args()

    if args.version:
        print("version is 0.0")

    if args.URL:
        url = args.URL[0]

    if args.output:
        output = args.output

    if not os.path.exists(output):
        os.mkdir(output)

    logging.getLogger().setLevel(logging.DEBUG)
    print(url)
    urls = get_lessons_dict(url)
    for name, url in urls.items():
        if url:
            full_url = "http://v.ucas.ac.cn/course/" + url
            output_path = os.path.join(output, name)
            command = ['./you-get', '-d', '-f', '-t', '6', '-o', output_path, full_url]
            print(command)
            subprocess.Popen(command)
        print(output_path)
        print(full_url)


def entry_main():
    try:
        main()
    except KeyBoardInterrupt:
        sys.exit(1)

entry_main()
