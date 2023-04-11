import axelrod as axl
C, D = axl.Action.C, axl.Action.D

class TestStrategy(axl.Player):
    name = "Test Strategy"
    classifier = {
        'memory_depth': 0,
        'stochastic': False,
        'long_run_time': False,
        'inspects_source': False,
        'manipulates_source': False,
        'manipulates_state': False,
    }

    def strategy(self, opponent):
        if self.history:
            if self.history[-1] == C:
                return D
        return C