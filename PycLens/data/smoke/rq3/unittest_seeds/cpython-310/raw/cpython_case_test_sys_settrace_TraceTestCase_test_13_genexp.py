# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sys_settrace.py
# case: TraceTestCase_test_13_genexp

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.run_test(generator_example)
    tracer = self.make_tracer()
    sys.settrace(tracer.traceWithGenexp)
    generator_example()
    sys.settrace(None)
    self.compare_events(generator_example.__code__.co_firstlineno, tracer.events, generator_example.events)
