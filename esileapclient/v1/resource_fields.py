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


class Resource(object):
    """Resource class
    This class is used to manage the various fields that a resource (e.g.
    Offer) contains.  An individual field consists of a
    'field_id' (key) and a 'label' (value).  The caller only provides the
    'field_ids' when instantiating the object.
    Ordering of the 'field_ids' will be preserved as specified by the caller.
    It also provides the ability to exclude some of these fields when they are
    being used for sorting.
    """

    FIELDS = {
        'created_at': "Created At",
        'end_date': "End Date",
        'id': "ID",
        'project_id': "Project ID",
        'properties': "Properties",
        'resource_type': "Resource Type",
        'resource_uuid': "Resource UUID",
        'start_date': "Start Date",
        'status': "Status",
        'updated_at': "Updated At",
        'uuid': "UUID",
    }

    def __init__(self, field_ids):
        """Create a Resource object
        :param field_ids:  A list of strings that the Resource object will
                           contain.  Each string must match an existing key in
                           FIELDS.
        :raises: ValueError if sort_excluded or override_labels contains values
                 not in field_ids
        """

        self._fields = tuple(field_ids)
        self._labels = tuple([self.FIELDS[x] for x in field_ids])

    @property
    def fields(self):
        return self._fields

    @property
    def labels(self):
        return self._labels


OFFER_RESOURCE = Resource(

    ['created_at',
     'end_date',
     'id',
     'project_id',
     'properties',
     'resource_type',
     'resource_uuid',
     'start_date',
     'status',
     'updated_at',
     'uuid'])
