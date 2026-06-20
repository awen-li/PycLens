# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sys_settrace.py
# case: JumpTestCase_test_jump_to_firstlineno

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    code = compile("\n# Comments don't count.\noutput.append(2)  # firstlineno is here.\noutput.append(3)\noutput.append(4)\n", '<fake module>', 'exec')

    class fake_function:
        __code__ = code
    tracer = JumpTracer(fake_function, 4, 1)
    sys.settrace(tracer.trace)
    namespace = {'output': []}
    exec(code, namespace)
    sys.settrace(None)
    self.compare_jump_output([2, 3, 2, 3, 4], namespace['output'])
