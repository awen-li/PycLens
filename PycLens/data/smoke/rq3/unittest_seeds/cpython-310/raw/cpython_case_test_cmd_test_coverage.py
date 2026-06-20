# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_cmd.py
# case: test_coverage

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    trace = support.import_module('trace')
    tracer = trace.Trace(ignoredirs=[sys.base_prefix, sys.base_exec_prefix], trace=0, count=1)
    tracer.run('import importlib; importlib.reload(cmd); test_main()')
    r = tracer.results()
    print('Writing coverage results...')
    r.write_results(show_missing=True, summary=True, coverdir=coverdir)
