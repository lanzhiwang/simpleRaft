from boards.memory_board import MemoryBoard
from messages.base import BaseMessage


board = MemoryBoard()
print(board)

msg = BaseMessage(0, 0, 0, 0)
print(msg)

board.post_message(msg)
for msg in board._board:
    print(msg)

print(board.get_message())

"""
board: []
AppendEntries: 0, RequestVote: 1, RequestVoteResponse: 2, Response: 3, _timestamp: 1581641629, _sender: 0, _receiver: 0, _data: 0, _term: 0
AppendEntries: 0, RequestVote: 1, RequestVoteResponse: 2, Response: 3, _timestamp: 1581641629, _sender: 0, _receiver: 0, _data: 0, _term: 0
AppendEntries: 0, RequestVote: 1, RequestVoteResponse: 2, Response: 3, _timestamp: 1581641629, _sender: 0, _receiver: 0, _data: 0, _term: 0
huzhi@huzhideMacBook-Pro simpleRaft %
"""