# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_subprocess.py
# case: ProcessTestCase_test_universal_newlines_communicate

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    p = subprocess.Popen([sys.executable, '-c', 'import sys,os;' + SETBINARY + 'buf = sys.stdout.buffer;buf.write(b"line2\\n");buf.flush();buf.write(b"line4\\n");buf.flush();buf.write(b"line5\\r\\n");buf.flush();buf.write(b"line6\\r");buf.flush();buf.write(b"\\nline7");buf.flush();buf.write(b"\\nline8");'], stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=1)
    self.addCleanup(p.stdout.close)
    self.addCleanup(p.stderr.close)
    (stdout, stderr) = p.communicate()
    self.assertEqual(stdout, 'line2\nline4\nline5\nline6\nline7\nline8')
