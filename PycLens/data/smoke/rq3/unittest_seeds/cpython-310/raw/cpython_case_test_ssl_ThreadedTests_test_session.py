# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ssl.py
# case: ThreadedTests_test_session

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (client_context, server_context, hostname) = testing_context()
    client_context.maximum_version = ssl.TLSVersion.TLSv1_2
    stats = server_params_test(client_context, server_context, sni_name=hostname)
    session = stats['session']
    self.assertTrue(session.id)
    self.assertGreater(session.time, 0)
    self.assertGreater(session.timeout, 0)
    self.assertTrue(session.has_ticket)
    self.assertGreater(session.ticket_lifetime_hint, 0)
    self.assertFalse(stats['session_reused'])
    sess_stat = server_context.session_stats()
    self.assertEqual(sess_stat['accept'], 1)
    self.assertEqual(sess_stat['hits'], 0)
    stats = server_params_test(client_context, server_context, session=session, sni_name=hostname)
    sess_stat = server_context.session_stats()
    self.assertEqual(sess_stat['accept'], 2)
    self.assertEqual(sess_stat['hits'], 1)
    self.assertTrue(stats['session_reused'])
    session2 = stats['session']
    self.assertEqual(session2.id, session.id)
    self.assertEqual(session2, session)
    self.assertIsNot(session2, session)
    self.assertGreaterEqual(session2.time, session.time)
    self.assertGreaterEqual(session2.timeout, session.timeout)
    stats = server_params_test(client_context, server_context, sni_name=hostname)
    self.assertFalse(stats['session_reused'])
    session3 = stats['session']
    self.assertNotEqual(session3.id, session.id)
    self.assertNotEqual(session3, session)
    sess_stat = server_context.session_stats()
    self.assertEqual(sess_stat['accept'], 3)
    self.assertEqual(sess_stat['hits'], 1)
    stats = server_params_test(client_context, server_context, session=session, sni_name=hostname)
    self.assertTrue(stats['session_reused'])
    session4 = stats['session']
    self.assertEqual(session4.id, session.id)
    self.assertEqual(session4, session)
    self.assertGreaterEqual(session4.time, session.time)
    self.assertGreaterEqual(session4.timeout, session.timeout)
    sess_stat = server_context.session_stats()
    self.assertEqual(sess_stat['accept'], 4)
    self.assertEqual(sess_stat['hits'], 2)
