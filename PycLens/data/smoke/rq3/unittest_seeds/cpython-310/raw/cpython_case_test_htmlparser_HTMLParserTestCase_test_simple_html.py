# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_htmlparser.py
# case: HTMLParserTestCase_test_simple_html

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self._run_check("\n<!DOCTYPE html PUBLIC 'foo'>\n<HTML>&entity;&#32;\n<!--comment1a\n-></foo><bar>&lt;<?pi?></foo<bar\ncomment1b-->\n<Img sRc='Bar' isMAP>sample\ntext\n&#x201C;\n<!--comment2a-- --comment2b-->\n</Html>\n", [('data', '\n'), ('decl', "DOCTYPE html PUBLIC 'foo'"), ('data', '\n'), ('starttag', 'html', []), ('entityref', 'entity'), ('charref', '32'), ('data', '\n'), ('comment', 'comment1a\n-></foo><bar>&lt;<?pi?></foo<bar\ncomment1b'), ('data', '\n'), ('starttag', 'img', [('src', 'Bar'), ('ismap', None)]), ('data', 'sample\ntext\n'), ('charref', 'x201C'), ('data', '\n'), ('comment', 'comment2a-- --comment2b'), ('data', '\n'), ('endtag', 'html'), ('data', '\n')])
