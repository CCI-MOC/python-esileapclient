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

"""
Base utilities to build API operation managers and objects on top of.
"""

import logging
import abc
import six

from esileapclient.common.apiclient import base


LOG = logging.getLogger(__name__)


@six.add_metaclass(abc.ABCMeta)
class Manager(object):
    """Provides  CRUD operations with a particular API."""

    @property
    @abc.abstractmethod
    def resource_class(self):
        """The resource class
        """

    @property
    @abc.abstractmethod
    def _resource_name(self):
        """The resource name.
        """

    @property
    @abc.abstractmethod
    def _creation_attributes(self):
        """A list of required creation attributes for a resource type.
        """

    def __init__(self, api):
        self.api = api

    def _path(self, resource_id=None):
        """Returns a request path for a given resource identifier.
        :param resource_id: Identifier of the resource to generate the request
                            path.
        """

        return ('/v1/%s/%s' % (self._resource_name, resource_id)
                if resource_id else '/v1/%s' % self._resource_name)

    def _format_body_data(self, body):

        data = body

        if not isinstance(data, list):
            data = [data]

        return data

    def _list(self, url, obj_class=None, os_esileap_api_version=None):
        if obj_class is None:
            obj_class = self.resource_class

        kwargs = {}

        if os_esileap_api_version is not None:
            kwargs['headers'] = {'X-OpenStack-ESI-Leap-API-Version':
                                 os_esileap_api_version}

        _, body = self.api.json_request('GET', url, **kwargs)
        body = body[self._resource_name]
        data = self._format_body_data(body)

        return [obj_class(self, res) for res in data if res]


class Resource(base.Resource):
    """Represents a particular instance of an object (tenant, user, etc).
    This is pretty much just a bag for attributes.
    """
