# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_htmlparser.py
# case: HTMLParserTestCase_test_broken_condcoms

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    html = '<![if !(IE)]>broken condcom<![endif]><![if ! IE]><link href="favicon.tiff"/><![endif]><![if !IE 6]><img src="firefox.png" /><![endif]><![if !ie 6]><b>foo</b><![endif]><![if (!IE)|(lt IE 9)]><img src="mammoth.bmp" /><![endif]>'
    expected = [('unknown decl', 'if !(IE)'), ('data', 'broken condcom'), ('unknown decl', 'endif'), ('unknown decl', 'if ! IE'), ('startendtag', 'link', [('href', 'favicon.tiff')]), ('unknown decl', 'endif'), ('unknown decl', 'if !IE 6'), ('startendtag', 'img', [('src', 'firefox.png')]), ('unknown decl', 'endif'), ('unknown decl', 'if !ie 6'), ('starttag', 'b', []), ('data', 'foo'), ('endtag', 'b'), ('unknown decl', 'endif'), ('unknown decl', 'if (!IE)|(lt IE 9)'), ('startendtag', 'img', [('src', 'mammoth.bmp')]), ('unknown decl', 'endif')]
    self._run_check(html, expected)
