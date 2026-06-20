# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_mailbox.py
# case: TestMessageConversion_test_x_to_plain

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for class_ in self.all_mailbox_types:
        msg = class_(_sample_message)
        msg_plain = mailbox.Message(msg)
        self._check_sample(msg_plain)
