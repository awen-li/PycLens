# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_subprocess.py
# case: ProcessTestCase_test_universal_newlines_and_text

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    args = [sys.executable, '-c', 'import sys,os;' + SETBINARY + 'buf = sys.stdout.buffer;buf.write(sys.stdin.readline().encode());buf.flush();buf.write(b"line2\\n");buf.flush();buf.write(sys.stdin.read().encode());buf.flush();buf.write(b"line4\\n");buf.flush();buf.write(b"line5\\r\\n");buf.flush();buf.write(b"line6\\r");buf.flush();buf.write(b"\\nline7");buf.flush();buf.write(b"\\nline8");']
    for extra_kwarg in ('universal_newlines', 'text'):
        p = subprocess.Popen(args, **{'stdin': subprocess.PIPE, 'stdout': subprocess.PIPE, extra_kwarg: True})
        with p:
            p.stdin.write('line1\n')
            p.stdin.flush()
            self.assertEqual(p.stdout.readline(), 'line1\n')
            p.stdin.write('line3\n')
            p.stdin.close()
            self.addCleanup(p.stdout.close)
            self.assertEqual(p.stdout.readline(), 'line2\n')
            self.assertEqual(p.stdout.read(6), 'line3\n')
            self.assertEqual(p.stdout.read(), 'line4\nline5\nline6\nline7\nline8')
