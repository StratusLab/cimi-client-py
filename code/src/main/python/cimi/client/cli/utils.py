# -*- coding: utf-8 -*-
#
# Copyright (c) 2014, Centre National de la Recherche Scientifique (CNRS)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from cimi.client.api.cloud_entry_point import CloudEntryPoint

def get_cloud_entry_point(cfg):
    cimi_endpoint = cfg.get('cimi_cloud_entry_point')
    ssl_verify = cfg.get('ssl_verify')

    return CloudEntryPoint(cimi_endpoint, ssl_verify=ssl_verify)
