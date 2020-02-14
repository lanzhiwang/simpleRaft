from .state import State

import sys
sys.path.insert(0, '../message')

from messages.request_vote import RequestVoteResponseMessage


class Voter(State):

    def __init__(self):
        self._last_vote = None

    def on_vote_request(self, message):
        """
        _name: 1,
        _state: <states.follower.Follower object at 0x103eeb470>,
        _log: [],
        _messageBoard: board: [],
        _neighbors: [<servers.server.Server object at 0x1040d6d68>],
        _total_nodes: 0,
        _commitIndex: 0,
        _currentTerm: 0,
        _lastApplied: 0,
        _lastLogIndex: 0,
        _lastLogTerm: None

        AppendEntries: 0, RequestVote: 1, RequestVoteResponse: 2, Response: 3, _timestamp: 1581673220,
        _sender: 0, _receiver: 1,
        _data: {'lastLogIndex': 0, 'lastLogTerm': 0, 'entries': []},
        _term: 2, _type: 1

        """
        if self._last_vote is None and message.data["lastLogIndex"] >= self._server._lastLogIndex:
            self._last_vote = message.sender
            self._send_vote_response_message(message)
        else:
            self._send_vote_response_message(message, yes=False)

        return self, None

    def _send_vote_response_message(self, msg, yes=True):
        voteResponse = RequestVoteResponseMessage(
            self._server._name,
            msg.sender,
            msg.term,
            {"response": yes})
        self._server.send_message_response(voteResponse)
