class agent:

    def __init__(self, environment):

        self.environment = environment

        self.f1 = 0  # number of moves
        self.f2 = 0  # number of failed moves
        self.f3 = 0  # number of suctions
        self.f4 = 0  # number of commands of suctions
        self.f5 = 0  # number of dirty rooms

    def move_left(self):
        self.f1 += 1
        return "left"

    def move_right(self):
        self.f1 += 1
        return "right"

    def move_up(self):
        self.f1 += 1
        return "up"

    def move_down(self):
        self.f1 += 1
        return "down"

    def clean(self):
        self.environment.vacuum()

    def status(self):
        print(f"f1: {self.f1} | f2: {self.f2} | f3: {
              self.f3} | f4: {self.f4} | f5: {self.f5}")


class ag_fullyObs_deterministic_static(agent):
    def run(self):
        while all(self.environment.rooms.values()) != "clean":

            perception = self.environment.perceive()
            position = perception['position']
            cleanliness = position["cleanliness"]

            self.f5 = list(cleanliness.values()).count("dirty")

            if cleanliness[position] == 'dirty':
                self.clean()
                self.f3 += 1
                self.f4 += 1

            if position == (0, 0) and cleanliness[(1, 0)] == "dirty":
                self.environment.move(self.move_right())
            elif position == (0, 0) and cleanliness[(0, 1)] == "dirty":
                self.environment.move(self.move_up())
            elif position == (1, 0):
                self.environment.move(self.move_left())
            elif position == (0, 1):
                self.environment.move(self.move_down())

        else:
            print("---FINISH---")
            self.status()


class ag_fullyObs_deterministic_dynamic(agent):
    pass


class ag_fullyObs_stochasticInMove_static(agent):
    pass


class ag_fullyObs_stochasticInMove_dynamic(agent):
    pass


class ag_fullyObs_stochasticInVac_static(agent):
    pass


class ag_fullyObs_stochasticInVac_dynamic(agent):
    pass


class ag_noPositionSensor_deterministic_static(agent):
    pass


class ag_noPositionSensor_deterministic_dynamic(agent):
    pass


class ag_noPositionSensor_stochasticInMove_static(agent):
    pass


class ag_noPositionSensor_stochasticInMove_dynamic(agent):
    pass


class ag_noPositionSensor_stochasticInVac_static(agent):
    pass


class ag_noPositionSensor_stochasticInVac_dynamic(agent):
    pass


class ag_noCleanSensor_deterministic_static(agent):
    pass


class ag_noCleanSensor_deterministic_dynamic(agent):
    pass


class ag_noCleanSensor_stochasticInMove_static(agent):
    pass


class ag_noCleanSensor_stochasticInMove_dynamic(agent):
    pass


class ag_noCleanSensor_stochasticInVac_static(agent):
    pass


class ag_noCleanSensor_stochasticInVac_dynamic(agent):
    pass
