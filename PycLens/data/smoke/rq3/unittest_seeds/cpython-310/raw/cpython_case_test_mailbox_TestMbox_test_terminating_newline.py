# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_mailbox.py
# case: TestMbox_test_terminating_newline

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    message = email.message.Message()
    message['From'] = 'john@example.com'
    message.set_payload('No newline at the end')
    i = self._box.add(message)
    message = self._box.get(i)
    self.assertEqual(message.get_payload(), 'No newline at the end\n')
