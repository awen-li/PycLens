# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_lltrace.py
# case: TestLLTrace_test_lltrace

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    stdout = self.run_code('\n            def dont_trace_1():\n                a = "a"\n                a = 10 * a\n            def trace_me():\n                for i in range(3):\n                    +i\n            def dont_trace_2():\n                x = 42\n                y = -x\n            dont_trace_1()\n            __ltrace__ = 1\n            trace_me()\n            del __ltrace__\n            dont_trace_2()\n        ')
    self.check_op_in('GET_ITER', stdout)
    self.check_op_in('FOR_ITER', stdout)
    self.check_op_in('UNARY_POSITIVE', stdout)
    self.check_op_in('POP_TOP', stdout)
    self.check_op_not_in('BINARY_MULTIPLY', stdout)
    self.check_op_not_in('UNARY_NEGATIVE', stdout)
