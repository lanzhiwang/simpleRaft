import time


class BaseMessage(object):
    AppendEntries = 0
    RequestVote = 1
    RequestVoteResponse = 2
    Response = 3

    def __init__(self, sender, receiver, term, data):
        self._timestamp = int(time.time())

        self._sender = sender
        self._receiver = receiver
        self._data = data
        self._term = term

    @property
    def receiver(self):
        return self._receiver

    @property
    def sender(self):
        return self._sender

    @property
    def data(self):
        return self._data

    @property
    def timestamp(self):
        return self._timestamp

    @property
    def term(self):
        return self._term

    @property
    def type(self):
        return self._type

    def __str__(self):
        return 'AppendEntries: %s, RequestVote: %s, RequestVoteResponse: %s, Response: %s, _timestamp: %s, _sender: %s, _receiver: %s, _data: %s, _term: %s' % (self.AppendEntries, self.RequestVote, self.RequestVoteResponse, self.Response, self._timestamp, self._sender, self._receiver, self._data, self._term)
