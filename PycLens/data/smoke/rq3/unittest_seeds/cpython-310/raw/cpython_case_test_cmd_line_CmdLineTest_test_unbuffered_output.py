# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_cmd_line.py
# case: CmdLineTest_test_unbuffered_output

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for stream in ('stdout', 'stderr'):
        code = "import os, sys; sys.%s.buffer.write(b'x'); os._exit(0)" % stream
        (rc, out, err) = assert_python_ok('-u', '-c', code)
        data = err if stream == 'stderr' else out
        self.assertEqual(data, b'x', 'binary %s not unbuffered' % stream)
        code = "import os, sys; sys.%s.write('x'); os._exit(0)" % stream
        (rc, out, err) = assert_python_ok('-u', '-c', code)
        data = err if stream == 'stderr' else out
        self.assertEqual(data, b'x', 'text %s not unbuffered' % stream)
