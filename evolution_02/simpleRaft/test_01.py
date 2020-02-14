import unittest

from boards.memory_board import MemoryBoard
from messages.append_entries import AppendEntriesMessage
from messages.request_vote import RequestVoteMessage
from servers.server import Server
from states.follower import Follower


"""
follower-0 follower-1
oserver    server
sender     receiver

"""

board = MemoryBoard()
state = Follower()
oserver = Server(0, state, [], board, [])
# print(oserver)
"""
_name: 0, 
_state: <states.follower.Follower object at 0x1047fbd68>, 
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
server = Server(1, state, [], board, [oserver])
# print(server)
"""
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

msg = AppendEntriesMessage(0, 1, 2, {})
# print(msg)
"""
AppendEntries: 0, RequestVote: 1, RequestVoteResponse: 2, Response: 3, 
_timestamp: 1581654239, _sender: 0, _receiver: 1, _data: {}, _term: 2, _type: 0
"""
server.on_message(msg)
# print(server)
"""
_name: 1, 
_state: <states.follower.Follower object at 0x10d08afd0>, 
_log: [], 
_messageBoard: board: [], 
_neighbors: [<servers.server.Server object at 0x10d08acf8>], 
_total_nodes: 0, 
_commitIndex: 0, 
_currentTerm: 2, 
_lastApplied: 0, 
_lastLogIndex: 0, 
_lastLogTerm: None
"""

# print(server._messageBoard)
# print(oserver._messageBoard)



msg = AppendEntriesMessage( 0, 1, -1, {} )
# print(msg)
"""
AppendEntries: 0, RequestVote: 1, RequestVoteResponse: 2, Response: 3, 
_timestamp: 1581654505, _sender: 0, _receiver: 1, _data: {}, _term: -1, _type: 0
"""
server.on_message(msg)

# print(oserver)
# print(server)

"""
_name: 0, 
_state: <states.follower.Follower object at 0x10e6c8d68>, 
_log: [], 
_messageBoard: board: [<messages.response.ResponseMessage object at 0x10ebac400>], 
_neighbors: [], 
_total_nodes: 0, 
_commitIndex: 0, 
_currentTerm: 0, 
_lastApplied: 0, 
_lastLogIndex: 0, 
_lastLogTerm: None

_name: 1, 
_state: <states.follower.Follower object at 0x10ebac0b8>, 
_log: [], 
_messageBoard: board: [], 
_neighbors: [<servers.server.Server object at 0x10eba6d68>], 
_total_nodes: 0, 
_commitIndex: 0, 
_currentTerm: 2, 
_lastApplied: 0, 
_lastLogIndex: 0, 
_lastLogTerm: None
"""

msg = AppendEntriesMessage( 0, 1, 2, {} )
# print(msg)
"""
AppendEntries: 0, RequestVote: 1, RequestVoteResponse: 2, Response: 3, 
_timestamp: 1581656311, _sender: 0, _receiver: 1, _data: {}, _term: 2, _type: 0
"""
server.on_message( msg )

# print(oserver)
# print(server)
"""
_name: 0, 
_state: <states.follower.Follower object at 0x1103f2d68>, 
_log: [], 
_messageBoard: board: [<messages.response.ResponseMessage object at 0x1108d6400>], 
_neighbors: [], 
_total_nodes: 0, 
_commitIndex: 0, 
_currentTerm: 0, 
_lastApplied: 0, 
_lastLogIndex: 0, 
_lastLogTerm: None

_name: 1, 
_state: <states.follower.Follower object at 0x1108d60b8>, 
_log: [], 
_messageBoard: board: [], 
_neighbors: [<servers.server.Server object at 0x1108d0d68>], 
_total_nodes: 0, 
_commitIndex: 0, 
_currentTerm: 2, 
_lastApplied: 0, 
_lastLogIndex: 0, 
_lastLogTerm: None

"""

server._log.append({"term": 100, "value": 2000})
# print(server)
"""
_name: 1, 
_state: <states.follower.Follower object at 0x103ef31d0>, 
_log: [{'term': 100, 'value': 2000}], 
_messageBoard: board: [], 
_neighbors: [<servers.server.Server object at 0x103eece80>], 
_total_nodes: 0, 
_commitIndex: 0, 
_currentTerm: 2, 
_lastApplied: 0, 
_lastLogIndex: 0, 
_lastLogTerm: None
"""
msg = AppendEntriesMessage( 0, 1, 2, {
					"prevLogIndex": 0,
					"prevLogTerm": 1,
					"leaderCommit": 1,
					"entries": [ { "term": 1, "value": 100 } ] } )
# print(msg)
"""
AppendEntries: 0, RequestVote: 1, RequestVoteResponse: 2, Response: 3, _timestamp: 1581657120, 
_sender: 0, _receiver: 1, 
_data: {'prevLogIndex': 0, 'prevLogTerm': 1, 'leaderCommit': 1, 'entries': [{'term': 1, 'value': 100}]}, 
_term: 2, _type: 0
"""
server.on_message( msg )
# print(oserver)
# print(server)
"""
_name: 0, 
_state: <states.follower.Follower object at 0x106188e80>, 
_log: [], 
_messageBoard: board: [<messages.response.ResponseMessage object at 0x10666d518>, <messages.response.ResponseMessage object at 0x10666d550>], 
_neighbors: [], 
_total_nodes: 0, 
_commitIndex: 0, 
_currentTerm: 0, 
_lastApplied: 0, 
_lastLogIndex: 0, 
_lastLogTerm: None

_name: 1, 
_state: <states.follower.Follower object at 0x10666d1d0>, 
_log: [], 
_messageBoard: board: [], 
_neighbors: [<servers.server.Server object at 0x106666e80>], 
_total_nodes: 0, 
_commitIndex: 0, 
_currentTerm: 2, 
_lastApplied: 0, 
_lastLogIndex: 0, 
_lastLogTerm: 1
"""


server._log.append( { "term": 1, "value": 0 } )
server._log.append( { "term": 1, "value": 200 } )
server._log.append( { "term": 1, "value": 300 } )
server._log.append( { "term": 2, "value": 400 } )

# print(server)
"""
_name: 1, 
_state: <states.follower.Follower object at 0x109622400>, 
_log: [{'term': 1, 'value': 0}, {'term': 1, 'value': 200}, {'term': 1, 'value': 300}, {'term': 2, 'value': 400}], 
_messageBoard: board: [], 
_neighbors: [<servers.server.Server object at 0x109622128>], 
_total_nodes: 0, 
_commitIndex: 0, 
_currentTerm: 2, 
_lastApplied: 0, 
_lastLogIndex: 0, 
_lastLogTerm: 1

"""
msg = AppendEntriesMessage( 0, 1, 2, {
					"prevLogIndex": 0,
					"prevLogTerm": 1,
					"leaderCommit": 1,
					"entries": [ { "term": 1, "value": 100 } ] } )

# print(msg)
"""
AppendEntries: 0, RequestVote: 1, RequestVoteResponse: 2, Response: 3, 
_timestamp: 1581659930, _sender: 0, _receiver: 1, 
_data: {'prevLogIndex': 0, 'prevLogTerm': 1, 'leaderCommit': 1, 
'entries': [{'term': 1, 'value': 100}]}, _term: 2, _type: 0
"""

server.on_message( msg )

# print(oserver)
# print(server)

"""
_name: 0, 
_state: <states.follower.Follower object at 0x108bbb128>, 
_log: [], 
_messageBoard: board: [<messages.response.ResponseMessage object at 0x109089780>, 
<messages.response.ResponseMessage object at 0x1090897b8>, 
<messages.response.ResponseMessage object at 0x109089588>, 
<messages.response.ResponseMessage object at 0x109089c18>], 
_neighbors: [], 
_total_nodes: 0, 
_commitIndex: 0, 
_currentTerm: 0, 
_lastApplied: 0, 
_lastLogIndex: 0, 
_lastLogTerm: None

_name: 1, 
_state: <states.follower.Follower object at 0x109089438>, 
_log: [{'term': 1, 'value': 0}, {'term': 1, 'value': 100}], 
_messageBoard: board: [], 
_neighbors: [<servers.server.Server object at 0x109089128>], 
_total_nodes: 0, 
_commitIndex: 2, 
_currentTerm: 2, 
_lastApplied: 0, 
_lastLogIndex: 1, 
_lastLogTerm: 1

"""

msg = AppendEntriesMessage( 0, 1, 2, {
							"prevLogIndex": 0,
							"prevLogTerm": 100,
							"leaderCommit": 1,
							"entries": [ { "term": 1, "value": 100 } ] } )

# print(msg)
"""
AppendEntries: 0, RequestVote: 1, RequestVoteResponse: 2, Response: 3, 
_timestamp: 1581669569, _sender: 0, _receiver: 1, 
_data: {'prevLogIndex': 0, 'prevLogTerm': 100, 'leaderCommit': 1, 'entries': [{'term': 1, 'value': 100}]}, 
_term: 2, _type: 0
"""
server.on_message( msg )

# print(oserver)
# print(server)
"""
_name: 0, 
_state: <states.follower.Follower object at 0x10099d1d0>, 
_log: [], 
_messageBoard: board: [<messages.response.ResponseMessage object at 0x100e6c828>, 
<messages.response.ResponseMessage object at 0x100e6c860>, 
<messages.response.ResponseMessage object at 0x100e6c630>, 
<messages.response.ResponseMessage object at 0x100e6ccc0>, 
<messages.response.ResponseMessage object at 0x100e6c898>], 
_neighbors: [], 
_total_nodes: 0, 
_commitIndex: 0, 
_currentTerm: 0, 
_lastApplied: 0, 
_lastLogIndex: 0, 
_lastLogTerm: None

_name: 1, 
_state: <states.follower.Follower object at 0x100e6c4e0>, 
_log: [], 
_messageBoard: board: [], 
_neighbors: [<servers.server.Server object at 0x100e6c1d0>], 
_total_nodes: 0, 
_commitIndex: 1, 
_currentTerm: 2, 
_lastApplied: 0, 
_lastLogIndex: 0, 
_lastLogTerm: 100


"""




board = MemoryBoard()
state = Follower()
oserver = Server(0, state, [], board, [])

board = MemoryBoard()
state = Follower()
server = Server(1, state, [], board, [oserver])

# print(oserver)
# print(server)
"""
_name: 0, 
_state: <states.follower.Follower object at 0x1040d6cc0>, 
_log: [], 
_messageBoard: board: [], 
_neighbors: [], 
_total_nodes: 0, 
_commitIndex: 0, 
_currentTerm: 0, 
_lastApplied: 0, 
_lastLogIndex: 0, 
_lastLogTerm: None

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

"""

msg = RequestVoteMessage(0, 1, 2, {"lastLogIndex": 0, "lastLogTerm": 0, "entries": []})
# print(msg)
"""
AppendEntries: 0, RequestVote: 1, RequestVoteResponse: 2, Response: 3, _timestamp: 1581673220, 
_sender: 0, _receiver: 1, 
_data: {'lastLogIndex': 0, 'lastLogTerm': 0, 'entries': []}, 
_term: 2, _type: 1
"""
server.on_message(msg)

# print(oserver)
# print(server)
"""
_name: 0, 
_state: <states.follower.Follower object at 0x105a17e48>, 
_log: [], 
_messageBoard: board: [<messages.request_vote.RequestVoteResponseMessage object at 0x105a17e10>], 
_neighbors: [], 
_total_nodes: 0, 
_commitIndex: 0, 
_currentTerm: 0, 
_lastApplied: 0, 
_lastLogIndex: 0, 
_lastLogTerm: None

_name: 1, 
_state: <states.follower.Follower object at 0x1057685f8>, 
_log: [], _messageBoard: board: [], 
_neighbors: [<servers.server.Server object at 0x105a17ef0>], 
_total_nodes: 0, 
_commitIndex: 0, 
_currentTerm: 2, 
_lastApplied: 0, 
_lastLogIndex: 0, 
_lastLogTerm: None

"""



board = MemoryBoard()
state = Follower()
oserver = Server(0, state, [], board, [])

board = MemoryBoard()
state = Follower()
server = Server(1, state, [], board, [oserver])

print(oserver)
print(server)
"""
_name: 0, 
_state: <states.follower.Follower object at 0x1040d6cc0>, 
_log: [], 
_messageBoard: board: [], 
_neighbors: [], 
_total_nodes: 0, 
_commitIndex: 0, 
_currentTerm: 0, 
_lastApplied: 0, 
_lastLogIndex: 0, 
_lastLogTerm: None

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

"""

msg = RequestVoteMessage(2, 1, 2, {})
server.on_message(msg)



class TestFollowerServer(unittest.TestCase):
    def setUp(self):
        board = MemoryBoard()
        state = Follower()
        self.oserver = Server(0, state, [], board, [])

        board = MemoryBoard()
        state = Follower()
        self.server = Server(1, state, [], board, [self.oserver])

    def test_follower_server_on_message(self):
        msg = AppendEntriesMessage(0, 1, 2, {})
        self.server.on_message(msg)

    def test_follower_server_on_receive_message_with_lesser_term(self):
        msg = AppendEntriesMessage(0, 1, -1, {})
        self.server.on_message(msg)

        self.assertEquals(False, self.oserver._messageBoard.get_message().data["response"])

    def test_follower_server_on_receive_message_with_greater_term(self):
        msg = AppendEntriesMessage(0, 1, 2, {})
        self.server.on_message(msg)
        self.assertEquals(2, self.server._currentTerm)

    def test_follower_server_on_receive_message_where_log_does_not_have_prevLogTerm(self):
        self.server._log.append({"term": 100, "value": 2000})
        msg = AppendEntriesMessage(0, 1, 2, {"prevLogIndex": 0, "prevLogTerm": 1, "leaderCommit": 1, "entries": [{"term": 1, "value": 100}]})
        self.server.on_message(msg)
        self.assertEquals(False, self.oserver._messageBoard.get_message().data["response"])
        self.assertEquals([], self.server._log)

    def test_follower_server_on_receive_message_where_log_contains_conflicting_entry_at_new_index(self):
        self.server._log.append({"term": 1, "value": 0})
        self.server._log.append({"term": 1, "value": 200})
        self.server._log.append({"term": 1, "value": 300})
        self.server._log.append({"term": 2, "value": 400})

        msg = AppendEntriesMessage(0, 1, 2, {"prevLogIndex": 0, "prevLogTerm": 1, "leaderCommit": 1, "entries": [{"term": 1, "value": 100}]})
        self.server.on_message(msg)
        self.assertEquals({"term": 1, "value": 100}, self.server._log[1])
        self.assertEquals([{"term": 1, "value": 0}, {"term": 1, "value": 100}], self.server._log)

    def test_follower_server_on_receive_message_where_log_is_empty_and_receives_its_first_value(self):
        msg = AppendEntriesMessage(0, 1, 2, {"prevLogIndex": 0, "prevLogTerm": 100, "leaderCommit": 1, "entries": [{"term": 1, "value": 100}]})
        self.server.on_message(msg)
        self.assertEquals({"term": 1, "value": 100}, self.server._log[0])

    def test_follower_server_on_receive_vote_request_message(self):
        msg = RequestVoteMessage(0, 1, 2, {"lastLogIndex": 0, "lastLogTerm": 0, "entries": []})
        self.server.on_message(msg)
        self.assertEquals(0, self.server._state._last_vote)
        self.assertEquals(True, self.oserver._messageBoard.get_message().data["response"])

    def test_follower_server_on_receive_vote_request_after_sending_a_vote(self):
        msg = RequestVoteMessage(0, 1, 2, {"lastLogIndex": 0, "lastLogTerm": 0, "entries": []})
        self.server.on_message(msg)

        msg = RequestVoteMessage(2, 1, 2, {})
        self.server.on_message(msg)
        self.assertEquals(0, self.server._state._last_vote)
