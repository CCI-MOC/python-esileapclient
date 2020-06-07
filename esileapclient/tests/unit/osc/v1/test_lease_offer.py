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

import copy
import json

from esileapclient.osc.v1 import lease_offer
from esileapclient.tests.unit.osc.v1 import fakes as lease_fakes


class TestLeaseOffer(lease_fakes.TestLease):

    def setUp(self):
        super(TestLeaseOffer, self).setUp()

        self.lease_mock = self.app.client_manager.lease
        self.lease_mock.reset_mock()


class TestLeaseOfferList(TestLeaseOffer):
    def setUp(self):
        super(TestLeaseOfferList, self).setUp()

        self.lease_mock.offer.list.return_value = [
            lease_fakes.FakeLeaseResource(
                None,
                copy.deepcopy(lease_fakes.OFFER))
        ]
        self.cmd = lease_offer.ListLeaseOffer(self.app, None)

    def test_lease_offer_list(self):
        arglist = []
        verifylist = []

        parsed_args = self.check_parser(self.cmd, arglist, verifylist)
        columns, data = self.cmd.take_action(parsed_args)

        self.lease_mock.offer.list.assert_called_with()

        collist = (
            "Created At",
            "End Date",
            "ID",
            "Project ID",
            "Properties",
            "Resource Type",
            "Resource UUID",
            "Start Date",
            "Status",
            "Updated At",
            "UUID",
        )

        self.assertEqual(collist, columns)

        datalist = ((lease_fakes.lease_created_at,
                     lease_fakes.lease_end_date,
                     lease_fakes.lease_id,
                     lease_fakes.lease_project_id,
                     json.loads(lease_fakes.lease_properties),
                     lease_fakes.lease_resource_type,
                     lease_fakes.lease_resource_uuid,
                     lease_fakes.lease_start_date,
                     lease_fakes.lease_status,
                     lease_fakes.lease_updated_at,
                     lease_fakes.lease_uuid
                     ),)
        self.assertEqual(datalist, tuple(data))
