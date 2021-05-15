from __future__ import annotations
from tagcommand import TagCommand
from selection import Selection

class MakeUnderlineCommand(TagCommand):
    def __init__(self, sel: Selection):
        super().__init__('<u>' , '</u>', sel)