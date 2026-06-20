# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_imaplib.py
# case: NewIMAPTestsMixin_test_lsub

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class LsubCmd(SimpleIMAPHandler):

        def cmd_LSUB(self, tag, args):
            self._send_textline('* LSUB () "." directoryA')
            return self._send_tagged(tag, 'OK', 'LSUB completed')
    (client, _) = self._setup(LsubCmd)
    client.login('user', 'pass')
    (typ, data) = client.lsub()
    self.assertEqual(typ, 'OK')
    self.assertEqual(data[0], b'() "." directoryA')
