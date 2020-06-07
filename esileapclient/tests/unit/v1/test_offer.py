import testtools

from esileapclient.tests.unit import utils
from esileapclient.tests.unit.osc.fakes import FakeResource

import esileapclient.v1.offer


OFFER = {
    'created_at': '2000-00-00T13',
    'end_date': "3000-00-00T13",
    'id': '200',
    'project_id': "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
    'properties': {},
    'resource_type': 'dummy_node',
    'resource_uuid': "1718",
    'start_date': "2010",
    'status': "fake_status",
    'updated_at': None,
    'uuid': "fac28c4b-f996-4c72-b0b4-81f1bcf3691c"
}

OFFER2 = {
    'created_at': '2000-00-00T13',
    'end_date': "3000-00-00T13",
    'id': '300',
    'project_id': "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
    'properties': {},
    'resource_type': 'dummy_node',
    'resource_uuid': "1718",
    'start_date': "2010",
    'status': "fake_status",
    'updated_at': None,
    'uuid': "0fad68ba-3be1-4798-aaea-baee1441cf03"
}


fake_responses = {
    '/v1/offers':
    {
        'GET': (
            {},
            {'offers': [OFFER, OFFER2]},
        ),

        'POST': (
            {},
            {'offers': OFFER},
        ),
    },

}


class OfferManagerTest(testtools.TestCase):

    def setUp(self):
        super(OfferManagerTest, self).setUp()
        self.api = utils.FakeAPI(fake_responses)
        self.manager = esileapclient.v1.offer.OfferManager(self.api)

    def test_offers_list(self):
        resources_list = self.manager.list()
        expected_call = [
            ('GET', '/v1/offers', {}, None),
        ]
        self.assertEqual(expected_call, self.api.calls)

        expected_resp = ({}, {'offers': [OFFER, OFFER2]})
        expected_resources = [FakeResource(None, OFFER),
                              FakeResource(None, OFFER2)]

        self.assertEqual(expected_resp,
                         self.api.responses['/v1/offers']['GET'])
        assert (len(expected_resources) == 2)
        self.assertEqual(resources_list[0]._info, expected_resources[0]._info)
        self.assertEqual(resources_list[1]._info, expected_resources[1]._info)
