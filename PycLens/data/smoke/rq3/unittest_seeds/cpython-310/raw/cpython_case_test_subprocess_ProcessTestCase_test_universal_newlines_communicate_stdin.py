# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_subprocess.py
# case: ProcessTestCase_test_universal_newlines_communicate_stdin

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    p = subprocess.Popen([sys.executable, '-c', 'import sys,os;' + SETBINARY + textwrap.dedent('\n                               s = sys.stdin.readline()\n                               assert s == "line1\\n", repr(s)\n                               s = sys.stdin.read()\n                               assert s == "line3\\n", repr(s)\n                              ')], stdin=subprocess.PIPE, universal_newlines=1)
    (stdout, stderr) = p.communicate('line1\nline3\n')
    self.assertEqual(p.returncode, 0)
