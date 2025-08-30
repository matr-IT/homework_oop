import pytest
from src.MixinLog import MixinLog

class TestMixinLog:
    def test_log_info(self, caplog):
        class TestClass(MixinLog):
            def __init__(self, name, value):
                self.name = name
                self.value = value
                super().__init__()