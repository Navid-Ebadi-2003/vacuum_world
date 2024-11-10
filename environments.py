import random


class environment:
    def __init__(self, R0, R1, R2):
        self.rooms = {
            (0, 0): R0,
            (1, 0): R1,
            (0, 1): R2
        }
        self.agent_position = (0, 0)

    # def perceive(self):
    #     pass

    def move(self, action):
        if action == "up" and self.agent_position == (0, 0):
            self.agent_position = (0, 1)
            print("move to up")
            return True
        elif action == "left" and self.agent_position == (1, 0):
            self.agent_position = (0, 0)
            print("move to left")
            return True
        elif action == "right" and self.agent_position == (0, 0):
            self.agent_position = (1, 0)
            print("move to right")
            return True
        elif action == "down" and self.agent_position == (0, 1):
            self.agent_position = (0, 0)
            print("move to down")
            return True
        else:
            return False

    def vacuum(self):
        if self.rooms[self.agent_position] == 'dirty':
            self.rooms[self.agent_position] = 'clean'
            return True
        else:
            return False

class env_fullyObs_deterministic_static(environment):
    def perceive(self):
        return {
            'position': self.agent_position,
            'cleanliness': self.rooms[self.agent_position]
        }


class env_fullyObs_deterministic_dynamic(environment):

    def dynamic_dirtying(self):
        for room in self.rooms:
            if random.random() < 0.2:
                self.rooms[room] = 'dirty'

    def perceive(self):

        perception = {
            'position': self.agent_position,
            'cleanliness': self.rooms[self.agent_position]
        }

        self.dynamic_dirtying()
        return perception


class env_fullyObs_stochasticInMove_static(environment):
    def perceive(self):
        return {
            'position': self.agent_position,
            'cleanliness': self.rooms[self.agent_position]
        }


class env_fullyObs_stochasticInMove_dynamic(environment):
    def dynamic_dirtying(self):
        for room in self.rooms:
            if random.random() < 0.2:
                self.rooms[room] = 'dirty'

    def perceive(self):

        perception = {
            'position': self.agent_position,
            'cleanliness': self.rooms[self.agent_position]
        }

        self.dynamic_dirtying()
        return perception


class env_fullyObs_stochasticInVac_static(environment):
    def perceive(self):
        return {
            'position': self.agent_position,
            'cleanliness': self.rooms[self.agent_position]
        }


class env_fullyObs_stochasticInVac_dynamic(environment):
    def dynamic_dirtying(self):
        for room in self.rooms:
            if random.random() < 0.2:
                self.rooms[room] = 'dirty'

    def perceive(self):

        perception = {
            'position': self.agent_position,
            'cleanliness': self.rooms[self.agent_position]
        }

        self.dynamic_dirtying()
        return perception











class env_noPositionSensor_deterministic_static(environment):
    def perceive(self):
        return {
            'cleanliness': self.rooms[self.agent_position]
        }


class env_noPositionSensor_deterministic_dynamic(environment):
    def dynamic_dirtying(self):
        for room in self.rooms:
            if random.random() < 0.2:
                self.rooms[room] = 'dirty'

    def perceive(self):

        perception = {
            'cleanliness': self.rooms[self.agent_position]
        }

        self.dynamic_dirtying()
        return perception














class env_noPositionSensor_stochasticInMove_static(environment):
    def perceive(self):
        return {
            'cleanliness': self.rooms[self.agent_position]
        }

    def move(self, action):
        if random.random() > 0.2:
            super().move(action)


class env_noPositionSensor_stochasticInMove_dynamic(environment):
    def perceive(self):
        return {
            'cleanliness': self.rooms[self.agent_position]
        }

    def move(self, action):
        if random.random() > 0.2:
            super().move(action)

    def dynamic_dirtying(self):
        for room in self.rooms:
            if random.random() < 0.2:
                self.rooms[room] = 'dirty'


class env_noPositionSensor_stochasticInVac_static(environment):
    def perceive(self):
        return {
            'cleanliness': self.rooms[self.agent_position]
        }

    def vacuum(self):
        if random.random() > 0.2:
            super().vacuum()


class env_noPositionSensor_stochasticInVac_dynamic(environment):
    def perceive(self):
        return {
            'cleanliness': self.rooms[self.agent_position]
        }

    def vacuum(self):
        if random.random() > 0.2:
            super().vacuum()

    def dynamic_dirtying(self):
        for room in self.rooms:
            if random.random() < 0.2:
                self.rooms[room] = 'dirty'









class env_noCleanSensor_deterministic_static(environment):
    def perceive(self):
        return {
            'position': self.agent_position
        }


class env_noCleanSensor_deterministic_dynamic(environment):
    def dynamic_dirtying(self):
        for room in self.rooms:
            if random.random() < 0.2:
                self.rooms[room] = 'dirty'

    def perceive(self):

        perception = {
            'position': self.agent_position,
        }

        self.dynamic_dirtying()
        return perception


class env_noCleanSensor_stochasticInMove_static(environment):
    def perceive(self):
        return {
            'position': self.agent_position
        }


class env_noCleanSensor_stochasticInMove_dynamic(environment):
    def dynamic_dirtying(self):
        for room in self.rooms:
            if random.random() < 0.2:
                self.rooms[room] = 'dirty'

    def perceive(self):

        perception = {
            'position': self.agent_position,
        }

        self.dynamic_dirtying()
        return perception


class env_noCleanSensor_stochasticInVac_static(environment):
    def perceive(self):
        return {
            'position': self.agent_position
        }


class env_noCleanSensor_stochasticInVac_dynamic(environment):
    def dynamic_dirtying(self):
        for room in self.rooms:
            if random.random() < 0.2:
                self.rooms[room] = 'dirty'

    def perceive(self):

        perception = {
            'position': self.agent_position,
        }

        self.dynamic_dirtying()
        return perception
