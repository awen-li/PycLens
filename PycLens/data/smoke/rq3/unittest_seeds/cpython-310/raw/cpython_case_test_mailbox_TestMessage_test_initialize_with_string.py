# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_mailbox.py
# case: TestMessage_test_initialize_with_string

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    msg = self._factory(_sample_message)
    self._post_initialize_hook(msg)
    self._check_sample(msg)
