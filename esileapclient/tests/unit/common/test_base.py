#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import testtools
import copy

from esileapclient.common import base
from esileapclient.tests.unit import utils
from esileapclient.tests.unit.osc.fakes import FakeResource


TESTABLE_RESOURCE = {
    'uuid': '11111111-2222-3333-4444-555555555555',
    'attribute1': '1',
    'attribute2': '2',
}
TESTABLE_RESOURCE2 = {
    'uuid': '66666666-7777-8888-9999-000000000000',
    'attribute1': '3',
    'attribute2': '4',
}


CREATE_TESTABLE_RESOURCE = copy.deepcopy(TESTABLE_RESOURCE)
del CREATE_TESTABLE_RESOURCE['uuid']

INVALID_ATTRIBUTE_TESTABLE_RESOURCE = {
    'non-existent-attribute': 'blablabla',
    'attribute1': '1',
    'attribute2': '2',
}


fake_responses = {
    '/v1/testableresources':
    {
        'GET': (
            {},
            {'testableresources': [TESTABLE_RESOURCE, TESTABLE_RESOURCE2]},
        ),
    },

}


class TestableResource(base.Resource):
    def __repr__(self):
        return "<TestableResource %s>" % self._info


class TestableManager(base.Manager):
    resource_class = TestableResource
    _creation_attributes = ['attribute1', 'attribute2']
    _resource_name = 'testableresources'

    def _path(self, id=None):
        return ('/v1/testableresources/%s' % id if id
                else '/v1/testableresources')

    def list(self, os_esileap_api_version=None):
        return self._list(self._path(),
                          os_esileap_api_version=os_esileap_api_version)


class ManagerTestCase(testtools.TestCase):

    def setUp(self):
        super(ManagerTestCase, self).setUp()
        self.api = utils.FakeAPI(fake_responses)
        self.manager = TestableManager(self.api)

    def test_list(self):
        resources_list = self.manager.list()
        expected_calls = [
            ('GET', '/v1/testableresources', {}, None),
        ]
        self.assertEqual(expected_calls, self.api.calls)

        expected_resp = ({}, {'testableresources':
                              [TESTABLE_RESOURCE, TESTABLE_RESOURCE2]})
        expected_resources = [FakeResource(None, TESTABLE_RESOURCE),
                              FakeResource(None, TESTABLE_RESOURCE2)]

        self.assertEqual(expected_resp,
                         self.api.responses['/v1/testableresources']['GET'])
        assert (len(expected_resources) == 2)
        self.assertEqual(resources_list[0]._info, expected_resources[0]._info)
        self.assertEqual(resources_list[1]._info, expected_resources[1]._info)

    def test_list_microversion_override(self):
        resources_list = self.manager.list(os_esileap_api_version='1.10')
        expected_calls = [
            ('GET', '/v1/testableresources',
             {'X-OpenStack-ESI-Leap-API-Version': '1.10'}, None),
        ]
        self.assertEqual(expected_calls, self.api.calls)

        expected_resp = ({}, {'testableresources':
                              [TESTABLE_RESOURCE, TESTABLE_RESOURCE2]})
        expected_resources = [FakeResource(None, TESTABLE_RESOURCE),
                              FakeResource(None, TESTABLE_RESOURCE2)]

        self.assertEqual(expected_resp,
                         self.api.responses['/v1/testableresources']['GET'])
        assert (len(expected_resources) == 2)
        self.assertEqual(resources_list[0]._info, expected_resources[0]._info)
        self.assertEqual(resources_list[1]._info, expected_resources[1]._info)
