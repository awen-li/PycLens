# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pathlib.py
# case: _BasePathTest_test_write_text_with_newlines

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    p = self.cls(BASE)
    (p / 'fileA').write_text('abcde\r\nfghlk\n\rmnopq', newline='\n')
    self.assertEqual((p / 'fileA').read_bytes(), b'abcde\r\nfghlk\n\rmnopq')
    (p / 'fileA').write_text('abcde\r\nfghlk\n\rmnopq', newline='\r')
    self.assertEqual((p / 'fileA').read_bytes(), b'abcde\r\rfghlk\r\rmnopq')
    (p / 'fileA').write_text('abcde\r\nfghlk\n\rmnopq', newline='\r\n')
    self.assertEqual((p / 'fileA').read_bytes(), b'abcde\r\r\nfghlk\r\n\rmnopq')
    os_linesep_byte = bytes(os.linesep, encoding='ascii')
    (p / 'fileA').write_text('abcde\nfghlk\n\rmnopq')
    self.assertEqual((p / 'fileA').read_bytes(), b'abcde' + os_linesep_byte + b'fghlk' + os_linesep_byte + b'\rmnopq')
