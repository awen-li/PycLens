# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_mailbox.py
# case: TestMailbox_test_dump_message

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for input in (email.message_from_string(_sample_message), _sample_message, io.BytesIO(_bytes_sample_message)):
        output = io.BytesIO()
        self._box._dump_message(input, output)
        self.assertEqual(output.getvalue(), _bytes_sample_message.replace(b'\n', os.linesep.encode()))
    output = io.BytesIO()
    self.assertRaises(TypeError, lambda : self._box._dump_message(None, output))
