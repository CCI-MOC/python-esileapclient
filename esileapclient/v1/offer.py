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


import logging

from esileapclient.common import base

LOG = logging.getLogger(__name__)


class Offer(base.Resource):
    def __repr__(self):
        return "<Offer %s>" % self._info


class OfferManager(base.Manager):
    resource_class = Offer
    _creation_attributes = ['id', 'uuid', 'project_id', 'resource_type',
                            'resource_uuid', 'start_date', 'end_date',
                            'status', 'properties']

    _resource_name = 'offers'

    def list(self, os_esileap_api_version=None):
        """Retrieve a list of offers.
        :returns: A list of offers.
        """

        path = ''
        offers = self._list(self._path(path),
                            os_esileap_api_version=os_esileap_api_version)

        return offers
