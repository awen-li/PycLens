# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_subprocess.py
# case: ProcessTestCase_test_universal_newlines_communicate_encodings

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for encoding in ['utf-16', 'utf-32-be']:
        code = "import sys; sys.stdout.buffer.write('1\\r\\n2\\r3\\n4'.encode('%s'))" % encoding
        args = [sys.executable, '-c', code]
        popen = subprocess.Popen(args, stdin=subprocess.PIPE, stdout=subprocess.PIPE, encoding=encoding)
        (stdout, stderr) = popen.communicate(input='')
        self.assertEqual(stdout, '1\n2\n3\n4')
