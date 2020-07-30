
from enum import Enum
from abc import ABC

class QuestionStatus(Enum):
    OPEN = "open" 
    CLOSED = "closed"
    DELETED = "deleted"

class Member:

    def __init__(self, **kwargs):
        self.id = id
        self.username = username
        self.reputation = reputation
        self.badge_ids = [] # system assigned


class Moderator(Member):

    def __init__(self, **kwargs):
        
        super(self).__init__(...)
        
        pass


class Question:
    
    def __init__(self **kwargs):
        self.id = id
        self.title = title
        self.description = description
        self.deleteion_votes = 0
        self.closure_votes = 0
        self.regular_votes = 0
        self.tags = set() # tag ids 
        self.status = QuestionStatus.OPEN
        self.comment_ids = [] # pull from DB whenever there someone makes a comment
        self.answer_ids = []


    def set_title(self, title):
        self.title = title

    def set_description(self, description):
        self.description = description
    
    def upvote(self):
        self.regular_votes += 1
    
    def downvote(self):
        self.regular_votes -= 1

    def vote_for_deletion(self):
        self.deletion_votes +=1 
    
    def vote_for_closure(self):
        self.closure_votes += 1

    
    def set_status(self, status):
        self.status = status

        # TO DO
        ## if status change from closure to open by moderator
        # reset closure votes to zero

        # if status changee from deleted too open by moderator
        # reset deletion votes to zero

    
class Answer:

    def __init__(self, **kwargs):
        self.id = id
        self.question_id = question_id
        self.content = conent
        self.votes = 0
        self.comment_ids = []

    
    def set_content(self):
        self.content = content
    
    def upvote(self):
        self.votes += 1
    
    def downvote(self):
        self.votes -= 1

class Comment:

    def __init__(self, **kwargs):

        self.id = id
        self.cotent = content
        self.timestamp = datetime.now()

class Badge:

    def __init__(self, **kwargs):
        self.id = id
        self.name = name
        self.description = description


class Tag:
    def __init__(self, **kwargs):
        self.id = id
        self.name = name



class Search(ABC):

    def search(self, query):
        None