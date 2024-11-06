import random

class Environment:
    def __init__(self):
        self.rooms = {
            (0, 0): 'dirty',
            (0, 1): 'dirty',
            (1, 0): 'dirty'
        }
        self.robot_position = (0, 0)  
    
    # def perceive(self):
    #     pass

    def move(self, action):
        if action == "up" and self.robot_position == (1, 0):
            self.robot_position = (1, 0)
        elif action == "up" and self.robot_position == (0, 0):
            self.robot_position = (1, 0)
        elif action == "up" and self.robot_position == (0, 1):
            self.robot_position = (0, 1)
        elif action == "left" and self.robot_position == (1, 0):
            self.robot_position = (1, 0)
        elif action == "left" and self.robot_position == (0, 0):
            self.robot_position = (0, 0)
        elif action == "left" and self.robot_position == (0, 1):
            self.robot_position = (0, 0)
        elif action == "right" and self.robot_position == (1, 0):
            self.robot_position = (1, 0)
        elif action == "right" and self.robot_position == (0, 0):
            self.robot_position = (0, 1)
        elif action == "right" and self.robot_position == (0, 1):
            self.robot_position = (0, 1)
        elif action == "down" and self.robot_position == (1, 0):
            self.robot_position = (0, 0)
        elif action == "down" and self.robot_position == (0, 0):
            self.robot_position = (0, 0)
        elif action == "down" and self.robot_position == (0, 1):
            self.robot_position = (0, 1)


    def vacuum(self):
        if self.rooms[self.robot_position] == 'dirty':
            self.rooms[self.robot_position] = 'clean'


class EnvFullyObsDeterministicStatic(Environment):
    def perceive(self):
        return {
            'position': self.robot_position,
            'cleanliness': self.rooms.copy()
        }


class EnvFullyObsDeterministicDynamic(Environment):
    def perceive(self):
        """Fully observable and deterministic with rooms potentially becoming dirty again."""
        return {
            'position': self.robot_position,
            'cleanliness': self.rooms.copy()
        }
    
    def move(self, action):
        super().move(action)
    
    def dynamic_dirtying(self):
        for room in self.rooms:
            if random.random() < 0.2:  
                self.rooms[room] = 'dirty'


class EnvFullyObsStochasticInMoveStatic(Environment):
    def perceive(self):
        return {
            'position': self.robot_position,
            'cleanliness': self.rooms.copy()
        }
    
    def move(self, action):
        if random.random() > 0.2:  
            super().move(action)


class EnvFullyObsStochasticInMoveDynamic(Environment):
    def perceive(self):
        return {
            'position': self.robot_position,
            'cleanliness': self.rooms.copy()
        }
    
    def move(self, action):
        if random.random() > 0.2:  
            super().move(action)
    
    def dynamic_dirtying(self):
        for room in self.rooms:
            if random.random() < 0.2:
                self.rooms[room] = 'dirty'


class EnvFullyObsStochasticInVacStatic(Environment):
    def perceive(self):
        return {
            'position': self.robot_position,
            'cleanliness': self.rooms.copy()
        }
    
    def vacuum(self):
        if random.random() > 0.2:  
            super().vacuum()


class EnvFullyObsStochasticInVacDynamic(Environment):
    def perceive(self):
        return {
            'position': self.robot_position,
            'cleanliness': self.rooms.copy()
        }
    
    def vacuum(self):
        if random.random() > 0.2:  
            super().vacuum()
    
    def dynamic_dirtying(self):
        for room in self.rooms:
            if random.random() < 0.2:
                self.rooms[room] = 'dirty'


class EnvNoPositionSensorDeterministicStatic(Environment):
    def perceive(self):
        return {
            'cleanliness': self.rooms.copy()
        }


class EnvNoPositionSensorDeterministicDynamic(Environment):
    def perceive(self):
        return {
            'cleanliness': self.rooms.copy()
        }
    
    def dynamic_dirtying(self):
        for room in self.rooms:
            if random.random() < 0.2:
                self.rooms[room] = 'dirty'


class EnvNoPositionSensorStochasticInMoveStatic(Environment):
    def perceive(self):
        return {
            'cleanliness': self.rooms.copy()
        }

    def move(self, action):
        if random.random() > 0.2:  
            super().move(action)


class EnvNoPositionSensorStochasticInMoveDynamic(Environment):
    def perceive(self):
        return {
            'cleanliness': self.rooms.copy()
        }

    def move(self, action):
        if random.random() > 0.2:  
            super().move(action)

    def dynamic_dirtying(self):
        for room in self.rooms:
            if random.random() < 0.2:  
                self.rooms[room] = 'dirty'


class EnvNoPositionSensorStochasticInVacStatic(Environment):
    def perceive(self):
        return {
            'cleanliness': self.rooms.copy()
        }

    def vacuum(self):
        if random.random() > 0.2:  
            super().vacuum()


class EnvNoPositionSensorStochasticInVacDynamic(Environment):
    def perceive(self):
        return {
            'cleanliness': self.rooms.copy()
        }

    def vacuum(self):
        if random.random() > 0.2:  
            super().vacuum()

    def dynamic_dirtying(self):
        for room in self.rooms:
            if random.random() < 0.2:  
                self.rooms[room] = 'dirty'


class EnvNoCleanSensorDeterministicStatic(Environment):
    def perceive(self):
        return {
            'position': self.robot_position
        }


class EnvNoCleanSensorDeterministicDynamic(Environment):
    def perceive(self):
        return {
            'position': self.robot_position
        }

    def dynamic_dirtying(self):
        for room in self.rooms:
            if random.random() < 0.2:  
                self.rooms[room] = 'dirty'


class EnvNoCleanSensorStochasticInMoveStatic(Environment):
    def perceive(self):
        return {
            'position': self.robot_position
        }

    def move(self, action):
        if random.random() > 0.2:  
            super().move(action)


class EnvNoCleanSensorStochasticInMoveDynamic(Environment):
    def perceive(self):
        return {
            'position': self.robot_position
        }

    def move(self, action):
        if random.random() > 0.2: 
            super().move(action)

    def dynamic_dirtying(self):
        for room in self.rooms:
            if random.random() < 0.2:  
                self.rooms[room] = 'dirty'


class EnvNoCleanSensorStochasticInVacStatic(Environment):
    def perceive(self):
        return {
            'position': self.robot_position
        }

    def vacuum(self):
        if random.random() > 0.2:  
            super().vacuum()


class EnvNoCleanSensorStochasticInVacDynamic(Environment):
    def perceive(self):
        return {
            'position': self.robot_position
        }

    def vacuum(self):
        if random.random() > 0.2: 
            super().vacuum()

    def dynamic_dirtying(self):
        for room in self.rooms:
            if random.random() < 0.2:  
                self.rooms[room] = 'dirty'
