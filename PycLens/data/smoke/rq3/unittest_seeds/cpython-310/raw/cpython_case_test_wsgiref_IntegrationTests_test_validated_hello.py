# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_wsgiref.py
# case: IntegrationTests_test_validated_hello

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (out, err) = run_amock(validator(hello_app))
    self.check_hello(out, has_length=False)
