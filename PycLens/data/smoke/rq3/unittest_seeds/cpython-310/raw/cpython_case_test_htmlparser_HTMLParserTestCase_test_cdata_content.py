# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_htmlparser.py
# case: HTMLParserTestCase_test_cdata_content

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    contents = ['<!-- not a comment --> &not-an-entity-ref;', "<not a='start tag'>", '<a href="" /> <p> <span></span>', 'foo = "</scr" + "ipt>";', 'foo = "</SCRIPT" + ">";', 'foo = <\n/script> ', '<!-- document.write("</scr" + "ipt>"); -->', '\n//<![CDATA[\ndocument.write(\'<s\'+\'cript type="text/javascript" src="http://www.example.org/r=\'+new Date().getTime()+\'"><\\/s\'+\'cript>\');\n//]]>', '\n<!-- //\nvar foo = 3.14;\n// -->\n', 'foo = "</sty" + "le>";', '<!-- ☃ -->']
    elements = ['script', 'style', 'SCRIPT', 'STYLE', 'Script', 'Style']
    for content in contents:
        for element in elements:
            element_lower = element.lower()
            s = '<{element}>{content}</{element}>'.format(element=element, content=content)
            self._run_check(s, [('starttag', element_lower, []), ('data', content), ('endtag', element_lower)])
