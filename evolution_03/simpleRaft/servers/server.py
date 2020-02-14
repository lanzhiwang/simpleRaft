

class Server(object):

    def __init__(self, name, state, log, messageBoard, neighbors):
        self._name = name
        self._state = state
        self._log = log
        self._messageBoard = messageBoard
        self._neighbors = neighbors
        self._total_nodes = 0

        self._commitIndex = 0
        self._currentTerm = 0

        self._lastApplied = 0

        self._lastLogIndex = 0
        self._lastLogTerm = None

        self._state.set_server(self)
        self._messageBoard.set_owner(self)

    def send_message(self, message):
        for n in self._neighbors:
            message._receiver = n._name
            n.post_message(message)

    def send_message_response(self, message):
        """
        ResponseMessage
        """
        n = [n for n in self._neighbors if n._name == message.receiver]
        if len(n) > 0:
            n[0].post_message(message)

    def post_message(self, message):
        self._messageBoard.post_message(message)

    def on_message(self, message):
        state, response = self._state.on_message(message)

        self._state = state

    def __str__(self):
        return '_name: %s, _state: %s, _log: %s, _messageBoard: %s, _neighbors: %s, _total_nodes: %s, _commitIndex: %s, _currentTerm: %s, _lastApplied: %s, _lastLogIndex: %s, _lastLogTerm: %s' % (self._name, self._state, self._log, self._messageBoard, self._neighbors, self._total_nodes, self._commitIndex, self._currentTerm, self._lastApplied, self._lastLogIndex, self._lastLogTerm)


