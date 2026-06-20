# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pydoc.py
# case: TestDescriptions_test_module

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    from test import pydocfodder
    doc = pydoc.render_doc(pydocfodder)
    self.assertIn('pydocfodder', doc)
