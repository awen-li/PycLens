# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_subprocess.py
# case: ProcessTestCase_test_universal_newlines_communicate_stdin_stdout_stderr

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    p = subprocess.Popen([sys.executable, '-c', 'import sys,os;' + SETBINARY + textwrap.dedent('\n                               s = sys.stdin.buffer.readline()\n                               sys.stdout.buffer.write(s)\n                               sys.stdout.buffer.write(b"line2\\r")\n                               sys.stderr.buffer.write(b"eline2\\n")\n                               s = sys.stdin.buffer.read()\n                               sys.stdout.buffer.write(s)\n                               sys.stdout.buffer.write(b"line4\\n")\n                               sys.stdout.buffer.write(b"line5\\r\\n")\n                               sys.stderr.buffer.write(b"eline6\\r")\n                               sys.stderr.buffer.write(b"eline7\\r\\nz")\n                              ')], stdin=subprocess.PIPE, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
    self.addCleanup(p.stdout.close)
    self.addCleanup(p.stderr.close)
    (stdout, stderr) = p.communicate('line1\nline3\n')
    self.assertEqual(p.returncode, 0)
    self.assertEqual('line1\nline2\nline3\nline4\nline5\n', stdout)
    self.assertTrue(stderr.startswith('eline2\neline6\neline7\n'))
