# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_robotparser.py
# case: BaseRequestRateTest_test_request_rate

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    parser = self.parser
    for url in self.good + self.bad:
        (agent, url) = self.get_agent_and_url(url)
        with self.subTest(url=url, agent=agent):
            self.assertEqual(parser.crawl_delay(agent), self.crawl_delay)
            parsed_request_rate = parser.request_rate(agent)
            self.assertEqual(parsed_request_rate, self.request_rate)
            if self.request_rate is not None:
                self.assertIsInstance(parsed_request_rate, urllib.robotparser.RequestRate)
                self.assertEqual(parsed_request_rate.requests, self.request_rate.requests)
                self.assertEqual(parsed_request_rate.seconds, self.request_rate.seconds)
