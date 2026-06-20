# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ssl.py
# case: ContextTests_test_num_tickest

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    self.assertEqual(ctx.num_tickets, 2)
    ctx.num_tickets = 1
    self.assertEqual(ctx.num_tickets, 1)
    ctx.num_tickets = 0
    self.assertEqual(ctx.num_tickets, 0)
    with self.assertRaises(ValueError):
        ctx.num_tickets = -1
    with self.assertRaises(TypeError):
        ctx.num_tickets = None
    ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    self.assertEqual(ctx.num_tickets, 2)
    with self.assertRaises(ValueError):
        ctx.num_tickets = 1
