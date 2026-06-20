# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_subprocess.py
# case: ProcessTestCase_test_communicate_errors

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for (errors, expected) in [('ignore', ''), ('replace', '��'), ('surrogateescape', '\udc80\udc80'), ('backslashreplace', '\\x80\\x80')]:
        code = "import sys; sys.stdout.buffer.write(b'[\\x80\\x80]')"
        args = [sys.executable, '-c', code]
        popen = subprocess.Popen(args, stdin=subprocess.PIPE, stdout=subprocess.PIPE, encoding='utf-8', errors=errors)
        (stdout, stderr) = popen.communicate(input='')
        self.assertEqual(stdout, '[{}]'.format(expected))
