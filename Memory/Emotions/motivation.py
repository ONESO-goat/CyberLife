from typing import Dict, Any

class Motivation:
    def __init__(self, Brain, thought_system, level: float = 5):
        """
        Docstring for __init__
        
        Motivation is it's own league when it comes to emotions.
        Though with sadness, happiness, etc you feel that emotion at that current moment,
        with motivation, it scales how you feel.
        Example, you can be angry, but depending on your motivation it can really change things up.
        High motivation would probaly urge you to proceed with violence,
        but lower motivation likely means a simpler mood.
        
        :param Brain: Brain()
        :param level: Level of your motivation
        type level: float
        """
        self.Thoughts = thought_system
        self.level = level
        self.Brain = Brain

    def enhanced_motivation(self, scale: float,  
                            current_motivation: Dict[str, float],
                            boost: bool = False,):
        
        current = current_motivation['motivation']
        if boost:
            current += scale * 2
        else:
            current += scale
        current_motivation['motivation'] = current
        return current_motivation

    def feeling_motivated(self, data: Dict[str, float], auto_enhance: bool = False):
        """
        Docstring for feeling_motivated
        
        :param data: The data to be check status.
        :type data: Dict[str, float]
        :param auto_enhance: increase the value of this matter.
        :type auto_enhance: bool
        """

        yes_or_not = data['motivation']
        if not yes_or_not:
            raise ValueError("Error finding motivated componet in system.")
        if auto_enhance:
            self.enhanced_motivation(scale=1.0, current_motivation=data)
        if yes_or_not >= 5.0:
            return True
        elif yes_or_not < 5.0:
            return False
        
    def why(self):
        """Look into why the motivation."""
        if self.is_database(self.Thoughts):
            """Soon 'databases' can be looked into."""
            self.Thoughts.query.get(emotion[0])
    
    def is_database(self, system) -> NotImplementedError:
        """Check if system is a database."""
        return NotImplementedError("Not yet implemented")

        
        