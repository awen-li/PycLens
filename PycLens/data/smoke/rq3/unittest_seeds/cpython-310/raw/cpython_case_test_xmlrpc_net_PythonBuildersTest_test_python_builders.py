# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xmlrpc_net.py
# case: PythonBuildersTest_test_python_builders

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    server = xmlrpclib.ServerProxy('http://buildbot.python.org/all/xmlrpc/')
    try:
        builders = server.getAllBuilders()
    except OSError as e:
        self.skipTest('network error: %s' % e)
    self.addCleanup(lambda : server('close')())
    self.assertIsInstance(builders, collections.abc.Sequence)
    self.assertTrue([x for x in builders if '3.x' in x], builders)
