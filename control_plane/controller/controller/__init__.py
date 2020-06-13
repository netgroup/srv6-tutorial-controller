#!/usr/bin/python

##########################################################################
# Copyright (C) 2020 Carmine Scarpitta - (Consortium GARR and University of Rome "Tor Vergata")
# www.garr.it - www.uniroma2.it/netgroup
#
#
# Licensed under the Apache License, Version 2.0 (the 'License');
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Controller
#
# @author Carmine Scarpitta <carmine.scarpitta@uniroma2.it>
#


##
#
# This module contains all public symbols from the library
#

"""Implementation of Controller"""

from controller.utils import get_grpc_session
from controller.srv6_utils import (handle_srv6_path,
                                   handle_srv6_behavior)
from controller.arangodb_utils import (
    extract_topo_from_isis,
    load_topo_on_arango,
    extract_topo_from_isis_and_load_on_arango)
