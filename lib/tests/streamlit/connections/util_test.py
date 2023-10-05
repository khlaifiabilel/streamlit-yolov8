# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
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

import unittest
from unittest.mock import MagicMock, patch

from streamlit.connections.util import extract_from_dict, running_in_sis


class ConnectionUtilTest(unittest.TestCase):
    def test_extract_from_dict(self):
        d = {"k1": "v1", "k2": "v2", "k3": "v3", "k4": "v4"}

        extracted = extract_from_dict(
            ["k1", "k2", "nonexistent_key"],
            d,
        )

        assert extracted == {"k1": "v1", "k2": "v2"}
        assert d == {"k3": "v3", "k4": "v4"}

    @patch("snowflake.connector.connection", MagicMock())
    def test_not_running_in_sis(self):
        assert not running_in_sis()

    @patch(
        "snowflake.connector.connection",
    )
    def test_running_in_sis(self, patched_connection):
        delattr(patched_connection, "SnowflakeConnection")
        assert running_in_sis()
