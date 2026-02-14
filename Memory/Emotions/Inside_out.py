# Inside_out.py


from typing import Dict, List, Optional, Any
import numpy as np

class Emotion:
    def __init__(self, name: str, scale: float = 5.0):
        self.scale = float(scale)
        self.name = name

    def adjust(self, amount: float):
        self.scale += amount
    def increase(self, amount: float = 1.0):
        """Increase emotion intensity."""
        self.level = min(10.0, self.level + amount)
    
    def decrease(self, amount: float = 1.0):
        """Decrease emotion intensity."""
        self.level = max(0.0, self.level - amount)
    
    def matches(self, emotion_word: str) -> bool:
        """Check if emotion word matches this emotion type."""
        emotion_word = emotion_word.lower().strip()
        return emotion_word in self.get_keywords()
    def get_keywords(self) -> List[str]:
        """Override in subclasses."""
        return []

    


class Joy(Emotion):
    def __init__(self):
        super().__init__("Joy")

        self.subclass: Dict = self.get_keywords()

        self.level: float = 0.0

        self.subemotions = {
            'joy': 0.0,
            'excitement': 0.0,
            'contentment': 0.0,
            'pride': 0.0
        }

    def _feeling_happy(self, data: Dict) -> bool:
        print("="*50)
        print("IN [_feeling_happy]\n")
        print("="*50)
        emo = []
        for list_ in self.subclass.values():
            for char in list_:
                emo.append(char)
        
        print(f"[_feeling_happy]: emo = {emo}\n")
        yes_or_not = data['emotion']
        print(f"yes_or_not {yes_or_not}")
        if not yes_or_not or yes_or_not == None:
            raise ValueError(f"\nData ({data}) is wrong, please insert valid data; make sure key is 'emotion' without a 's'")
        if yes_or_not not in self.subclass.keys() and yes_or_not not in emo:
            return False
        return True
    
    def joy(self, 
              Emotion_adjust_by: float, 
              data: Optional[Dict[str, Any]] = None,
              why: str = '',
              achieve: bool = True,
              priority: int = 1): 
        
        print("="*50)
        print("IN [joy] FUNCTION")
        print("="*50)
        
        JOY = 'joy'
        self.subemotions['joy'] += Emotion_adjust_by
        print(f"DATA: {data}")

        if data is not None:
            print("="*30)
            print("DATA IS NOT NONE")
            print("="*30)
            emotion = data.get('emotion', None)
            if not emotion:
                raise ValueError(f"missing emotion key: {data}") 
            data['emotion'] = {
                JOY: {"regulation": np.zeros((4,4))}
            }
            
            """Emotions can vary. should look like this:
            
            [0.0 0.0 0.0 0.0] # top row focuses on emotion control (tenisty of this emotion), Responsible for high-level emotional control, decision-making, and rational thought.
            [0.0 0.0 0.0 0.0] # 2nd row focuses on physiological responses
            [0.0 0.0 0.0 0.0] # 3rd row focuses on facial expression (implement system for face plates in the future)
            [0.0 0.0 0.0 0.0] # Reward Circuitry, Involves the dopamine-rich ventral tegmental area and ventral striatum. # forebrain feature 
            """
            if priority == 1:
                matter = 1.0
            elif priority == 2:
                matter = 0.5
            elif priority == 3:
                matter = 0.25
            else:
                raise ValueError(f"Priority ({priority}) is invalid. Please choose from 1 - 2 - 3.")
            
            data['priority'] = {
                priority: matter
            }
            print(f"MATTER {matter}")

            if why.strip() != '':
                data['why_this_feeling'] = why
            else: 
                data['why_this_feeling'] = """You feel this way for an unknown reason."""            

            if achieve:
                print("WE ARE ACHIEVING NEW DATA\n")
                print(f"NEW DATA {data}")
                return data

    def excitement(self, 
              Emotion_adjust_by: float, 
              data: Optional[Dict[str, Any]] = None,
              why: str = '',
              achieve: bool = True,
              priority: int = 1): 
        
        EXCITEMENT = 'excitement'
        self.subemotions['excitement'] += Emotion_adjust_by

        if data is not None:
            emotion = data.get('emotion', None)
            if not emotion:
                raise ValueError(f"missing emotion key: {data}") 
            data['emotion'] = {
                EXCITEMENT: {"regulation": np.zeros((4,4))}
            }
            
            """Emotions can vary. should look like this:
            
            [0.0 0.0 0.0 0.0] # top row focuses on emotion control (tenisty of this emotion), Responsible for high-level emotional control, decision-making, and rational thought.
            [0.0 0.0 0.0 0.0] # 2nd row focuses on physiological responses
            [0.0 0.0 0.0 0.0] # 3rd row focuses on facial expression (implement system for face plates in the future)
            [0.0 0.0 0.0 0.0] # Reward Circuitry, Involves the dopamine-rich ventral tegmental area and ventral striatum. # forebrain feature 
            """
            if priority == 1:
                matter = 1.0
            elif priority == 2:
                matter = 0.5
            elif priority == 3:
                matter = 0.25
            else:
                raise ValueError(f"Priority ({priority}) is invalid. Please choose from 1 - 2 - 3.")
            
            data['priority'] = {
                priority: matter
            }

            if why.strip() != '':
                data['why_this_feeling'] = why
            else: 
                data['why_this_feeling'] = """You feel this way for an unknown reason."""            

            if achieve:
                return data

    def contentment(self, 
              Emotion_adjust_by: float, 
              data: Optional[Dict[str, Any]] = None,
              why: str = '',
              achieve: bool = True,
              priority: int = 1): 
        
        CONTENTMENT = 'contentment'
        self.subemotions['contentment'] += Emotion_adjust_by

        if data is not None:
            emotion = data.get('emotion', None)
            if not emotion:
                raise ValueError(f"missing emotion key: {data}") 
            data['emotion'] = {
                CONTENTMENT: {"regulation": np.zeros((4,4))}
            }
            
            """Emotions can vary. should look like this:
            
            [0.0 0.0 0.0 0.0] # top row focuses on emotion control (tenisty of this emotion), Responsible for high-level emotional control, decision-making, and rational thought.
            [0.0 0.0 0.0 0.0] # 2nd row focuses on physiological responses
            [0.0 0.0 0.0 0.0] # 3rd row focuses on facial expression (implement system for face plates in the future)
            [0.0 0.0 0.0 0.0] # Reward Circuitry, Involves the dopamine-rich ventral tegmental area and ventral striatum. # forebrain feature 
            """
            if priority == 1:
                matter = 1.0
            elif priority == 2:
                matter = 0.5
            elif priority == 3:
                matter = 0.25
            else:
                raise ValueError(f"Priority ({priority}) is invalid. Please choose from 1 - 2 - 3.")
            
            data['priority'] = {
                priority: matter
            }

            if why.strip() != '':
                data['why_this_feeling'] = why
            else: 
                data['why_this_feeling'] = """You feel this way for an unknown reason."""            

            if achieve:
                return data

    def pride(self, 
              Emotion_adjust_by: float, 
              data: Optional[Dict[str, Any]] = None,
              why: str = '',
              achieve: bool = True,
              priority: int = 1): 
        print("="*40)
        print("INSIDE [pride] FUNCTION in Inside_out.py")
        print("="*40)
        PRIDE = 'pride'
        self.subemotions['pride'] += Emotion_adjust_by

        if data is not None:
            emotion = data.get('emotion', None)
            if not emotion:
                raise ValueError(f"missing emotion key: {data}") 
            data['emotion'] = {
                PRIDE: {"regulation": np.zeros((4,4))}
            }
            
            """Emotions can vary. should look like this:
            
            [0.0 0.0 0.0 0.0] # top row focuses on emotion control (tenisty of this emotion), Responsible for high-level emotional control, decision-making, and rational thought.
            [0.0 0.0 0.0 0.0] # 2nd row focuses on physiological responses
            [0.0 0.0 0.0 0.0] # 3rd row focuses on facial expression (implement system for face plates in the future)
            [0.0 0.0 0.0 0.0] # Reward Circuitry, Involves the dopamine-rich ventral tegmental area and ventral striatum. # forebrain feature 
            """
            if priority == 1:
                matter = 1.0
            elif priority == 2:
                matter = 0.5
            elif priority == 3:
                matter = 0.25
            else:
                raise ValueError(f"Priority ({priority}) is invalid. Please choose from 1 - 2 - 3.")
            print(f'MATTER: {matter}')
            data['priority'] = {
                priority: matter
            }

            if why.strip() != '':
                data['why_this_feeling'] = why
            else: 
                data['why_this_feeling'] = """You feel this way for an unknown reason."""            

            if achieve:
                return data
            
    def happy_keyword_query(self, emotion: str, data: Optional[Dict[str, Any]] = None):
        print("="*50)
        print("INSIDE [happy_keyword_query] in Inside_out.py")
        print("="*50)
        emotion = emotion.lower()
        print(f"[happy_keyword_query] EMOTION: {emotion}")

        function = {
            'pride': self.pride,
            'joy': self.joy,
            'contentment': self.contentment,
            'excitement': self.excitement
        }
        try:
            print("LOOPING IN happy_keyword_query")
            for emotion_, list_ in self.subclass.items():
                print(f"CURRENT EMOTION_ {emotion_}\n")
                if emotion == emotion_:
                    print(f"MATCHES: {emotion}/{emotion_}\n")
                    print(f"running: function[{emotion_.lower()}](Emotion_adjust_by=1.0, data=data)\n")
                    return function[emotion_.lower()](Emotion_adjust_by=1.0, data=data)
                else:
                    print("LOOPING LIST\n")
                    for char in list_:
                        print(f"CURRENT CHAR: {char}\n")
                        if char == emotion:
                            print(f"MATCHES {char}/{emotion}\n")
                            print(f"running: function[{emotion_.lower()}](Emotion_adjust_by=1.0, data=data)\n")
                            return function[emotion_.lower()](Emotion_adjust_by=1.0, data=data)
        except RuntimeError as e:
            raise RuntimeError(f"There was an error while querying for keywords for happiness: {e}")
                
    def increase(self, amount: float):
        """Increase overall happiness."""
        self.level = min(10.0, self.level + amount)
    
    def decrease(self, amount: float):
        """Decrease overall happiness."""
        self.level = max(0.0, self.level - amount)
    
    def get_level(self) -> float:
        """Current happiness intensity."""
        return self.level

    def get_keywords(self) -> Dict[str, List[str]]:
        return {
            'joy': ['joyful', 'happy'],
            'excitment': ['excitement'],
            'contentment': [],
            'pride': [ 'proud', 'prideful']
        }
    
    def __repr__(self) -> str:
        return f"""Happy=[{self.subclass}]"""


class Sadness(Emotion):
    def __init__(self):
        super().__init__("Sadness")
        self.subclass = self.get_keywords()
        
        self.level: float = 0.0

        self.subemotions = {
            'upset': 0.0,
            'disappointment': 0.0,
            'grief': 0.0,
            'loneliness': 0.0
        }

    
    def _feeling_upset(self, data: Dict) -> bool:
        
        yes_or_not = data['emotion']
        if not yes_or_not or yes_or_not == None:
            raise ValueError(f"Data ({data}) is wrong, please insert valid data.")
        if yes_or_not not in self.subclass.keys():
            return False
        return True

    def upset(self, 
              Emotion_adjust_by: float, 
              data: Optional[Dict[str, Any]] = None,
              why: str = '',
              achieve: bool = False,
              priority: int = 1): 
        """
        Docstring for upset
        
        Emotion_adjust_by: adjust this emotion level
        data: Change emotions of your system
        why: Explain why on this change and feeling 
        achieve: optain new data set
        priority: can feel 3 different emotions at ounce. first priority is the emotion showcased the most
        
        """
        
        UPSET = 'upset'
        self.subemotions['upset'] += Emotion_adjust_by

        if data is not None:
            emotion = data.get('emotion', None)
            if not emotion:
                raise ValueError(f"missing emotion key: {data}") 
            data['emotion'] = {
                UPSET: {"regulation": np.zeros((4,4))}
            }

            """Emotions can vary. should look like this:
            
            [0.0 0.0 0.0 0.0] # top row focuses on emotion control (tenisty of this emotion), Responsible for high-level emotional control, decision-making, and rational thought.
            [0.0 0.0 0.0 0.0] # 2nd row focuses on physiological responses
            [0.0 0.0 0.0 0.0] # 3rd row focuses on facial expression (implement system for face plates in the future)
            [0.0 0.0 0.0 0.0] # Reward Circuitry, Involves the dopamine-rich ventral tegmental area and ventral striatum. # forebrain feature 
            """
            if priority == 1:
                matter = 1.0
            elif priority == 2:
                matter = 0.5
            elif priority == 3:
                matter = 0.25
            else:
                raise ValueError(f"Priority ({priority}) is invalid. Please choose from 1 - 2 - 3.")
            
            data['priority'] = {
                priority: matter
            }

            if why.strip() != '':
                data['why_this_feeling'] = why
            else: 
                data['why_this_feeling'] = 'unkown'
            

            if achieve:
                return data

            

            


    def disappointment(self, 
              Emotion_adjust_by: float, 
              data: Optional[Dict[str, Any]] = None,
              why: str = '',
              achieve: bool = False,
              priority: int = 1): 
        
        DISAPPOINTED = 'disappointment'
        self.subemotions['disappointment'] += Emotion_adjust_by

        if data is not None:
            emotion = data.get('emotion', None)
            if not emotion:
                raise ValueError(f"missing emotion key: {data}") 
            data['emotion'] = {
                DISAPPOINTED: {"regulation": np.zeros((4,4))}
            }
            
            """Emotions can vary. should look like this:
            
            [0.0 0.0 0.0 0.0] # top row focuses on emotion control (tenisty of this emotion), Responsible for high-level emotional control, decision-making, and rational thought.
            [0.0 0.0 0.0 0.0] # 2nd row focuses on physiological responses
            [0.0 0.0 0.0 0.0] # 3rd row focuses on facial expression (implement system for face plates in the future)
            [0.0 0.0 0.0 0.0] # Reward Circuitry, Involves the dopamine-rich ventral tegmental area and ventral striatum. # forebrain feature 
            """
            if priority == 1:
                matter = 1.0
            elif priority == 2:
                matter = 0.5
            elif priority == 3:
                matter = 0.25
            else:
                raise ValueError(f"Priority ({priority}) is invalid. Please choose from 1 - 2 - 3.")
            
            data['priority'] = {
                priority: matter
            }

            if why.strip() != '':
                data['why_this_feeling'] = why
            else: 
                data['why_this_feeling'] = """You feel this way for an unknown reason."""            

            if achieve:
                return data

    def grief(self, 
              Emotion_adjust_by: float, 
              data: Optional[Dict[str, Any]] = None,
              why: str = '',
              achieve: bool = False,
              priority: int = 1): 
        
        GRIEF = 'greif'
        self.subemotions['greif'] += Emotion_adjust_by

        if data is not None:
            emotion = data.get('emotion', None)
            if not emotion:
                raise ValueError(f"missing emotion key: {data}") 
            data['emotion'] = {
                GRIEF: {"regulation": np.zeros((4,4))}
            }
            
            """Emotions can vary. should look like this:
            
            [0.0 0.0 0.0 0.0] # top row focuses on emotion control (tenisty of this emotion), Responsible for high-level emotional control, decision-making, and rational thought.
            [0.0 0.0 0.0 0.0] # 2nd row focuses on physiological responses
            [0.0 0.0 0.0 0.0] # 3rd row focuses on facial expression (implement system for face plates in the future)
            [0.0 0.0 0.0 0.0] # Reward Circuitry, Involves the dopamine-rich ventral tegmental area and ventral striatum. # forebrain feature 
            """
            if priority == 1:
                matter = 1.0
            elif priority == 2:
                matter = 0.5
            elif priority == 3:
                matter = 0.25
            else:
                raise ValueError(f"Priority ({priority}) is invalid. Please choose from 1 - 2 - 3.")
            
            data['priority'] = {
                priority: matter
            }

            if why.strip() != '':
                data['why_this_feeling'] = why
            else: 
                data['why_this_feeling'] = """You feel this way for an unknown reason."""            

            if achieve:
                return data

    def loneliness(self, 
              Emotion_adjust_by: float, 
              data: Optional[Dict[str, Any]] = None,
              why: str = '',
              achieve: bool = False,
              priority: int = 1): 
        
        LONELINESS = 'loneliness'
        self.subemotions['loneliness'] += Emotion_adjust_by

        if data is not None:
            emotion = data.get('emotion', None)
            if not emotion:
                raise ValueError(f"missing emotion key: {data}") 
            data['emotion'] = {
                LONELINESS: {"regulation": np.zeros((4,4))}
            }
            
            """Emotions can vary. should look like this:
            
            [0.0 0.0 0.0 0.0] # top row focuses on emotion control (tenisty of this emotion), Responsible for high-level emotional control, decision-making, and rational thought.
            [0.0 0.0 0.0 0.0] # 2nd row focuses on physiological responses
            [0.0 0.0 0.0 0.0] # 3rd row focuses on facial expression (implement system for face plates in the future)
            [0.0 0.0 0.0 0.0] # Reward Circuitry, Involves the dopamine-rich ventral tegmental area and ventral striatum. # forebrain feature 
            """
            if priority == 1:
                matter = 1.0
            elif priority == 2:
                matter = 0.5
            elif priority == 3:
                matter = 0.25
            else:
                raise ValueError(f"Priority ({priority}) is invalid. Please choose from 1 - 2 - 3.")
            
            data['priority'] = {
                priority: matter
            }

            if why.strip() != '':
                data['why_this_feeling'] = why
            else: 
                data['why_this_feeling'] = """You feel this way for an unknown reason."""            

            if achieve:
                return data
            
    def increase(self, amount: float):
        """Increase overall happiness."""
        self.level = min(10.0, self.level + amount)
    
    def decrease(self, amount: float):
        """Decrease overall happiness."""
        self.level = max(0.0, self.level - amount)
    
    def get_level(self) -> float:
        """Current happiness intensity."""
        return self.level
    
    def get_keywords(self) -> Dict[str, List[str]]:
        return {
            'upset': [ 'sadness','sad'],
            'disappointment': ['disappointed'],
            'grief': ['grieving'],
            'loneliness': ['lonely']
        }
    
    def __repr__(self) -> str:
        return f"""Sad=[{self.subclass}]"""



class Anger(Emotion):

    def __init__(self):
        super().__init__("Anger")

        self.subclass: List[str] = self.get_keywords()
        
        self.level: float = 0.0

        self.subemotions = {
            'frustration': 0.0,
            'rage': 0.0,
            'irritation': 0.0,
            'resentment': 0.0
        }

    def _feeling_angry(self, data: Dict[str, str]) -> bool:

        yes_or_not = data['emotion']
        if not yes_or_not or yes_or_not == None:
            raise ValueError(f"Data ({data}) is wrong, please insert valid data.")

        if yes_or_not not in self.subclass:
            return False
        return True
    
    def frustration(self, 
              Emotion_adjust_by: float, 
              data: Optional[Dict[str, Any]] = None,
              why: str = '',
              achieve: bool = False,
              priority: int = 1): 
        
        FRUSTRATION = 'frustration'
        self.subemotions['frustration'] += Emotion_adjust_by

        if data is not None:
            emotion = data.get('emotion', None)
            if not emotion:
                raise ValueError(f"missing emotion key: {data}") 
            data['emotion'] = {
                FRUSTRATION: {"regulation": np.zeros((4,4))}
            }
            
            """Emotions can vary. should look like this:
            
            [0.0 0.0 0.0 0.0] # top row focuses on emotion control (tenisty of this emotion), Responsible for high-level emotional control, decision-making, and rational thought.
            [0.0 0.0 0.0 0.0] # 2nd row focuses on physiological responses
            [0.0 0.0 0.0 0.0] # 3rd row focuses on facial expression (implement system for face plates in the future)
            [0.0 0.0 0.0 0.0] # Reward Circuitry, Involves the dopamine-rich ventral tegmental area and ventral striatum. # forebrain feature 
            """
            if priority == 1:
                matter = 1.0
            elif priority == 2:
                matter = 0.5
            elif priority == 3:
                matter = 0.25
            else:
                raise ValueError(f"Priority ({priority}) is invalid. Please choose from 1 - 2 - 3.")
            
            data['priority'] = {
                priority: matter
            }

            if why.strip() != '':
                data['why_this_feeling'] = why
            else: 
                data['why_this_feeling'] = """You feel this way for an unknown reason."""            

            if achieve:
                return data

    def rage(self, 
              Emotion_adjust_by: float, 
              data: Optional[Dict[str, Any]] = None,
              why: str = '',
              achieve: bool = False,
              priority: int = 1): 
        
        RAGE = 'rage'
        self.subemotions['rage'] += Emotion_adjust_by

        if data is not None:
            emotion = data.get('emotion', None)
            if not emotion:
                raise ValueError(f"missing emotion key: {data}") 
            data['emotion'] = {
                RAGE: {"regulation": np.zeros((4,4))}
            }
            
            """Emotions can vary. should look like this:
            
            [0.0 0.0 0.0 0.0] # top row focuses on emotion control (tenisty of this emotion), Responsible for high-level emotional control, decision-making, and rational thought.
            [0.0 0.0 0.0 0.0] # 2nd row focuses on physiological responses
            [0.0 0.0 0.0 0.0] # 3rd row focuses on facial expression (implement system for face plates in the future)
            [0.0 0.0 0.0 0.0] # Reward Circuitry, Involves the dopamine-rich ventral tegmental area and ventral striatum. # forebrain feature 
            """
            if priority == 1:
                matter = 1.0
            elif priority == 2:
                matter = 0.5
            elif priority == 3:
                matter = 0.25
            else:
                raise ValueError(f"Priority ({priority}) is invalid. Please choose from 1 - 2 - 3.")
            
            data['priority'] = {
                priority: matter
            }

            if why.strip() != '':
                data['why_this_feeling'] = why
            else: 
                data['why_this_feeling'] = """You feel this way for an unknown reason."""            

            if achieve:
                return data

    def irritation(self, 
              Emotion_adjust_by: float, 
              data: Optional[Dict[str, Any]] = None,
              why: str = '',
              achieve: bool = False,
              priority: int = 1): 
        
        IRRITATION = 'irritation'
        self.subemotions['rage'] += Emotion_adjust_by

        if data is not None:
            emotion = data.get('emotion', None)
            if not emotion:
                raise ValueError(f"missing emotion key: {data}") 
            data['emotion'] = {
                IRRITATION: {"regulation": np.zeros((4,4))}
            }
            
            """Emotions can vary. should look like this:
            
            [0.0 0.0 0.0 0.0] # top row focuses on emotion control (tenisty of this emotion), Responsible for high-level emotional control, decision-making, and rational thought.
            [0.0 0.0 0.0 0.0] # 2nd row focuses on physiological responses
            [0.0 0.0 0.0 0.0] # 3rd row focuses on facial expression (implement system for face plates in the future)
            [0.0 0.0 0.0 0.0] # Reward Circuitry, Involves the dopamine-rich ventral tegmental area and ventral striatum. # forebrain feature 
            """
            if priority == 1:
                matter = 1.0
            elif priority == 2:
                matter = 0.5
            elif priority == 3:
                matter = 0.25
            else:
                raise ValueError(f"Priority ({priority}) is invalid. Please choose from 1 - 2 - 3.")
            
            data['priority'] = {
                priority: matter
            }

            if why.strip() != '':
                data['why_this_feeling'] = why
            else: 
                data['why_this_feeling'] = """You feel this way for an unknown reason."""            

            if achieve:
                return data

    def resentment(self, 
              Emotion_adjust_by: float, 
              data: Optional[Dict[str, Any]] = None,
              why: str = '',
              achieve: bool = False,
              priority: int = 1): 
        
        RESENTMENT = 'resentment'
        self.subemotions['resentment'] += Emotion_adjust_by

        if data is not None:
            emotion = data.get('emotion', None)
            if not emotion:
                raise ValueError(f"missing emotion key: {data}") 
            data['emotion'] = {
                RESENTMENT: {"regulation": np.zeros((4,4))}
            }
            
            """Emotions can vary. should look like this:
            
            [0.0 0.0 0.0 0.0] # top row focuses on emotion control (tenisty of this emotion), Responsible for high-level emotional control, decision-making, and rational thought.
            [0.0 0.0 0.0 0.0] # 2nd row focuses on physiological responses
            [0.0 0.0 0.0 0.0] # 3rd row focuses on facial expression (implement system for face plates in the future)
            [0.0 0.0 0.0 0.0] # Reward Circuitry, Involves the dopamine-rich ventral tegmental area and ventral striatum. # forebrain feature 
            """
            if priority == 1:
                matter = 1.0
            elif priority == 2:
                matter = 0.5
            elif priority == 3:
                matter = 0.25
            else:
                raise ValueError(f"Priority ({priority}) is invalid. Please choose from 1 - 2 - 3.")
            
            data['priority'] = {
                priority: matter
            }

            if why.strip() != '':
                data['why_this_feeling'] = why
            else: 
                data['why_this_feeling'] = """You feel this way for an unknown reason."""            

            if achieve:
                return data

    def increase(self, amount: float):
        """Increase overall happiness."""
        self.level = min(10.0, self.level + amount)
    
    def decrease(self, amount: float):
        """Decrease overall happiness."""
        self.level = max(0.0, self.level - amount)
    
    def get_level(self) -> float:
        """Current happiness intensity."""
        return self.level
    
    
    def get_keywords(self) -> List[str]:
        return [
            'angry', 'anger', 'mad',
            'frustrated', 'frustration',
            'furious', 'rage',
            'irritated', 'irritation',
            'resentful', 'resentment'
        ]

    def __repr__(self) -> str:
        return f"""Angry=[{self.subclass}]"""


class Fear(Emotion):
    def __init__(self):
        super().__init__("Fear")

        self.subclass: List[str] = self.get_keywords()
        
        self.level: float = 0.0

        self.subemotions = {
            'anxiety': 0.0,
            'panic': 0.0,
            'worry': 0.0,
            'dread': 0.0
        }

    def _feeling_fear(self, data: Dict) -> bool:
        
        yes_or_not = data['emotion']
        if not yes_or_not or yes_or_not == None:
            raise ValueError(f"Data ({data}) is wrong, please insert valid data.")
        if yes_or_not not in self.subclass:
            return False
        return True
    
    def anxiety(self, 
              Emotion_adjust_by: float, 
              data: Optional[Dict[str, Any]] = None,
              why: str = '',
              achieve: bool = False,
              priority: int = 1): 
        
        ANXIETY = 'anxiety'
        self.subemotions['anxiety'] += Emotion_adjust_by

        if data is not None:
            emotion = data.get('emotion', None)
            if not emotion:
                raise ValueError(f"missing emotion key: {data}") 
            data['emotion'] = {
                ANXIETY: {"regulation": np.zeros((4,4))}
            }
            
            """Emotions can vary. should look like this:
            
            [0.0 0.0 0.0 0.0] # top row focuses on emotion control (tenisty of this emotion), Responsible for high-level emotional control, decision-making, and rational thought.
            [0.0 0.0 0.0 0.0] # 2nd row focuses on physiological responses
            [0.0 0.0 0.0 0.0] # 3rd row focuses on facial expression (implement system for face plates in the future)
            [0.0 0.0 0.0 0.0] # Reward Circuitry, Involves the dopamine-rich ventral tegmental area and ventral striatum. # forebrain feature 
            """
            if priority == 1:
                matter = 1.0
            elif priority == 2:
                matter = 0.5
            elif priority == 3:
                matter = 0.25
            else:
                raise ValueError(f"Priority ({priority}) is invalid. Please choose from 1 - 2 - 3.")
            
            data['priority'] = {
                priority: matter
            }

            if why.strip() != '':
                data['why_this_feeling'] = why
            else: 
                data['why_this_feeling'] = """You feel this way for an unknown reason."""            

            if achieve:
                return data

    def panic(self, 
              Emotion_adjust_by: float, 
              data: Optional[Dict[str, Any]] = None,
              why: str = '',
              achieve: bool = False,
              priority: int = 1): 
        
        PANIC = 'panic'
        self.subemotions['panic'] += Emotion_adjust_by

        if data is not None:
            emotion = data.get('emotion', None)
            if not emotion:
                raise ValueError(f"missing emotion key: {data}") 
            data['emotion'] = {
                PANIC: {"regulation": np.zeros((4,4))}
            }
            
            """Emotions can vary. should look like this:
            
            [0.0 0.0 0.0 0.0] # top row focuses on emotion control (tenisty of this emotion), Responsible for high-level emotional control, decision-making, and rational thought.
            [0.0 0.0 0.0 0.0] # 2nd row focuses on physiological responses
            [0.0 0.0 0.0 0.0] # 3rd row focuses on facial expression (implement system for face plates in the future)
            [0.0 0.0 0.0 0.0] # Reward Circuitry, Involves the dopamine-rich ventral tegmental area and ventral striatum. # forebrain feature 
            """
            if priority == 1:
                matter = 1.0
            elif priority == 2:
                matter = 0.5
            elif priority == 3:
                matter = 0.25
            else:
                raise ValueError(f"Priority ({priority}) is invalid. Please choose from 1 - 2 - 3.")
            
            data['priority'] = {
                priority: matter
            }

            if why.strip() != '':
                data['why_this_feeling'] = why
            else: 
                data['why_this_feeling'] = """You feel this way for an unknown reason."""            

            if achieve:
                return data

    def worry(self, 
              Emotion_adjust_by: float, 
              data: Optional[Dict[str, Any]] = None,
              why: str = '',
              achieve: bool = False,
              priority: int = 1): 
        
        WORRIED = 'worry'
        self.subemotions['worry'] += Emotion_adjust_by

        if data is not None:
            emotion = data.get('emotion', None)
            if not emotion:
                raise ValueError(f"missing emotion key: {data}") 
            data['emotion'] = {
                WORRIED: {"regulation": np.zeros((4,4))}
            }
            
            """Emotions can vary. should look like this:
            
            [0.0 0.0 0.0 0.0] # top row focuses on emotion control (tenisty of this emotion), Responsible for high-level emotional control, decision-making, and rational thought.
            [0.0 0.0 0.0 0.0] # 2nd row focuses on physiological responses
            [0.0 0.0 0.0 0.0] # 3rd row focuses on facial expression (implement system for face plates in the future)
            [0.0 0.0 0.0 0.0] # Reward Circuitry, Involves the dopamine-rich ventral tegmental area and ventral striatum. # forebrain feature 
            """
            if priority == 1:
                matter = 1.0
            elif priority == 2:
                matter = 0.5
            elif priority == 3:
                matter = 0.25
            else:
                raise ValueError(f"Priority ({priority}) is invalid. Please choose from 1 - 2 - 3.")
            
            data['priority'] = {
                priority: matter
            }

            if why.strip() != '':
                data['why_this_feeling'] = why
            else: 
                data['why_this_feeling'] = """You feel this way for an unknown reason."""            

            if achieve:
                return data

    def dread(self, 
              Emotion_adjust_by: float, 
              data: Optional[Dict[str, Any]] = None,
              why: str = '',
              achieve: bool = False,
              priority: int = 1): 
        
        DREAD = 'dread'
        self.subemotions['dread'] += Emotion_adjust_by

        if data is not None:
            emotion = data.get('emotion', None)
            if not emotion:
                raise ValueError(f"missing emotion key: {data}") 
            data['emotion'] = {
                DREAD: {"regulation": np.zeros((4,4))}
            }
            
            """Emotions can vary. should look like this:
            
            [0.0 0.0 0.0 0.0] # top row focuses on emotion control (tenisty of this emotion), Responsible for high-level emotional control, decision-making, and rational thought.
            [0.0 0.0 0.0 0.0] # 2nd row focuses on physiological responses
            [0.0 0.0 0.0 0.0] # 3rd row focuses on facial expression (implement system for face plates in the future)
            [0.0 0.0 0.0 0.0] # Reward Circuitry, Involves the dopamine-rich ventral tegmental area and ventral striatum. # forebrain feature 
            """
            if priority == 1:
                matter = 1.0
            elif priority == 2:
                matter = 0.5
            elif priority == 3:
                matter = 0.25
            else:
                raise ValueError(f"Priority ({priority}) is invalid. Please choose from 1 - 2 - 3.")
            
            data['priority'] = {
                priority: matter
            }

            if why.strip() != '':
                data['why_this_feeling'] = why
            else: 
                data['why_this_feeling'] = """You feel this way for an unknown reason."""            

            if achieve:
                return data
            
    def increase(self, amount: float):
        """Increase overall happiness."""
        self.level = min(10.0, self.level + amount)
    
    def decrease(self, amount: float):
        """Decrease overall happiness."""
        self.level = max(0.0, self.level - amount)
    
    def get_level(self) -> float:
        """Current happiness intensity."""
        return self.level
    def get_keywords(self) -> List[str]:
        return [
            'fearful', 'fear', 'afraid', 'scared',
            'anxious', 'anxiety',
            'panicked', 'panic',
            'worried', 'worry',
            'dreadful', 'dread'
        ]

    def __repr__(self) -> str:
        return f"""Fear=[{self.subclass}]"""


class Surprise(Emotion):
    def __init__(self):
        super().__init__("Surprise")

        self.subclass: List[str] = self.get_keywords()
        
        self.level: float = 0.0

        self.subemotions = {
            'shock': 0.0,
            'amazement': 0.0,
            'confusion': 0.0,
            'curiosity': 0.0
        }

    def _feeling_surprised(self, data: Dict) -> bool:
        
        yes_or_not = data['emotion']
        if not yes_or_not or yes_or_not == None:
            raise ValueError(f"Data ({data}) is wrong, please insert valid data.")
        if yes_or_not not in self.subclass:
            return False
        return True
    def shock(self, 
              Emotion_adjust_by: float, 
              data: Optional[Dict[str, Any]] = None,
              why: str = '',
              achieve: bool = False,
              priority: int = 1): 
        
        SHOCK = 'shock'
        self.subemotions['shock'] += Emotion_adjust_by

        if data is not None:
            emotion = data.get('emotion', None)
            if not emotion:
                raise ValueError(f"missing emotion key: {data}") 
            data['emotion'] = {
                SHOCK: {"regulation": np.zeros((4,4))}
            }
            
            """Emotions can vary. should look like this:
            
            [0.0 0.0 0.0 0.0] # top row focuses on emotion control (tenisty of this emotion), Responsible for high-level emotional control, decision-making, and rational thought.
            [0.0 0.0 0.0 0.0] # 2nd row focuses on physiological responses
            [0.0 0.0 0.0 0.0] # 3rd row focuses on facial expression (implement system for face plates in the future)
            [0.0 0.0 0.0 0.0] # Reward Circuitry, Involves the dopamine-rich ventral tegmental area and ventral striatum. # forebrain feature 
            """
            if priority == 1:
                matter = 1.0
            elif priority == 2:
                matter = 0.5
            elif priority == 3:
                matter = 0.25
            else:
                raise ValueError(f"Priority ({priority}) is invalid. Please choose from 1 - 2 - 3.")
            
            data['priority'] = {
                priority: matter
            }

            if why.strip() != '':
                data['why_this_feeling'] = why
            else: 
                data['why_this_feeling'] = """You feel this way for an unknown reason."""            

            if achieve:
                return data

    def amazement(self, Emotion_adjust_by: float):
        # TODO
        pass

    def confusion(self, Emotion_adjust_by: float):
        # TODO
        pass

    def curiosity(self, Emotion_adjust_by: float):
        # TODO
        pass
    def increase(self, amount: float):
        """Increase overall happiness."""
        self.level = min(10.0, self.level + amount)
    
    def decrease(self, amount: float):
        """Decrease overall happiness."""
        self.level = max(0.0, self.level - amount)
    
    def get_level(self) -> float:
        """Current happiness intensity."""
        return self.level
    
    def get_keywords(self) -> List[str]:
        return [
            'surprised', 'surprise',
            'shocked', 'shock',
            'amazed', 'amazement',
            'confused', 'confusion',
            'curious', 'curiosity'
        ]
    def __repr__(self) -> str:
        return f"""Surprise=[{self.subclass}]"""


class Disgust(Emotion):
    def __init__(self):
        super().__init__("Disgust")

        self.subclass: List[str] = self.get_keywords()

        self.level: float = 0.0

        self.subemotions = {
            'revulsion': 0.0,
            'contempt': 0.0,
            'aversion': 0.0,
            'disapproval': 0.0
        }

    def _feeling_disgust(self, data: Dict) -> bool:
        yes_or_not = data['emotion']
        if not yes_or_not or yes_or_not == None:
            raise ValueError(f"Data ({data}) is wrong, please insert valid data.")
        if yes_or_not not in self.subclass:
            return False
        return True
    
    def revulsion(self, 
              Emotion_adjust_by: float, 
              data: Optional[Dict[str, Any]] = None,
              why: str = '',
              achieve: bool = False,
              priority: int = 1): 
        
        REVULSION = 'revulsion'
        self.subemotions['revulsion'] += Emotion_adjust_by

        if data is not None:
            emotion = data.get('emotion', None)
            if not emotion:
                raise ValueError(f"missing emotion key: {data}") 
            data['emotion'] = {
                REVULSION: {"regulation": np.zeros((4,4))}
            }
            
            """Emotions can vary. should look like this:
            
            [0.0 0.0 0.0 0.0] # top row focuses on emotion control (tenisty of this emotion), Responsible for high-level emotional control, decision-making, and rational thought.
            [0.0 0.0 0.0 0.0] # 2nd row focuses on physiological responses
            [0.0 0.0 0.0 0.0] # 3rd row focuses on facial expression (implement system for face plates in the future)
            [0.0 0.0 0.0 0.0] # Reward Circuitry, Involves the dopamine-rich ventral tegmental area and ventral striatum. # forebrain feature 
            """
            if priority == 1:
                matter = 1.0
            elif priority == 2:
                matter = 0.5
            elif priority == 3:
                matter = 0.25
            else:
                raise ValueError(f"Priority ({priority}) is invalid. Please choose from 1 - 2 - 3.")
            
            data['priority'] = {
                priority: matter
            }

            if why.strip() != '':
                data['why_this_feeling'] = why
            else: 
                data['why_this_feeling'] = """You feel this way for an unknown reason."""            

            if achieve:
                return data

    def contempt(self, 
              Emotion_adjust_by: float, 
              data: Optional[Dict[str, Any]] = None,
              why: str = '',
              achieve: bool = False,
              priority: int = 1): 
        
        CONTEMPT = 'contempt'
        self.subemotions['rage'] += Emotion_adjust_by

        if data is not None:
            emotion = data.get('emotion', None)
            if not emotion:
                raise ValueError(f"missing emotion key: {data}") 
            data['emotion'] = {
                CONTEMPT: {"regulation": np.zeros((4,4))}
            }
            
            """Emotions can vary. should look like this:
            
            [0.0 0.0 0.0 0.0] # top row focuses on emotion control (tenisty of this emotion), Responsible for high-level emotional control, decision-making, and rational thought.
            [0.0 0.0 0.0 0.0] # 2nd row focuses on physiological responses
            [0.0 0.0 0.0 0.0] # 3rd row focuses on facial expression (implement system for face plates in the future)
            [0.0 0.0 0.0 0.0] # Reward Circuitry, Involves the dopamine-rich ventral tegmental area and ventral striatum. # forebrain feature 
            """
            if priority == 1:
                matter = 1.0
            elif priority == 2:
                matter = 0.5
            elif priority == 3:
                matter = 0.25
            else:
                raise ValueError(f"Priority ({priority}) is invalid. Please choose from 1 - 2 - 3.")
            
            data['priority'] = {
                priority: matter
            }

            if why.strip() != '':
                data['why_this_feeling'] = why
            else: 
                data['why_this_feeling'] = """You feel this way for an unknown reason."""            

            if achieve:
                return data

    def aversion(self, 
              Emotion_adjust_by: float, 
              data: Optional[Dict[str, Any]] = None,
              why: str = '',
              achieve: bool = False,
              priority: int = 1): 
        
        AVERSION = 'aversion'
        self.subemotions['aversion'] += Emotion_adjust_by

        if data is not None:
            emotion = data.get('emotion', None)
            if not emotion:
                raise ValueError(f"missing emotion key: {data}") 
            data['emotion'] = {
                AVERSION: {"regulation": np.zeros((4,4))}
            }
            
            """Emotions can vary. should look like this:
            
            [0.0 0.0 0.0 0.0] # top row focuses on emotion control (tenisty of this emotion), Responsible for high-level emotional control, decision-making, and rational thought.
            [0.0 0.0 0.0 0.0] # 2nd row focuses on physiological responses
            [0.0 0.0 0.0 0.0] # 3rd row focuses on facial expression (implement system for face plates in the future)
            [0.0 0.0 0.0 0.0] # Reward Circuitry, Involves the dopamine-rich ventral tegmental area and ventral striatum. # forebrain feature 
            """
            if priority == 1:
                matter = 1.0
            elif priority == 2:
                matter = 0.5
            elif priority == 3:
                matter = 0.25
            else:
                raise ValueError(f"Priority ({priority}) is invalid. Please choose from 1 - 2 - 3.")
            
            data['priority'] = {
                priority: matter
            }

            if why.strip() != '':
                data['why_this_feeling'] = why
            else: 
                data['why_this_feeling'] = """You feel this way for an unknown reason."""            

            if achieve:
                return data

    def disapproval(self, 
              Emotion_adjust_by: float, 
              data: Optional[Dict[str, Any]] = None,
              why: str = '',
              achieve: bool = False,
              priority: int = 1): 
        
        DISAPPROVAL = 'disapproval'
        self.subemotions['disapproval'] += Emotion_adjust_by

        if data is not None:
            emotion = data.get('emotion', None)
            if not emotion:
                raise ValueError(f"missing emotion key: {data}") 
            data['emotion'] = {
                DISAPPROVAL: {"regulation": np.zeros((4,4))}
            }
            
            """Emotions can vary. should look like this:
            
            [0.0 0.0 0.0 0.0] # top row focuses on emotion control (tenisty of this emotion), Responsible for high-level emotional control, decision-making, and rational thought.
            [0.0 0.0 0.0 0.0] # 2nd row focuses on physiological responses
            [0.0 0.0 0.0 0.0] # 3rd row focuses on facial expression (implement system for face plates in the future)
            [0.0 0.0 0.0 0.0] # Reward Circuitry, Involves the dopamine-rich ventral tegmental area and ventral striatum. # forebrain feature 
            """
            if priority == 1:
                matter = 1.0
            elif priority == 2:
                matter = 0.5
            elif priority == 3:
                matter = 0.25
            else:
                raise ValueError(f"Priority ({priority}) is invalid. Please choose from 1 - 2 - 3.")
            
            data['priority'] = {
                priority: matter
            }

            if why.strip() != '':
                data['why_this_feeling'] = why
            else: 
                data['why_this_feeling'] = """You feel this way for an unknown reason."""            

            if achieve:
                return data

    def increase(self, amount: float):
        """Increase overall happiness."""
        self.level = min(10.0, self.level + amount)
    
    def decrease(self, amount: float):
        """Decrease overall happiness."""
        self.level = max(0.0, self.level - amount)
    
    def get_level(self) -> float:
        """Current happiness intensity."""
        return self.level
    
    def get_keywords(self) -> List[str]:
        return [
            'disgusted', 'disgust',
            'revolted', 'revulsion',
            'contempt', 'contemptuous',
            'aversion',
            'disapproval', 'disapproving'
        ]
    
    def __repr__(self) -> str:
        return f"""Disgust=[{self.subclass}]"""


class RileyAnderson:
    
    def __init__(self):
        """SET OF EMOTIONS
        Happy, 
        Angry, 
        Sad, 
        Fear, 
        Surprise, 
        Disgust
        """

        self.Joy = Joy()
        """
        Includes different subemotions of Happiness
        """

        self.Anger = Anger()
        """
        Includes different subemotions of Anger
        """

        self.Disgust = Disgust()
        """
        Includes different subemotions of Disgust
        """
        self.Sadness = Sadness()
        """
        Includes different subemotions of Sadness
        """
        self.Fear = Fear()
        """
        Includes different subemotions of Fear
        """

        self.Surprise = Surprise()
        """
        Includes different subemotions of Surprise
        """

        self.emotions = [
            self.Joy, self.Sadness, self.Anger,
            self.Fear, self.Disgust, self.Surprise
        ]
    def emotion_query(self, data: Dict[str, str]):
        if self.Joy._feeling_happy(data):
            test = self.Joy.happy_keyword_query(emotion=data['emotion'], data=data)
        elif self.Anger._feeling_angry(data):
            pass
        elif self.Sadness._feeling_upset(data):
            pass
        elif self.Disgust._feeling_disgust(data):
            pass
        elif self.Surprise._feeling_surprised(data):
            pass
        elif self.Fear._feeling_fear(data):
            pass
        else:
            raise RuntimeError("Data doesn't fit any emotions, please double check.")
        return test

    def detect_emotion(self, emotion_word: str) -> Optional[Emotion]:
        """Figure out which emotion category this word belongs to."""
        for emotion in self.emotions:
            if emotion.matches(emotion_word):
                return emotion
        return None  # Neutral/unknown
    
    def get_dominant_emotion(self) -> Emotion:
        """Which emotion is currently strongest."""
        return max(self.emotions, key=lambda e: e.level)
    
    def get_mood(self) -> Dict[str, float]:
        """Current emotional state across all emotions."""
        return {e.name: e.level for e in self.emotions}
    
    def regulate(self):
        """Emotions decay over time (return to baseline)."""
        for emotion in self.emotions:
            emotion.level *= 0.95  # 5% decay
    
    def __repr__(self) -> str:
        mood = self.get_mood()
        return f"EmotionSystem({mood})"

"""(Happy, 
    Angry, 
    Sad, 
    Fear, 
    Surprise, 
    Disgust)"""

if __name__ == '__main__':
    pass
   