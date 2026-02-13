# Inside_out.py


from typing import Dict, List, Any, Optional

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

        self.subclass: List[str] = self.get_keywords()

        self.level: float = 0.0

        self.subemotions = {
            'joy': 0.0,
            'excitement': 0.0,
            'contentment': 0.0,
            'pride': 0.0
        }

    def _feeling_happy(self, data: Dict) -> bool:

        
        yes_or_not = data['emotion']
        if not yes_or_not or yes_or_not == None:
            raise ValueError(f"\nData ({data}) is wrong, please insert valid data; make sure key is 'emotion' without a 's'")
        if yes_or_not not in self.subclass:
            return False
        return True
    
    def joy(self, Emotion_adjust_by: float):

        # TODO
        pass

    def excitement(self, Emotion_adjust_by: float):
        # TODO
        pass

    def contentment(self, Emotion_adjust_by: float):
        # TODO
        pass

    def pride(self, Emotion_adjust_by: float):
        # TODO
        pass

    def get_keywords(self) -> List[str]:
        return [
            'happy', 'joyful', 'joy',
            'excited', 'excitement',
            'content', 'contentment',
            'proud', 'pride', 'prideful'
        ]
    
    def __repr__(self) -> str:
        return f"""Happy=[{self.subclass}]"""


class Sadness(Emotion):
    def __init__(self):
        super().__init__("Sadness")
        self.subclass = ['upset', 'disappointed', 'grief', 'loneliness']
        
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
        if yes_or_not not in self.subclass:
            return False
        return True

    def upset(self, Emotion_adjust_by: float):
        # TODO
        pass

    def disappointment(self, Emotion_adjust_by: float):
        # TODO
        pass

    def grief(self, Emotion_adjust_by: float):
        # TODO
        pass

    def loneliness(self, Emotion_adjust_by: float):
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
            'sad', 'sadness',
            'upset',
            'disappointed', 'disappointment',
            'grief', 'grieving',
            'lonely', 'loneliness'
        ]
    
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
    
    def frustration(self, Emotion_adjust_by: float):
        # TODO
        pass

    def rage(self, Emotion_adjust_by: float):
        # TODO
        pass

    def irritation(self, Emotion_adjust_by: float):
        # TODO
        pass

    def resentment(self, Emotion_adjust_by: float):
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
    
    def anxiety(self, Emotion_adjust_by: float):
        # TODO
        pass

    def panic(self, Emotion_adjust_by: float):
        # TODO
        pass

    def worry(self, Emotion_adjust_by: float):
        # TODO
        pass

    def dread(self, Emotion_adjust_by: float):
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
    def shock(self, Emotion_adjust_by: float):
        # TODO
        pass

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
    
    def revulsion(self, Emotion_adjust_by: float):
        # TODO
        pass

    def contempt(self, Emotion_adjust_by: float):
        # TODO
        pass

    def aversion(self, Emotion_adjust_by: float):
        # TODO
        pass

    def disapproval(self, Emotion_adjust_by: float):
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
   