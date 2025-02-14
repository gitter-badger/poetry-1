
# pip3 install pypinyin
from pypinyin import lazy_pinyin
import os
import shutil


class Profile:
    def __init__(self, href, author, title):
        self.href = href
        self.author = author
        self.title = title

    def __str__(self):
        return self.author + ' ' + self.title + ' ' + self.href

    def poet_path(self):
        pinyin = "".join(lazy_pinyin(self.author))
        return os.path.join('.', 'tmp', self.author + '_' + pinyin)

    def file_path(self):
        return os.path.join(self.poet_path(), self.title + '.pt')


def write_poem(p, content):
    poet_dir_path = p.poet_path()
    if not os.path.exists(poet_dir_path):
        os.makedirs(poet_dir_path)
    title = p.title
    poem_path = p.file_path()
    content = 'title:' + title + '\r\n' + 'date:\r\n\r\n' + content
    try:
        with open(poem_path, 'w') as file:
            file.write(content)
    except OSError:
        print('author:' + p.author + '\r\n')
        print('title:' + title + '\r\n')
        print('-----------------------')


def remove_tmp_all():
    try:
        shutil.rmtree(os.path.join('.', 'tmp'))
    except FileNotFoundError:
        pass
