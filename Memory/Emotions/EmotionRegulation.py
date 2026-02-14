import numpy as np


class EmotionRegulation:
    """
    Models emotion as distributed brain system.
    Based on actual neuroscience.
    """
    
    def __init__(self, emotion_type: str):
        self.emotion_type = emotion_type
        
        # 4x4 matrix: [prefrontal, physiological, expression, reward]
        self.state = np.zeros((4, 4))
        
        # Initialize based on emotion type
        self._initialize_baseline()
    
    def _initialize_baseline(self):
        """Set baseline values for this emotion."""
        
        baselines = {
            'pride': {
                'reward_value': 0.8,       # Positive outcome
                'approach_tendency': 0.9,  # Want more
                'arousal': 0.6,           # Energized
                'energy': 0.8             # Energizing emotion
            },
            'shame': {
                'reward_value': 0.2,
                'approach_tendency': 0.1,  # Avoid
                'arousal': 0.5,
                'energy': 0.3              # Draining
            },
            'fear': {
                'reward_value': 0.1,       # Threat
                'approach_tendency': 0.0,  # Strong avoid
                'arousal': 0.9,            # High activation
                'energy': 0.4              # Draining but mobilizing
            },
            'joy': {
                'reward_value': 0.9,
                'approach_tendency': 0.9,
                'arousal': 0.7,
                'energy': 0.9
            }
        }
        
        baseline = baselines.get(self.emotion_type, {})
        
        # Set reward row
        self.state[3, 0] = baseline.get('reward_value', 0.5)
        self.state[3, 3] = baseline.get('approach_tendency', 0.5)
        
        # Set physiological row
        self.state[1, 0] = baseline.get('arousal', 0.5)
        self.state[1, 3] = baseline.get('energy', 0.5)
    
    def trigger(self, intensity: float, context: dict):
        """
        Trigger emotion with given intensity.
        Context affects how it manifests.
        """
        
        # Update prefrontal (cognitive layer)
        self.state[0, 0] = intensity  # Current intensity
        self.state[0, 2] = context.get('reappraisal', 0.5)  # Can you reframe it?
        
        # Update physiological
        self.state[1, 0] = intensity * 0.8  # Arousal tracks intensity
        self.state[1, 1] = 0.5 + intensity * 0.3  # Heart rate
        
        # Update expression
        social_context = context.get('social', True)
        if social_context:
            self.state[2, 0] = intensity * 0.7  # Show it on face
            self.state[2, 3] = intensity * 0.8  # Social signaling
        else:
            self.state[2, 0] = intensity * 0.3  # Suppress expression
            self.state[2, 3] = intensity * 0.2
    
    def regulate(self, strategy: str):
        """
        Apply emotion regulation strategy.
        """
        
        if strategy == 'reappraisal':
            # Cognitive reframing reduces intensity
            self.state[0, 1] = 0.8  # High regulation
            self.state[0, 0] *= 0.7  # Reduce intensity
        
        elif strategy == 'suppression':
            # Hide expression but intensity remains
            self.state[0, 3] = 0.9  # High inhibition
            self.state[2, :] *= 0.3  # Reduce all expression
        
        elif strategy == 'acceptance':
            # Allow emotion without fighting it
            self.state[0, 1] = 0.3  # Low regulation
            self.state[1, 3] += 0.1  # Less energy drain
    
    def update(self, time_step: float = 0.1):
        """
        Run one time step of emotion dynamics.
        Emotions change over time based on interactions.
        """
        self.state = self.emotion_dynamics(emotion_matrix=self.state, time_step=time_step)
    
    def get_state(self) -> dict:
        """Get human-readable state."""
        return {
            'intensity': self.state[0, 0],
            'regulation': self.state[0, 1],
            'arousal': self.state[1, 0],
            'energy': self.state[1, 3],
            'expression': self.state[2, 3],
            'reward_value': self.state[3, 0],
            'approach': self.state[3, 3]
        }
    
    def to_dict(self) -> dict:
        """For JSON storage."""
        return {
            'regulation': self.state  # numpy array
        }


    def emotion_dynamics(self, emotion_matrix: np.ndarray, time_step: float) -> np.ndarray:
        """
        Emotions are dynamic - each row influences the others.
        This models how they interact over time.
        """
        
        # Unpack current state
        prefrontal = emotion_matrix[0]  # Row 0
        physiological = emotion_matrix[1]  # Row 1
        expression = emotion_matrix[2]  # Row 2
        reward = emotion_matrix[3]  # Row 3
        
        # === INTERACTIONS ===
        
        # 1. Physiological arousal makes regulation harder
        # High arousal → harder to control
        regulation_difficulty = 1.0 - physiological[0] * 0.5
        prefrontal[1] *= regulation_difficulty
        
        # 2. Strong regulation reduces expression
        # If you're holding back, less shows externally
        expression[3] *= (1.0 - prefrontal[3] * 0.3)  # Inhibition reduces social signal
        
        # 3. Reward value influences arousal
        # Positive outcomes energize, negative ones drain
        if reward[0] > 0.5:
            physiological[3] += 0.1  # Gain energy
        else:
            physiological[3] -= 0.1  # Lose energy
        
        # 4. Prediction errors drive arousal
        # Surprises (positive or negative) increase activation
        arousal_boost = abs(reward[2]) * 0.2
        physiological[0] += arousal_boost
        
        # 5. Facial expression provides feedback (facial feedback hypothesis)
        # Smiling makes you happier, frowning makes you sadder
        if expression[0] > 0.7:
            prefrontal[0] += 0.05  # Expressing intensifies feeling
        
        # 6. Energy depletion reduces regulation capacity
        # Tired → less self-control
        if physiological[3] < 0.3:
            prefrontal[1] *= 0.7  # Weakened regulation
        
        # Clamp values
        emotion_matrix = np.clip(emotion_matrix, 0.0, 1.0)
        
        return emotion_matrix