# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_mailcap.py
# case: HelperFunctionTest_test_readmailcapfile

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with open(MAILCAPFILE, 'r') as mcf:
        with self.assertWarns(DeprecationWarning):
            d = mailcap.readmailcapfile(mcf)
    self.assertDictEqual(d, MAILCAPDICT_DEPRECATED)
