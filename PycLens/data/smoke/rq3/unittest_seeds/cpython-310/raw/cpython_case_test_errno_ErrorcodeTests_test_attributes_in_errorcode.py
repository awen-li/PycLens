# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_errno.py
# case: ErrorcodeTests_test_attributes_in_errorcode

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for attribute in errno.__dict__.keys():
        if attribute.isupper():
            self.assertIn(getattr(errno, attribute), errno.errorcode, 'no %s attr in errno.errorcode' % attribute)
