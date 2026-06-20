# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree.py
# case: ElementTreeTest_test_xpath_tokenizer

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    from xml.etree import ElementPath

    def check(p, expected, namespaces=None):
        self.assertEqual([op or tag for (op, tag) in ElementPath.xpath_tokenizer(p, namespaces)], expected)
    check('*', ['*'])
    check('text()', ['text', '()'])
    check('@name', ['@', 'name'])
    check('@*', ['@', '*'])
    check('para[1]', ['para', '[', '1', ']'])
    check('para[last()]', ['para', '[', 'last', '()', ']'])
    check('*/para', ['*', '/', 'para'])
    check('/doc/chapter[5]/section[2]', ['/', 'doc', '/', 'chapter', '[', '5', ']', '/', 'section', '[', '2', ']'])
    check('chapter//para', ['chapter', '//', 'para'])
    check('//para', ['//', 'para'])
    check('//olist/item', ['//', 'olist', '/', 'item'])
    check('.', ['.'])
    check('.//para', ['.', '//', 'para'])
    check('..', ['..'])
    check('../@lang', ['..', '/', '@', 'lang'])
    check('chapter[title]', ['chapter', '[', 'title', ']'])
    check('employee[@secretary and @assistant]', ['employee', '[', '@', 'secretary', '', 'and', '', '@', 'assistant', ']'])
    check('@{ns}attr', ['@', '{ns}attr'])
    check('{http://spam}egg', ['{http://spam}egg'])
    check('./spam.egg', ['.', '/', 'spam.egg'])
    check('.//{http://spam}egg', ['.', '//', '{http://spam}egg'])
    check('{ns}*', ['{ns}*'])
    check('{}*', ['{}*'])
    check('{*}tag', ['{*}tag'])
    check('{*}*', ['{*}*'])
    check('.//{*}tag', ['.', '//', '{*}tag'])
    check('./xsd:type', ['.', '/', '{http://www.w3.org/2001/XMLSchema}type'], {'xsd': 'http://www.w3.org/2001/XMLSchema'})
    check('type', ['{http://www.w3.org/2001/XMLSchema}type'], {'': 'http://www.w3.org/2001/XMLSchema'})
    check('@xsd:type', ['@', '{http://www.w3.org/2001/XMLSchema}type'], {'xsd': 'http://www.w3.org/2001/XMLSchema'})
    check('@type', ['@', 'type'], {'': 'http://www.w3.org/2001/XMLSchema'})
    check('@{*}type', ['@', '{*}type'], {'': 'http://www.w3.org/2001/XMLSchema'})
    check('@{ns}attr', ['@', '{ns}attr'], {'': 'http://www.w3.org/2001/XMLSchema', 'ns': 'http://www.w3.org/2001/XMLSchema'})
