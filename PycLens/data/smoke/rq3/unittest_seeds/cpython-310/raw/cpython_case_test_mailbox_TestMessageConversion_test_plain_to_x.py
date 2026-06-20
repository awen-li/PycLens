# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_mailbox.py
# case: TestMessageConversion_test_plain_to_x

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for class_ in self.all_mailbox_types:
        msg_plain = mailbox.Message(_sample_message)
        msg = class_(msg_plain)
        self._check_sample(msg)
