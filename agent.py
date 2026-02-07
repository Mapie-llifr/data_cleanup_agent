#agent.py

class Agent:
    def __init__(self, goal):
        self.goal = goal
        self.memory = []   # working memory

    def add_observation(self, obs):
        self.memory.append(obs)

    def get_context(self):
        text = "\n".join(self.memory)
        return f"Goal: {self.goal}\n\nMemory:\n{text}"

