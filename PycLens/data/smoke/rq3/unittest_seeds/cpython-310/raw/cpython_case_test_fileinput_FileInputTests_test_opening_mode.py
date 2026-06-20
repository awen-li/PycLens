# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_fileinput.py
# case: FileInputTests_test_opening_mode

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    try:
        fi = FileInput(mode='w', encoding='utf-8')
        self.fail('FileInput should reject invalid mode argument')
    except ValueError:
        pass
    t1 = self.writeTmp(b'A\nB\r\nC\rD', mode='wb')
    with warnings_helper.check_warnings(('', DeprecationWarning)):
        fi = FileInput(files=t1, mode='U', encoding='utf-8')
    with warnings_helper.check_warnings(('', DeprecationWarning)):
        lines = list(fi)
    self.assertEqual(lines, ['A\n', 'B\n', 'C\n', 'D'])
