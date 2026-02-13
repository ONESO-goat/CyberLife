from BrainAnomaly.BrainAnomaly import Brain
from Memory.memory_systems import CyberMemory, EmotionalCalling
from Memory.Emotions.Inside_out import RileyAnderson


if __name__ == "__main__":
    
    import sys
    print(sys.path)
    
    print("="*60)
    print("CYBERLIFE BRAIN SYSTEM - COMPREHENSIVE TEST")
    print("="*60)

    
    #print(f"Brain now: {B.showcase}")


    

    # Test 2: Add memories with helper method
    print("\n[TEST 2] Storing memories...")
    test_memories = [
        ("I am coding!", "happy", 0.5)
    ]
     # Create brain with emotions
    brain = Brain(name="Riley", pounds=3.0, watts=20.0)
    emotions = RileyAnderson()
    memory_system = EmotionalCalling(brain.mind, brain, emotions)
    print(f"✓ Created: {brain}\n")
    print(f"Name: {brain.achieve_name()}\n")

    # Store emotional memory
    memory_system.encode_memory(
        content="First day at new school",
        emotion_data={'emotion': 'nervous', 'intensity': 0.8}
    )

    # Emotion levels update
    print(emotions.Fear.level)  # Increased because "nervous" matches Fear

    # Recall based on mood
    current_mood = emotions.get_dominant_emotion().name.lower()
    relevant_memories = memory_system.emotional_recall(current_mood)

    # Regulate emotions over time
    emotions.regulate()  # Fee
    
            
