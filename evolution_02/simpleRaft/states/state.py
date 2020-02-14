import time
import random

import sys
sys.path.insert(0, '../message')

from messages.base import BaseMessage
from messages.response import ResponseMessage


class State(object):

    def set_server(self, server):
        self._server = server

    def on_message(self, message):
        """
        AppendEntries: 0, RequestVote: 1, RequestVoteResponse: 2, Response: 3,
        _timestamp: 1581652434, _sender: 0, _receiver: 1, _data: {}, _term: 2

        _name: 1,
        _state: <states.follower.Follower object at 0x10ef77048>,
        _log: [],
        _messageBoard: board: [],
        _neighbors: [<servers.server.Server object at 0x10ef71cf8>],
        _total_nodes: 0,
        _commitIndex: 0,
        _currentTerm: 0,
        _lastApplied: 0,
        _lastLogIndex: 0,
        _lastLogTerm: None

        """

        _type = message.type

        if message.term > self._server._currentTerm:
            self._server._currentTerm = message.term
        elif message.term < self._server._currentTerm:
            self._send_response_message(message, yes=False)
            return self, None

        if _type == BaseMessage.AppendEntries:
            return self.on_append_entries(message)

        elif _type == BaseMessage.RequestVote:
            return self.on_vote_request(message)

        elif _type == BaseMessage.RequestVoteResponse:
            return self.on_vote_received(message)

        elif _type == BaseMessage.Response:
            return self.on_response_received(message)

    def _nextTimeout(self):
        self._currentTime = time.time()
        return self._currentTime + random.randrange(self._timeout,
                                                    2 * self._timeout)

    def _send_response_message(self, msg, yes=True):
        """
        AppendEntries: 0, RequestVote: 1, RequestVoteResponse: 2, Response: 3,
        _timestamp: 1581652434, _sender: 0, _receiver: 1, _data: {}, _term: 2

        _name: 1,
        _state: <states.follower.Follower object at 0x10ef77048>,
        _log: [],
        _messageBoard: board: [],
        _neighbors: [<servers.server.Server object at 0x10ef71cf8>],
        _total_nodes: 0,
        _commitIndex: 0,
        _currentTerm: 0,
        _lastApplied: 0,
        _lastLogIndex: 0,
        _lastLogTerm: None

        """

        response = ResponseMessage(
            self._server._name,
            msg.sender,
            msg.term,
            {
            "response": yes,
            "currentTerm": self._server._currentTerm
            }
        )
        # print(response)
        self._server.send_message_response(response)

    def on_leader_timeout(self, message):
        pass

    def on_vote_request(self, message):
        pass

    def on_vote_received(self, message):
        pass

    def on_append_entries(self, message):
        pass

    def on_response_received(self, message):
        pass

    def on_client_command(self, message):
        pass
