"""
This is where the YAGNI short for "You Aren't Gonna Need It" comes to the rescue.

Always implement things when you actually need them, never when you just foresee that you might need them.

Reduced waste: By only implementing what's necessary, you avoid wasting time and effort on unnecessary code.

Simplified codebase: YAGNI promotes a lean and simple codebase, making it easier to maintain and update.

Faster development: A laser focus on immediate needs means you get features out the door faster. You're not bogged down by potential "what ifs".

Improved adaptability: With a flexible and modular codebase, you can respond quickly to changing requirements.


"""

class BlogPost():
    """
    In this example the likes , shares and reactions are defined and still not being used
    """

    def __init__(self,title,content):

        self.title = title
        self.content = content
        self.likes = 0
        self.shares = 0
        self.reactions = { 'love' : 0 , 'wow' : 0 , 'angry': 0 }

    def get_title(self):

        print(f"The title is {self.title}")

        return True

    
    def get_content(self):

        print(f"The content are {self.content}")

        return True
    


class BlogPost():
    """
    In this example the defined things are used as well 
    """

    def __init__(self,title,content):

        self.title = title
        self.content = content

    def get_title(self):

        print(f"The title is {self.title}")

        return True

    
    def get_content(self):

        print(f"The content are {self.content}")

        return True
