# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_cmd_line.py
# case: CmdLineTest_test_int_max_str_digits

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    code = 'import sys; print(sys.flags.int_max_str_digits, sys.get_int_max_str_digits())'
    assert_python_failure('-X', 'int_max_str_digits', '-c', code)
    assert_python_failure('-X', 'int_max_str_digits=foo', '-c', code)
    assert_python_failure('-X', 'int_max_str_digits=100', '-c', code)
    assert_python_failure('-X', 'int_max_str_digits', '-c', code, PYTHONINTMAXSTRDIGITS='4000')
    assert_python_failure('-c', code, PYTHONINTMAXSTRDIGITS='foo')
    assert_python_failure('-c', code, PYTHONINTMAXSTRDIGITS='100')

    def res2int(res):
        out = res.out.strip().decode('utf-8')
        return tuple((int(i) for i in out.split()))
    res = assert_python_ok('-c', code)
    self.assertEqual(res2int(res), (-1, sys.get_int_max_str_digits()))
    res = assert_python_ok('-X', 'int_max_str_digits=0', '-c', code)
    self.assertEqual(res2int(res), (0, 0))
    res = assert_python_ok('-X', 'int_max_str_digits=4000', '-c', code)
    self.assertEqual(res2int(res), (4000, 4000))
    res = assert_python_ok('-X', 'int_max_str_digits=100000', '-c', code)
    self.assertEqual(res2int(res), (100000, 100000))
    res = assert_python_ok('-c', code, PYTHONINTMAXSTRDIGITS='0')
    self.assertEqual(res2int(res), (0, 0))
    res = assert_python_ok('-c', code, PYTHONINTMAXSTRDIGITS='4000')
    self.assertEqual(res2int(res), (4000, 4000))
    res = assert_python_ok('-X', 'int_max_str_digits=6000', '-c', code, PYTHONINTMAXSTRDIGITS='4000')
    self.assertEqual(res2int(res), (6000, 6000))
