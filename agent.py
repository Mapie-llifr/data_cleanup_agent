#agent.py

class Agent:
    def __init__(self, goal):
        self.goal = goal
        self.memory = []

    def observe(self, text):
        self.memory.append(text)

    def context(self):
        history = "\n".join(self.memory[-10:])  # last 10 steps
        return f"""
GOAL:
{self.goal}

PAST ACTIONS AND OBSERVATIONS:
{history}
"""


