# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_exceptions.py
# case: ExceptionTests_test_memory_error_subclasses

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class TestException(MemoryError):
        pass
    try:
        raise MemoryError
    except MemoryError as exc:
        inst = exc
    try:
        raise TestException
    except Exception:
        pass
    for _ in range(10):
        try:
            raise MemoryError
        except MemoryError as exc:
            pass
        gc_collect()
