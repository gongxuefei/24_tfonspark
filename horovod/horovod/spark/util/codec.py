# Copyright 2018 Uber Technologies, Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

import base64
import cloudpickle


def loads_base64(encoded):
    decoded = base64.b64decode(encoded)
    return cloudpickle.loads(decoded)


def dumps_base64(obj):
    serialized = cloudpickle.dumps(obj)
    return base64.b64encode(serialized).decode('ascii')
