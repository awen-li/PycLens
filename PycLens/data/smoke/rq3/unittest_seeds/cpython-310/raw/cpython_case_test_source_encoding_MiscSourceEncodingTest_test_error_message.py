# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_source_encoding.py
# case: MiscSourceEncodingTest_test_error_message

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    compile(b'# -*- coding: iso-8859-15 -*-\n', 'dummy', 'exec')
    compile(b'\xef\xbb\xbf\n', 'dummy', 'exec')
    compile(b'\xef\xbb\xbf# -*- coding: utf-8 -*-\n', 'dummy', 'exec')
    with self.assertRaisesRegex(SyntaxError, 'fake'):
        compile(b'# -*- coding: fake -*-\n', 'dummy', 'exec')
    with self.assertRaisesRegex(SyntaxError, 'iso-8859-15'):
        compile(b'\xef\xbb\xbf# -*- coding: iso-8859-15 -*-\n', 'dummy', 'exec')
    with self.assertRaisesRegex(SyntaxError, 'BOM'):
        compile(b'\xef\xbb\xbf# -*- coding: iso-8859-15 -*-\n', 'dummy', 'exec')
    with self.assertRaisesRegex(SyntaxError, 'fake'):
        compile(b'\xef\xbb\xbf# -*- coding: fake -*-\n', 'dummy', 'exec')
    with self.assertRaisesRegex(SyntaxError, 'BOM'):
        compile(b'\xef\xbb\xbf# -*- coding: fake -*-\n', 'dummy', 'exec')
