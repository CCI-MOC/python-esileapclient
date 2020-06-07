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

import mock
import json

from osc_lib.tests import utils

from esileapclient.tests.unit.osc import fakes


lease_created_at = "2000-00-00T13"
lease_end_date = "3000-00-00T13"
lease_id = "130"
lease_project_id = "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
lease_properties = "{}"
lease_resource_type = "dummy_node"
lease_resource_uuid = "1213123123"
lease_start_date = "2010"
lease_status = "fake_status"
lease_updated_at = None
lease_uuid = "9999999"

OFFER = {
    'created_at': lease_created_at,
    'end_date': lease_end_date,
    'id': lease_id,
    'project_id': lease_project_id,
    'properties': json.loads(lease_properties),
    'resource_type': lease_resource_type,
    'resource_uuid': lease_resource_uuid,
    'start_date': lease_start_date,
    'status': lease_status,
    'updated_at': lease_updated_at,
    'uuid': lease_uuid
}


class TestLease(utils.TestCommand):

    def setUp(self):
        super(TestLease, self).setUp()

        self.app.client_manager.auth_ref = mock.Mock(auth_token="TOKEN")
        self.app.client_manager.lease = mock.Mock()


class FakeLeaseResource(fakes.FakeResource):

    def get_keys(self):
        return {'property': 'value'}
