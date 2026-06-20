# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_mailbox.py
# case: TestMessage_test_initialize_with_binary_file

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with open(self._path, 'wb+') as f:
        f.write(_bytes_sample_message)
        f.seek(0)
        msg = self._factory(f)
        self._post_initialize_hook(msg)
        self._check_sample(msg)
