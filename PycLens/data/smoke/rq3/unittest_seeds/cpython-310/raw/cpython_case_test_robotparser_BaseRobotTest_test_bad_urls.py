# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_robotparser.py
# case: BaseRobotTest_test_bad_urls

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for url in self.bad:
        (agent, url) = self.get_agent_and_url(url)
        with self.subTest(url=url, agent=agent):
            self.assertFalse(self.parser.can_fetch(agent, url))
