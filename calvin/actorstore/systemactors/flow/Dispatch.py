# -*- coding: utf-8 -*-

# Copyright (c) 2015 Ericsson AB
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

from calvin.actor.actor import Actor, condition


class Dispatch(Actor):
    """
    Dispatch tokens to all connected outports, aiming at keeping all queues equal, i.e. the token will end up in the smallest queue at all times.
    Inputs:
      token : incoming token stream
    Outputs:
        token(routing="balanced") : outgoing token stream
    """

    def init(self):
        pass

    @condition(['token'], ['token'])
    def dispatch(self, data):
        return (data, )

    action_priority = (dispatch,)
