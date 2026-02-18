from BrainAnomaly.BrainAnomaly import Brain
from Memory.memory_systems import CyberMemory, EmotionalCalling
import numpy as np
from Memory.Emotions.Inside_out import RileyAnderson
from Memory.Emotions.Headquarters import Prefrontal_Control, Headquarters
import random

if __name__ == "__main__":
    
    import sys
    print(sys.path)
    
    print("="*60)
    print("CYBERLIFE BRAIN SYSTEM - COMPREHENSIVE TEST")
    print("="*60)

    
    #print(f"Brain now: {B.showcase}")

     # Create brain with emotions
    brain = Brain(name="Test", pounds=3.0, watts=20.0)
    emotions = RileyAnderson()
    memory_system = EmotionalCalling(brain.mind, brain, emotions)
    print(f"✓ Created: {brain}\n")
    print(f"Name: {brain.achieve_name()}\n")
    random_content = [
        "I just finished my big game and made alot of friends doing so.",
        "I just finished the final boss fight!",
        "I finally reached rank diamond in overwatch!",
        "I will be attending college soon.",
        "Coding is the best thing to ever exist!",
        "I have been listening to music all day and that makes me proud!",
        "I was able to speak my mind the other day!",
        "We are finally reaching break! finally am I right!",
        "I am going to intern for a drone competeion",
        "My math skills are improving at a great pace",
        "I just completed my first marathon and it feels amazing!",
        "I finally built my first PC by myself!",
        "I passed my driving test on the first try!",
        "I just submitted my biggest project of the year!",
        "I reached 10,000 followers today!",
        "I learned how to cook a brand new recipe!",
        "I finally cleaned my entire room!",
        "I finished reading a whole book in one day!",
        "I started going to the gym consistently!",
        "I just got accepted into my dream program!",
        "I solved a problem that had me stuck for hours!",
        "I made a new friend today!",
        "I improved my personal best time in running!",
        "I organized my schedule and feel super productive!",
        "I tried something new today and loved it!",
        "I finally understand that topic in math!",
        "I woke up early and actually felt energized!",
        "I practiced coding and built something cool!",
        "I stepped out of my comfort zone today!",
        "I stayed consistent with my goals this week!"
    ]
    randomTen = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]
    content = random.choice(random_content)
    inten = random.choice(randomTen)
    stuff = {
        'emotion': 'proud',
        'intensity': inten
    }
    # Store emotional memory
    memory_system.encode_memory(
        content=content,
        emotion_data=stuff
    )

    print("Working with rows...\n")
    hq = Headquarters(memories=brain.mind.get_all(), Brain=brain)
    
    id = '5277aecf-113d-40cd-a61c-743e76ff7314'
    
    hq.focus(id=id)
    print(f"EXISTS CHECK: {brain.mind.exists(id=id)}")
    chosen_memory = brain.mind.find(id=id)
    print(f'CURRENT MEMORY: {chosen_memory}\n')
    test = brain.mind.read_numpy(id=id)
    print(f"CURRENT NUMPY READING: {test}\n")
    
    adjust = hq.ROW1.adjust(by=0.5)
    print(f"NEW CURRENT NUMPY: {adjust}\n")
    actually_worked = brain.mind.read_numpy(id=id)
    print(f"UPDATED?: {actually_worked}\n")
    print(f"STORAGE: {len(brain.mind.get_all())}/{brain.mind.get_capacity()}")
    

    

