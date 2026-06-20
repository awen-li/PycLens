# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_utf8_mode.py
# case: UTF8ModeTests_test_io

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    code = textwrap.dedent('\n            import sys\n            filename = sys.argv[1]\n            with open(filename) as fp:\n                print(f"{fp.encoding}/{fp.errors}")\n        ')
    filename = __file__
    out = self.get_output('-c', code, filename, PYTHONUTF8='1')
    self.assertEqual(out, 'UTF-8/strict')
