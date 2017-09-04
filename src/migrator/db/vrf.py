#
# Migrator tool for phpIPAM-NetBox
# migrator/db/vrf.py - database type for VRFs
#
# Copyright (c) 2017 Catalyst.net Ltd
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#


'''
Database type for VRFs.
'''


from migrator.db.object import Object


class VRF(Object):
    '''
    Database type for VRFs.
    '''


    def __init__(self,
                 vrf_id,
                 route_distinguisher,
                 enforce_unique=False,
                 name=None,
                 description=None,
                 tenant_id=None):
        '''
        VLAN group object constructor.
        '''

        self.__init__(vrf_id, name, description)

        self.route_distinguisher = route_distinguisher
        self.enforce_unique = enforce_unique

        self.tenant_id = tenant_id
