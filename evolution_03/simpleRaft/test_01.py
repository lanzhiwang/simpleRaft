import unittest

from boards.memory_board import MemoryBoard
from messages.append_entries import AppendEntriesMessage
from messages.request_vote import RequestVoteMessage
from servers.server import Server
from states.follower import Follower
from states.candidate import Candidate
from states.leader import Leader


board = MemoryBoard()
state = Follower()
oserver = Server(0, state, [], board, [])
# print(oserver)
"""
_name: 0, 
_state: Follower ** _timeout: 500, _timeoutTime: 1581685132.670627, _last_vote: None, 
_log: [], 
_messageBoard: board: [], 
_neighbors: [], 
_total_nodes: 0, 
_commitIndex: 0, 
_currentTerm: 0, 
_lastApplied: 0, 
_lastLogIndex: 0, 
_lastLogTerm: None
"""

board = MemoryBoard()
state = Candidate()  # 候选人
# print(state)  # Candidate ** _last_vote: None, _votes: None

server = Server(1, state, [], board, [oserver])
# print(server)
"""
_name: 1, 
_state: Candidate ** _last_vote: 1, _votes: {}, 
_log: [], 
_messageBoard: board: [], 
_neighbors: [<servers.server.Server object at 0x10550b908>], 
_total_nodes: 0, 
_commitIndex: 0, 
_currentTerm: 1, 
_lastApplied: 0, 
_lastLogIndex: 0, 
_lastLogTerm: None
"""

oserver._neighbors.append(server)
# print(oserver)

"""
_name: 0, 
_state: Follower ** _timeout: 500, _timeoutTime: 1581685712.0402, _last_vote: None, 
_log: [], 
_messageBoard: board: [<messages.request_vote.RequestVoteMessage object at 0x105510198>], 
_neighbors: [<servers.server.Server object at 0x1055104a8>], 
_total_nodes: 0, 
_commitIndex: 0, 
_currentTerm: 0, 
_lastApplied: 0, 
_lastLogIndex: 0, 
_lastLogTerm: None
"""

msg = oserver._messageBoard.get_message()
# print(msg)
"""
AppendEntries: 0, RequestVote: 1, RequestVoteResponse: 2, Response: 3, _timestamp: 1581684927, 
_sender: 1, _receiver: 0, _data: {'lastLogIndex': 0, 'lastLogTerm': None}, _term: 1, _type: 1
"""
oserver.on_message(msg)

# print(oserver)
# print(server)
"""

_name: 0, 
_state: Follower ** _timeout: 500, _timeoutTime: 1581685712.0402, _last_vote: 1, 
_log: [], 
_messageBoard: board: [], 
_neighbors: [<servers.server.Server object at 0x1055104a8>], 
_total_nodes: 0, 
_commitIndex: 0, 
_currentTerm: 1, 
_lastApplied: 0, 
_lastLogIndex: 0, 
_lastLogTerm: None

_name: 1, 
_state: 
Candidate ** _last_vote: 1, _votes: {}, 
_log: [], 
_messageBoard: board: [<messages.request_vote.RequestVoteResponseMessage object at 0x1055105f8>], 
_neighbors: [<servers.server.Server object at 0x10550b908>], 
_total_nodes: 0, 
_commitIndex: 0, 
_currentTerm: 1, 
_lastApplied: 0, 
_lastLogIndex: 0, 
_lastLogTerm: None

"""



board = MemoryBoard()
state = Follower()
server0 = Server(0, state, [], board, [])
print(server0)
"""
_name: 0, 
_state: Follower ** _timeout: 500, _timeoutTime: 1581687254.687777, _last_vote: None, 
_log: [], 
_messageBoard: board: [], 
_neighbors: [], 
_total_nodes: 0, 
_commitIndex: 0, 
_currentTerm: 0, 
_lastApplied: 0, 
_lastLogIndex: 0, 
_lastLogTerm: None
"""

board = MemoryBoard()
state = Follower()
oserver = Server(1, state, [], board, [])
print(oserver)
"""
_name: 1, 
_state: Follower ** _timeout: 500, _timeoutTime: 1581687345.6878211, _last_vote: None, 
_log: [], 
_messageBoard: board: [], 
_neighbors: [], 
_total_nodes: 0, 
_commitIndex: 0, 
_currentTerm: 0, 
_lastApplied: 0, 
_lastLogIndex: 0, 
_lastLogTerm: None
"""

board = MemoryBoard()
state = Candidate()
server = Server(2, state, [], board, [oserver, server0])
print(server)
"""
_name: 2, 
_state: Candidate ** _last_vote: 2, _votes: {}, 
_log: [], 
_messageBoard: board: [], 
_neighbors: [<servers.server.Server object at 0x103203b00>, <servers.server.Server object at 0x103203780>], 
_total_nodes: 0, 
_commitIndex: 0, 
_currentTerm: 1, 
_lastApplied: 0, 
_lastLogIndex: 0, 
_lastLogTerm: None

"""

server0._neighbors.append(server)
oserver._neighbors.append(server)

msg = oserver._messageBoard.get_message()
print(msg)
"""
AppendEntries: 0, RequestVote: 1, RequestVoteResponse: 2, Response: 3, _timestamp: 1581688245, 
_sender: 2, _receiver: 0, _data: {'lastLogIndex': 0, 'lastLogTerm': None}, _term: 1, _type: 1
"""
oserver.on_message(msg)
print(oserver)
"""
_name: 1, _state: Follower ** _timeout: 500, _timeoutTime: 1581689033.635461, _last_vote: 2, _log: [], _messageBoard: board: [], _neighbors: [<servers.server.Server object at 0x10b9c3e48>], _total_nodes: 0, _commitIndex: 0, _currentTerm: 1, _lastApplied: 0, _lastLogIndex: 0, _lastLogTerm: None
"""

server0.on_message(server0._messageBoard.get_message())

server._total_nodes = 3

server.on_message(server._messageBoard.get_message())
server.on_message(server._messageBoard.get_message())

print(type(server._state))




class TestCandidateServer(unittest.TestCase):

    def setUp(self):
        board = MemoryBoard()
        state = Follower()
        self.oserver = Server(0, state, [], board, [])

        board = MemoryBoard()
        state = Candidate()  # 候选人
        self.server = Server(1, state, [], board, [self.oserver])

        self.oserver._neighbors.append(self.server)

    def test_candidate_server_had_intiated_the_election(self):

        self.assertEquals(1, len(self.oserver._messageBoard._board))

        self.oserver.on_message(self.oserver._messageBoard.get_message())

        self.assertEquals(1, len(self.server._messageBoard._board))
        self.assertEquals(True, self.server._messageBoard.get_message().data["response"])

    def test_candidate_server_had_gotten_the_vote(self):
        self.oserver.on_message(self.oserver._messageBoard.get_message())

        self.assertEquals(1, len(self.server._messageBoard._board))
        self.assertEquals(True, self.server._messageBoard.get_message().data["response"])

    def test_candidate_server_wins_election(self):
        board = MemoryBoard()
        state = Follower()
        server0 = Server(0, state, [], board, [])

        board = MemoryBoard()
        state = Follower()
        oserver = Server(1, state, [], board, [])

        board = MemoryBoard()
        state = Candidate()
        server = Server(2, state, [], board, [oserver, server0])

        server0._neighbors.append(server)
        oserver._neighbors.append(server)

        oserver.on_message(oserver._messageBoard.get_message())
        server0.on_message(server0._messageBoard.get_message())

        server._total_nodes = 3

        server.on_message(server._messageBoard.get_message())
        server.on_message(server._messageBoard.get_message())

        self.assertEquals(type(server._state), Leader)

    def test_two_candidates_tie(self):
        followers = []

        for i in range(4):
            board = MemoryBoard()
            state = Follower()
            followers.append(Server(i, state, [], board, []))

        board = MemoryBoard()
        state = Candidate()
        c0 = Server(5, state, [], board, followers[0:2])

        board = MemoryBoard()
        state = Candidate()
        c1 = Server(6, state, [], board, followers[2:])

        for i in range(2):
            followers[i]._neighbors.append(c0)
            followers[i].on_message(followers[i]._messageBoard.get_message())

        for i in range(2, 4):
            followers[i]._neighbors.append(c1)
            followers[i].on_message(followers[i]._messageBoard.get_message())

        c0._total_nodes = 6
        c1._total_nodes = 6

        for i in range(2):
            c0.on_message(c0._messageBoard.get_message())
            c1.on_message(c1._messageBoard.get_message())

        self.assertEquals(type(c0._state), Candidate)
        self.assertEquals(type(c1._state), Candidate)

    def test_two_candidates_one_wins(self):
        followers = []

        for i in range(6):
            board = MemoryBoard()
            state = Follower()
            followers.append(Server(i, state, [], board, []))

        board = MemoryBoard()
        state = Candidate()
        c0 = Server(7, state, [], board, followers[0:2])

        board = MemoryBoard()
        state = Candidate()
        c1 = Server(8, state, [], board, followers[2:])

        for i in range(2):
            followers[i]._neighbors.append(c0)
            followers[i].on_message(followers[i]._messageBoard.get_message())

        for i in range(2, 6):
            followers[i]._neighbors.append(c1)
            followers[i].on_message(followers[i]._messageBoard.get_message())

        c0._total_nodes = 7
        c1._total_nodes = 7

        for i in range(2):
            c0.on_message(c0._messageBoard.get_message())

        for i in range(4):
            c1.on_message(c1._messageBoard.get_message())

        self.assertEquals(type(c0._state), Candidate)
        self.assertEquals(type(c1._state), Leader)

    def test_candidate_fails_to_win_election_so_resend_request(self):
        pass

    def test_multiple_candidates_fail_to_win_so_resend_requests(self):
        pass
