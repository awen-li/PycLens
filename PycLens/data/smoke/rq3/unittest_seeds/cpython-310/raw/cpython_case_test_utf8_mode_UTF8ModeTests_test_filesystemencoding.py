# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_utf8_mode.py
# case: UTF8ModeTests_test_filesystemencoding

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    code = textwrap.dedent('\n            import sys\n            print("{}/{}".format(sys.getfilesystemencoding(),\n                                 sys.getfilesystemencodeerrors()))\n        ')
    if MS_WINDOWS:
        expected = 'utf-8/surrogatepass'
    else:
        expected = 'utf-8/surrogateescape'
    out = self.get_output('-X', 'utf8', '-c', code)
    self.assertEqual(out, expected)
    if MS_WINDOWS:
        out = self.get_output('-X', 'utf8', '-c', code, PYTHONUTF8='strict', PYTHONLEGACYWINDOWSFSENCODING='1')
        self.assertEqual(out, 'mbcs/replace')
