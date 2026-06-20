# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_imaplib.py
# case: ThreadedNetworkedTests_test_bracket_flags

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class BracketFlagHandler(SimpleIMAPHandler):

        def handle(self):
            self.flags = ['Answered', 'Flagged', 'Deleted', 'Seen', 'Draft']
            super().handle()

        def cmd_AUTHENTICATE(self, tag, args):
            self._send_textline('+')
            self.server.response = (yield)
            self._send_tagged(tag, 'OK', 'FAKEAUTH successful')

        def cmd_SELECT(self, tag, args):
            flag_msg = ' \\'.join(self.flags)
            self._send_line(('* FLAGS (%s)' % flag_msg).encode('ascii'))
            self._send_line(b'* 2 EXISTS')
            self._send_line(b'* 0 RECENT')
            msg = '* OK [PERMANENTFLAGS %s \\*)] Flags permitted.' % flag_msg
            self._send_line(msg.encode('ascii'))
            self._send_tagged(tag, 'OK', '[READ-WRITE] SELECT completed.')

        def cmd_STORE(self, tag, args):
            new_flags = args[2].strip('(').strip(')').split()
            self.flags.extend(new_flags)
            flags_msg = '(FLAGS (%s))' % ' \\'.join(self.flags)
            msg = '* %s FETCH %s' % (args[0], flags_msg)
            self._send_line(msg.encode('ascii'))
            self._send_tagged(tag, 'OK', 'STORE completed.')
    with self.reaped_pair(BracketFlagHandler) as (server, client):
        (code, data) = client.authenticate('MYAUTH', lambda x: b'fake')
        self.assertEqual(code, 'OK')
        self.assertEqual(server.response, b'ZmFrZQ==\r\n')
        client.select('test')
        (typ, [data]) = client.store(b'1', '+FLAGS', '[test]')
        self.assertIn(b'[test]', data)
        client.select('test')
        (typ, [data]) = client.response('PERMANENTFLAGS')
        self.assertIn(b'[test]', data)
