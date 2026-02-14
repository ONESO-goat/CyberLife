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
    content = "I just finished my big game and made alot of friends doing so."
    stuff = {
        'emotion': 'proud',
        'intensity': 0.8
    }
    # Store emotional memory
    memory_system.encode_memory(
        content=content,
        emotion_data=stuff
    )
    
    
            
