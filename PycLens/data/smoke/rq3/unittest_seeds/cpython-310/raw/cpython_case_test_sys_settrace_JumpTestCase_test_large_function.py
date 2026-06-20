# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sys_settrace.py
# case: JumpTestCase_test_large_function

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    d = {}
    exec("def f(output):        # line 0\n            x = 0                     # line 1\n            y = 1                     # line 2\n            '''                       # line 3\n            %s                        # lines 4-1004\n            '''                       # line 1005\n            x += 1                    # line 1006\n            output.append(x)          # line 1007\n            return" % ('\n' * 1000,), d)
    f = d['f']
    self.run_test(f, 2, 1007, [0])
