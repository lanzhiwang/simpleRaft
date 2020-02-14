from boards.memory_board import MemoryBoard
from messages.base import BaseMessage


board = MemoryBoard()

msg = BaseMessage(0, 0, 0, 0)
msg2 = BaseMessage(0, 0, 0, 0)
msg2._timestamp -= 100

board.post_message(msg)
board.post_message(msg2)
for msg in board._board:
    print(msg)
print()
print(board.get_message())
"""
AppendEntries: 0, RequestVote: 1, RequestVoteResponse: 2, Response: 3, _timestamp: 1581641751, _sender: 0, _receiver: 0, _data: 0, _term: 0
AppendEntries: 0, RequestVote: 1, RequestVoteResponse: 2, Response: 3, _timestamp: 1581641651, _sender: 0, _receiver: 0, _data: 0, _term: 0

AppendEntries: 0, RequestVote: 1, RequestVoteResponse: 2, Response: 3, _timestamp: 1581641651, _sender: 0, _receiver: 0, _data: 0, _term: 0
"""