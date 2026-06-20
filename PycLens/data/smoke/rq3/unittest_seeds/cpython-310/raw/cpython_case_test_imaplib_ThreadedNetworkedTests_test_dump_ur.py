# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_imaplib.py
# case: ThreadedNetworkedTests_test_dump_ur

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    untagged_resp_dict = {'READ-WRITE': [b'']}
    with self.reaped_server(SimpleIMAPHandler) as server:
        with self.imap_class(*server.server_address) as imap:
            with mock.patch.object(imap, '_mesg') as mock_mesg:
                imap._dump_ur(untagged_resp_dict)
                mock_mesg.assert_called_with("untagged responses dump:READ-WRITE: [b'']")
