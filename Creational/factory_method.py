from abc import ABCMeta,abstractmethod

class Interviewer:
    """
    Abstract class for Interviewer
    """
    __metaclass__=ABCMeta

    @abstractmethod
    def ask_questions(self):
        raise NotImplementedError

class Developer(Interviewer):
    """
    Concrete class for Developer Interviewer
    """

    def ask_questions(self):
        print "asks about distributed systems."

class Data_scientist(Interviewer):
    """
    Concrete class for Data Scientist Interviewer
    """

    def ask_questions(self):
        print "asks about convolutional neural nets."


class Hiring_manager:
    """
    Abstract class for Hiring Manager
    """

    __metaclass__=ABCMeta

    @abstractmethod
    def assign_interviewer(self):
        raise NotImplementedError

class Data_scientist_manager(Hiring_manager):
    """
    Concrete class for data scientist hiring manager
    """
    def assign_interviewer(self):
        return Data_scientist()


class Developer_manager(Hiring_manager):
    """
    Concrete class for developer hiring manager
    """
    def assign_interviewer(self):
        return Developer()


if __name__ == '__main__':
    data_scientist_manager = Data_scientist_manager()
    developer_manager = Developer_manager()

    data_science_interviewer = data_scientist_manager.assign_interviewer()
    developer_interviewer = developer_manager.assign_interviewer()

    data_science_interviewer.ask_questions()
    developer_interviewer.ask_questions()
