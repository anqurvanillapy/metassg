# -*- coding: utf-8 -*-

from metassg import MetaSSG

import codecs
from os.path import basename, splitext
from markdown import Markdown
from bs4 import BeautifulSoup


class MockSSG(MetaSSG):
    """\
    - Mock SSG for multiple usage, e.g.
        + slideshow generator (without `clean()` method)
        + blog, wiki (with `clean()` method)
    """
    tmplpath = 'tests/data'
    ifpath = 'foo'
    ofpath = 'bar'

    def render(self, posts):
        """Render Jinja2 templates"""
        pages = []

        for t in posts:
            try:
                with codecs.open(t, 'r', encoding='utf-8') as f:
                    md = Markdown(extensions=self.pymd_exts)
                    html = BeautifulSoup(md.convert(f.read()), 'lxml')
                    meta = md.Meta
                    fname = lambda x: '{}.html'.format(splitext(basename(x))[0])
                    pages.append({'html': html, 'meta': meta, 'fname': fname(t)})
            except Exception as e:
                raise e

        return pages
