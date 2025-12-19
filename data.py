"""Small sample dataset used by the demo vector search engine.

For now we start with a *small* list of music artists and
some descriptors so you can experiment with "similar artists"
without needing any external files.
"""

from typing import List, Dict


DOCUMENTS: List[Dict[str, str]] = [
    {"id": "artist1", "text": "Radiohead, alternative rock, experimental, art rock, melancholic"},
    {"id": "artist2", "text": "Coldplay, alternative rock, pop rock, melodic, uplifting"},
    {"id": "artist3", "text": "Kendrick Lamar, hip hop, conscious rap, storytelling, lyrical"},
    {"id": "artist4", "text": "Drake, hip hop, pop rap, mainstream, melodic"},
    {"id": "artist5", "text": "Taylor Swift, pop, country, singer-songwriter, storytelling"},
    {"id": "artist6", "text": "Billie Eilish, pop, dark, minimalist, alternative"},
    {"id": "artist7", "text": "Metallica, metal, heavy metal, aggressive, guitar riffs"},
    {"id": "artist8", "text": "Nirvana, grunge, alternative rock, 90s, raw"},
    {"id": "artist9", "text": "The Weeknd, R&B, pop, dark, synth-driven"},
    {"id": "artist10", "text": "Daft Punk, electronic, house, dance, French"},
]

def load_documents() -> List[Dict[str, str]]:
    """Load and return the sample documents."""
    return DOCUMENTS