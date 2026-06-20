# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codecs.py
# case: UTF7Test_test_ascii

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    set_d = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'(),-./:?"
    self.assertEqual(set_d.encode(self.encoding), set_d.encode('ascii'))
    self.assertEqual(set_d.encode('ascii').decode(self.encoding), set_d)
    set_o = ' !"#$%&*;<=>@[]^_`{|}'
    self.assertEqual(set_o.encode(self.encoding), set_o.encode('ascii'))
    self.assertEqual(set_o.encode('ascii').decode(self.encoding), set_o)
    self.assertEqual('a+b'.encode(self.encoding), b'a+-b')
    self.assertEqual(b'a+-b'.decode(self.encoding), 'a+b')
    ws = ' \t\n\r'
    self.assertEqual(ws.encode(self.encoding), ws.encode('ascii'))
    self.assertEqual(ws.encode('ascii').decode(self.encoding), ws)
    other_ascii = ''.join(sorted(set(bytes(range(128)).decode()) - set(set_d + set_o + '+' + ws)))
    self.assertEqual(other_ascii.encode(self.encoding), b'+AAAAAQACAAMABAAFAAYABwAIAAsADAAOAA8AEAARABIAEwAUABUAFgAXABgAGQAaABsAHAAdAB4AHwBcAH4Afw-')
