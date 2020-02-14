from .base import BaseMessage


class RequestVoteMessage(BaseMessage):

    _type = BaseMessage.RequestVote

    def __init__(self, sender, receiver, term, data):
        BaseMessage.__init__(self, sender, receiver, term, data)

    def __str__(self):
        return 'AppendEntries: %s, RequestVote: %s, RequestVoteResponse: %s, Response: %s, _timestamp: %s, _sender: %s, _receiver: %s, _data: %s, _term: %s, _type: %s' % (self.AppendEntries, self.RequestVote, self.RequestVoteResponse, self.Response, self._timestamp, self._sender, self._receiver, self._data, self._term, self._type)



class RequestVoteResponseMessage(BaseMessage):

    _type = BaseMessage.RequestVoteResponse

    def __init__(self, sender, receiver, term, data):
        BaseMessage.__init__(self, sender, receiver, term, data)

    def __str__(self):
        return 'AppendEntries: %s, RequestVote: %s, RequestVoteResponse: %s, Response: %s, _timestamp: %s, _sender: %s, _receiver: %s, _data: %s, _term: %s, _type: %s' % (self.AppendEntries, self.RequestVote, self.RequestVoteResponse, self.Response, self._timestamp, self._sender, self._receiver, self._data, self._term, self._type)

