# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: TextIOWrapperTest_test_reconfigure_defaults

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    txt = self.TextIOWrapper(self.BytesIO(), 'ascii', 'replace', '\n')
    txt.reconfigure(encoding=None)
    self.assertEqual(txt.encoding, 'ascii')
    self.assertEqual(txt.errors, 'replace')
    txt.write('LF\n')
    txt.reconfigure(newline='\r\n')
    self.assertEqual(txt.encoding, 'ascii')
    self.assertEqual(txt.errors, 'replace')
    txt.reconfigure(errors='ignore')
    self.assertEqual(txt.encoding, 'ascii')
    self.assertEqual(txt.errors, 'ignore')
    txt.write('CRLF\n')
    txt.reconfigure(encoding='utf-8', newline=None)
    self.assertEqual(txt.errors, 'strict')
    txt.seek(0)
    self.assertEqual(txt.read(), 'LF\nCRLF\n')
    self.assertEqual(txt.detach().getvalue(), b'LF\nCRLF\r\n')
