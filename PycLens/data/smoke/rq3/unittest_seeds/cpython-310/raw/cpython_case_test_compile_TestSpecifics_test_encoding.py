# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_compile.py
# case: TestSpecifics_test_encoding

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    code = b'# -*- coding: badencoding -*-\npass\n'
    self.assertRaises(SyntaxError, compile, code, 'tmp', 'exec')
    code = '# -*- coding: badencoding -*-\n"Â¤"\n'
    compile(code, 'tmp', 'exec')
    self.assertEqual(eval(code), 'Â¤')
    code = '"Â¤"\n'
    self.assertEqual(eval(code), 'Â¤')
    code = b'"\xc2\xa4"\n'
    self.assertEqual(eval(code), '¤')
    code = b'# -*- coding: latin1 -*-\n"\xc2\xa4"\n'
    self.assertEqual(eval(code), 'Â¤')
    code = b'# -*- coding: utf-8 -*-\n"\xc2\xa4"\n'
    self.assertEqual(eval(code), '¤')
    code = b'# -*- coding: iso8859-15 -*-\n"\xc2\xa4"\n'
    self.assertEqual(eval(code), 'Â€')
    code = '"""\\\n# -*- coding: iso8859-15 -*-\nÂ¤"""\n'
    self.assertEqual(eval(code), '# -*- coding: iso8859-15 -*-\nÂ¤')
    code = b'"""\\\n# -*- coding: iso8859-15 -*-\n\xc2\xa4"""\n'
    self.assertEqual(eval(code), '# -*- coding: iso8859-15 -*-\n¤')
