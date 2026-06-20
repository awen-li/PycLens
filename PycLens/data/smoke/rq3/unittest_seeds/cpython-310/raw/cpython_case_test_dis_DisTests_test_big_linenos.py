# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dis.py
# case: DisTests_test_big_linenos

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def func(count):
        namespace = {}
        func = 'def foo():\n ' + ''.join(['\n '] * count + ['spam\n'])
        exec(func, namespace)
        return namespace['foo']
    for i in range(1, 300):
        expected = _BIG_LINENO_FORMAT % (i + 2)
        self.do_disassembly_test(func(i), expected)
    for i in range(300, 1000, 10):
        expected = _BIG_LINENO_FORMAT % (i + 2)
        self.do_disassembly_test(func(i), expected)
    for i in range(1000, 5000, 10):
        expected = _BIG_LINENO_FORMAT2 % (i + 2)
        self.do_disassembly_test(func(i), expected)
    from test import dis_module
    self.do_disassembly_test(dis_module, dis_module_expected_results)
