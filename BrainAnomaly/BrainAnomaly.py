
import numpy as np
import importlib as lib
import sys
import os
from datetime import datetime
import matplotlib.pyplot as plt
from typing import Any, Tuple, Dict, List
import json_numpy as J
from pathlib import Path
from matplotlib.patches import Circle


"""
CyberLife Brain Architecture:

CURRENT (v0.1):
- Physical brain structure (size, power constraints)
- JSON-based memory storage
- Basic visualization

PLANNED (v0.2-0.5):
- Brain region systems (Prosencephalon, Mesencephalon, etc.)
- Inter-region communication
- Activation dynamics
- Neural database for state persistence

FUTURE (v1.0+):
- Spiking neural networks within regions
- Neurotransmitter simulation
- Learning/plasticity mechanisms
- Full brain-like behavior emergence
"""

class BrainAnomaly():
    """
    The Brain can come in different shapes. 
    Rats brains being only 2 grams.
    Humans brains being 3 pounds.
    Sperm whales brains being 20 pounds. 
    
    Create a "brain" that determines speed, personity, and other factors.
    """

    def __init__(self, pounds=0.005, watts = 1.0):
        """
        Docstring for __init__
        
        :param pounds: Size of the brain. smallest being 0.005, highest around 20

        :param power: how much brain power being seeked after
        :type power: float
        """
        if not 0.005 <= pounds <= 20.0:
            raise ValueError(f"Inputed Brain Width ({pounds}) falls outside range of (0.005 - 20.0)")
        if not 1.0 <= watts <= 100.0:
            raise ValueError(f"Inputed Watts ({watts}) falls outside range of (1.0 - 100.0)")
        
        self.brain_size = pounds
        self.power = watts

        # Avoid tedious work to manually changing size if program scales
        self.max = 20
        self.mininum = 0.001

        #self.BrainCreation(size=self.brain_size, watts=self.power)

    def resize(self, to: int | float):
        """Resize the brain. Change it from 100 down to 10, etc"""
        if to is None:
            raise ValueError("Arg cannot be None.")
        
        if to > self.max:
            raise ValueError(f"Args ({to}) extends max limit of {self.max}.")
        
        elif to < self.mininum:
            raise ValueError(f"Valid limit is {self.mininum} but Args is: {to}.")
        
        elif to == self.brain_size:
            raise ValueError(f"Brain size is already chosen size.")
        self.brain_size = to
        #self.BrainCreation(size=self.brain_size, watts=self.power)

    def reduce(self, by: float=1.0):

        f"""Decrease the power of watts, currently sits at {self.power}"""
        # watts fall around 1.0 to 100.0, anything higher will be invalid
        
        if self.power == 1.0:
            raise ValueError("Power already lowest limit (1.0)")
        
        # decrease power by called amount 
        self.power = self.power - by
        self.power = max(1.0, min(self.power, 100.0))

    
    def increase(self, by: float = 1.0):
        f"""Increase the power of watts, currently sits at {self.power}"""
        # watts fall around 1.0 to 100.0, anything higher will be invalid
        
        if self.power == 100.0:
            raise ValueError("Power already highest limit (100.0).")
        
        # increase power by called amount 
        self.power = self.power + by



    def get_size(self) -> float:
        """Return the size of the brain"""
        return self.brain_size
    
    def get_power(self) -> float:
        """Return strengh of WATTS"""
        return self.power
    


class Brain(BrainAnomaly):
    def __init__(self, pounds: float = 0.005, watts: float = 1.0, name: str = 'bob', storage_size: int = 1000000):
        
        self._validate_name(name)

        super().__init__(pounds=pounds, watts=watts)

        # Fun little feature, name your 'brain'
        self.name: str = name.strip().capitalize()

        #self._create_config_()
        self.mind = Storage(self.get_brain_data(), size=storage_size)
        """Storage"""

                # Regional activation tracking (simple version)
        self.region_activity = {
            'forebrain': 0.0,
            'midbrain': 0.0,
            'hindbrain': 0.0
        }


        # Future systems (placeholders)
        # Uncomment when ready to implement:
        # self.forebrain = Prosencephalon(self)
        # self.midbrain = Mesencephalon(self)
        # self.hindbrain = Rhombencephalon(self)
        
    def _validate_name(self, name: str):
        """Validate Brain name"""
        special_chars = r"~!@#$%^&*()_+`-={}|[]\:;<>?,./'"  

        if not name or name.strip() == '':
            raise ValueError("Name cannot be empty")
             
        if any(char in special_chars for char in name):
            raise ValueError(f"Name cannot contain special characters: {special_chars}")
        

    def BrainCreation(self) -> Tuple[float, float, float]:
        """Create the size of the brain. 
        Grab input of pounds and watts to determine brain.
        Returns tuple for self.showcase"""

        size = self.brain_size
        watts_ = self.power

        forebrain = self.brain_size * 0.5
        midbrain = self.brain_size * 0.3
        hindbrain = self.brain_size * 0.2
        return forebrain, midbrain, hindbrain

    

    def get_brain_data(self) -> Dict[str, Any]:
        stuff = {
            "NAME": self.name,
            "WATTS": self.power,
            "SIZE": self.brain_size
        }
        return stuff
    

    def stimulate_region(self, region: str, intensity: float):
        """
        Activate a brain region.
        FUTURE: Will trigger actual neural processing.
        CURRENT: Just tracks activation levels.
        """
        if region not in self.region_activity:
            raise ValueError(f"Unknown region: {region}")
        
        self.region_activity[region] += intensity
        self.region_activity[region] = min(1.0, self.region_activity[region])
        
        # Activation decays over time
        for r in self.region_activity:
            if r != region:
                self.region_activity[r] *= 0.95
    
    def get_brain_state(self):
        """Current state of all regions."""
        return self.region_activity.copy()
    
    def showcase(self, mode: str = "2D") -> None:
        """Display brain visualization."""
        mode = mode.upper()
        
        if mode == '2D':
            self.render_visualize_brain_2D()
        elif mode == '3D':
            #self.render_visualize_brain_3D()  # Implement this later
            raise NotImplementedError("3D visual not yet made.")
        else:
            raise ValueError(f"Invalid mode: {mode}. Choose '2D' or '3D'")
        

    def render_visualize_brain_2D(self, 
                 figsize:tuple[int, int]=(7,7), 
                 border_color:str='black', 
                 _color:str='lightgray', 
                 shape: str = 'circle', 
                 Brain_Size:float= 1.0):
        """Show brain with memories represented."""
        import matplotlib.pyplot as plt
        import numpy as np
        from matplotlib.patches import Circle

        fig, ax = plt.subplots(figsize=figsize)
        ax.set_xlim(-2, 2)
        ax.set_ylim(-2, 2)
        ax.set_aspect('equal')
        ax.axis('off')
        
        # Brain outline
        brain_circle = Circle((0, 0), 1.5, 
                            color=_color, 
                            ec='darkgray', 
                            linewidth=3, 
                            alpha=0.3)
        ax.add_patch(brain_circle)
        
        # Each memory = dot inside brain
        memories = self.recall_all()
        
        emotion_colors = {
            'happy': 'gold',
            'sad': 'blue',
            'angry': 'red',
            'fearful': 'purple',
            'neutral': 'gray',
            'curious': 'green',
            'excited': 'orange'
        }
        
        for memory in memories:
            # Random position inside brain
            angle = np.random.uniform(0, 2 * np.pi)
            radius = np.random.uniform(0, 1.3)
            x = radius * np.cos(angle)
            y = radius * np.sin(angle)
            
            color = emotion_colors.get(memory['emotion'], 'gray')
            size = 50 + memory['importance'] * 100  # Size based on importance
            
            ax.scatter(x, y, s=size, c=color, alpha=0.7, edgecolors='black')
        
        plt.title(f"{self.name}'s Brain - {len(memories)} memories")
        plt.show()
    def remember(self, content: str, 
                 emotion: str = 'neutral', 
                 importance: float = 0.5, 
                    ) -> None:
        """Store a new memory."""
        memory = {
            'content': content,
            'emotion': emotion.lower(),
            'importance': importance,
            'motivation': np.array([
                [0.0, 0.0, 0.0],
                [0.0, 0.0, 0.0],
                [0.0, 0.0, 0.0]
            ]),
            'timestamp': datetime.now().isoformat()
        }
        self.mind.add(memory)
    
    def forget(self, memory_item: Dict[str, Any]) -> None:
        """Remove a memory."""
        self.mind.remove(memory_item)
    
    def get_memory_count(self) -> int:
        """How many memories are stored."""
        return len(self.mind.memories)
    
    def get_memories_by_emotion(self, emotion: str) -> List[Dict[str, Any]]:
        """Get all memories with specific emotion."""
        return [m for m in self.mind.memories if m.get('emotion') == emotion]
    def __repr__(self) -> str:
        return f"Brain(name='{self.name}', size={self.brain_size}lbs, power={self.power}W, memories={len(self.mind.memories)})"

    def _create_config_(self, auto_Activation: bool = False):
        """
        FUTURE IMPLEMENTATION:
        Creates persistent database for neural state tracking.
        
        Will store:
        - Synaptic weights (connection strengths between regions)
        - Neurotransmitter levels (dopamine, serotonin analogs)
        - Long-term potentiation (learning traces)
        - Regional activation patterns
        
        Currently creates basic SQLite structure.
        TODO: Integrate with actual neural simulation when regions are implemented.
        """
    
    # Current implementation (basic structure)
    
        import uuid
        import importlib as lib
        from pathlib import Path
        import os
        import sys
        
        try:
            
            id = str(uuid.uuid4())
            file = f"{self.name}_CONFIG.py" 
            path = Path(id) / Path(file)
            with open(file, 'w') as f:
                f.write(self._())
            if auto_Activation:
                lib.invalidate_caches()

                if os.getcwd() not in sys.path:
                    sys.path.append(os.getcwd())

                module = lib.import_module(file[:-3].strip())
                module.run()
                
        except IOError as e:
            raise IOError("There was an error creating brain database: ", e)
        
        # TODO: Add tables for:
        # - synaptic_connections
        # - neurotransmitter_levels  
        # - activation_history
        # - learning_traces
    
    def _(self) -> str:
        
        script = f"""
import sqlite3
import uuid
from datetime import datetime

def run():
    ID = "{self.name}"+str(uuid.uuid4())+datetime.utcnow().isoformat().strip()
    env = "{self.name}.env"
    script = "{self.name.upper()}_ID="+ID

    with open(env, 'w') as f:
        f.write(script)

    # Create database
    conn = sqlite3.connect("{self.name}_brain.db")
    cursor = conn.cursor()

    # Create table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS memories (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            content TEXT,
            emotion TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            importance FLOAT
        )
    ''')

    # Insert memory
    cursor.execute('''
        INSERT INTO memories (content, emotion, importance)
        VALUES (?, ?, ?)
    ''', ("First memory", "happy", 0.8))

    conn.commit()

    # Query memories
    cursor.execute('SELECT * FROM memories ORDER BY importance DESC')
    memories = cursor.fetchall()

    conn.close()

"""
        return script
    def achieve_name(self) -> str:
        return self.name
    
    def recall_all(self):
        """Get all memories."""
        return self.mind.get_all()

    
    
    
class Storage():
        """There will be a storage for this system as if too much data gets accepted, 
        it can crash and mess the system."""
        def __init__(self, system: Dict, size: int=1000000):
            self.watts: float = system["WATTS"]
            self.name: str = system["NAME"]
            self.brain_size: float = system["SIZE"]
            self.STORAGE_size = size
            
            self.name = self.name
            self.brain_dir = Path(f'brains/{self.name}')
            self.brain_dir.mkdir(parents=True, exist_ok=True)
            
            self.memory_file = self.brain_dir / 'memories.json'
            self.config_file = self.brain_dir / 'config.json'

            self._load_or_create()

        def _load_or_create(self):
            """Load existing data or create new."""
            if self.memory_file.exists():
                with open(self.memory_file, 'r') as f:
                    self.memories: List[Dict[str, Any]]= J.load(f)
            else:
                self.memories: List[Dict[str, Any]] = []
                self.commit()

        def add(self, item: Dict[str, Any], auto_save: bool = True):
            if self.STORAGE_size - len(self.memories) <= 0:
                raise MemoryError("You have ran out of space. Please free some space or upgrade.")
            
            self.memories.append(item)
            if auto_save:
                self.commit()
        
        def commit(self):
            """Persist to disk."""
            with open(self.memory_file, 'w') as f:
                J.dump(self.memories, f, indent=2)

        def preview_storage(self, figsize=(7,7)):
            """Showcase storage"""
            plt.figure(figsize=figsize)
        
        def replace(self, item1: object, item2: object):
            """Replace information inside the 'mind' with different data.
            """
            if not item1 or not item2:
                raise ValueError("Please insert items")
            
        def find(self, args: object) -> bool:
            if not args:
                raise ValueError("Args cannot be empty")
            try:
                Module_name = f"{self.name}_MODEL"
                Module = lib.import_module(Module_name)

                exists = Module.query.get(args).first()
                if not exists:
                    raise ValueError(f"args ({args}) couldnt be located in memory.")
                return True

            except ModuleNotFoundError as e:
                raise ModuleNotFoundError("Error when trying to import Brain Model file.", e)



        def get_all(self) -> List[Dict[str, Any]]:
            """Get all memories."""
            
            return self.memories 
        

        def free(self, amount=10):
            """Free storage space from "mind"."""

        def remove(self, item: Any):
            try:
                if item in  self.memories:
                    self.memories.remove(item)
                    self.commit()
                else:
                    raise ValueError()
            except ValueError as e:
                raise e
            
        def avilable_space(self):
            """Check how much space is avilable for the mind."""
            space =  self.STORAGE_size - len(self.memories)
            if space <= 0:
                print(f"space left: {space}\n")
                print(f"memories space {self.memories}")
                return False 
            print(f"space left: {space}")
            return True
        
        def is_there_free_space(self) -> bool:
            space = len(self.memories) 
            return True # Placeholder
        
        def resize(self, new_size: int, force: bool = False):
            """Resize storage. If shrinking, force=True required to confirm data loss."""
            
            if not 0 < new_size <= 100:
                raise ValueError(f"New size ({new_size}) outside valid range (0-100)")
            
            if new_size == self.STORAGE_size:
                return  # Already that size, do nothing
            
            # Shrinking storage
            if new_size < self.STORAGE_size:
                if not force:
                    raise ValueError(
                        f"Shrinking from {self.STORAGE_size} to {new_size} will lose data. "
                        f"Use force=True to confirm."
                    )
                
                # Truncate memories to fit new size
                if len(self.memories) > new_size:
                    self.memories = self.memories[:new_size]
                    self.commit()
            
            self.STORAGE_size = new_size
                
        def revert(self, copy_or_new: Any, get_copy: bool = True) -> List[Dict[str, Any]]:
            """revert object to copy or new data.

                get: if True, return the new copy
            """
            self.memories = copy_or_new
            if not get_copy:
                print('')
            return self.memories
        
        def get_capacity(self) -> int:
            return self.STORAGE_size

        def get_used(self) -> int:
            return len(self.memories)
        
        def get_current_memories(self) -> List[Dict[str, Any]]:
            return self.memories

        def get_free(self) -> int:
            return self.STORAGE_size - len(self.memories)
                
                


if __name__ == "__main__":
    from datetime import datetime
    
    print("="*60)
    print("CYBERLIFE BRAIN SYSTEM - COMPREHENSIVE TEST")
    print("="*60)
    
    # Test 1: Basic creation
    print("\n[TEST 1] Creating brain...")
    brain = Brain(name="Alice", pounds=3.0, watts=20.0, storage_size=10)
    print(f"✓ Created: {brain}")
    
    # Test 2: Add memories with helper method
    print("\n[TEST 2] Storing memories...")
    test_memories = [
        ("First conversation", "curious", 0.8),
        ("Learned about classes", "excited", 0.7),
        ("Made a syntax error", "frustrated", 0.4),
        ("Fixed the bug!", "happy", 0.9),
        ("Reading docs", "neutral", 0.3),
    ]
    
    for content, emotion, importance in test_memories:
        brain.remember(content, emotion, importance)
        print(f"  ✓ Stored: {content[:30]}...")
    
    print(f"\nTotal memories: {brain.get_memory_count()}/{brain.mind.get_capacity()}")
    
    # Test 3: Query by emotion
    print("\n[TEST 3] Querying memories...")
    happy_memories = brain.get_memories_by_emotion("happy")
    print(f"Happy memories: {len(happy_memories)}")
    for mem in happy_memories:
        print(f"  • {mem['content']}")
    
    # Test 4: Power adjustments
    print("\n[TEST 4] Adjusting brain power...")
    print(f"Initial: {brain.get_power()}W")
    brain.increase(by=10.0)
    print(f"After +10W: {brain.get_power()}W")
    brain.reduce(by=5.0)
    print(f"After -5W: {brain.get_power()}W")
    
    # Test 5: Visualization
    print("\n[TEST 5] Generating visualization...")
    brain.showcase(mode="2D")
    
    # Test 6: Storage limits
    print("\n[TEST 6] Testing storage capacity...")
    try:
        for i in range(20):
            brain.remember(f"Extra memory {i}", "neutral", 0.1)
    except MemoryError as e:
        print(f"✓ Storage limit enforced: {e}")
    
    # Test 7: Error handling
    print("\n[TEST 7] Testing error handling...")
    errors_caught = 0
    
    try:
        bad1 = Brain(name="", pounds=3.0)
    except ValueError:
        errors_caught += 1
    
    try:
        bad2 = Brain(name="Bad@Name", pounds=3.0)
    except ValueError:
        errors_caught += 1
    
    try:
        bad3 = Brain(name="Bob", pounds=50.0)
    except ValueError:
        errors_caught += 1
    
    print(f"✓ Caught {errors_caught}/3 invalid inputs")
    brain = Brain(name="Test")

    # Simulate thinking (activates forebrain)
    brain.stimulate_region('forebrain', 0.5)

    # Simulate sensory input (activates midbrain)
    brain.stimulate_region('midbrain', 0.3)

    print(brain.get_brain_state())
    # {'forebrain': 0.5, 'midbrain': 0.3, 'hindbrain': 0.0}
    print("\n" + "="*60)
    print(f"FINAL STATE: {brain}")
    print("="*60)