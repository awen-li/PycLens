# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dis.py
# case: DisTests_test_big_offsets

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def func(count):
        namespace = {}
        func = 'def foo(x):\n ' + ';'.join(['x = x + 1'] * count) + '\n return x'
        exec(func, namespace)
        return namespace['foo']

    def expected(count, w):
        s = ['           %*d LOAD_FAST                0 (x)\n           %*d LOAD_CONST               1 (1)\n           %*d BINARY_ADD\n           %*d STORE_FAST               0 (x)\n' % (w, 8 * i, w, 8 * i + 2, w, 8 * i + 4, w, 8 * i + 6) for i in range(count)]
        s += ['\n  3        %*d LOAD_FAST                0 (x)\n           %*d RETURN_VALUE\n' % (w, 8 * count, w, 8 * count + 2)]
        s[0] = '  2' + s[0][3:]
        return ''.join(s)
    for i in range(1, 5):
        self.do_disassembly_test(func(i), expected(i, 4))
    self.do_disassembly_test(func(1249), expected(1249, 4))
    self.do_disassembly_test(func(1250), expected(1250, 5))
