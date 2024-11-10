import random


class agent:

    def __init__(self, environment):

        self.environment = environment

        self.f1 = 0  # number of moves
        self.f2 = 0  # number of failed moves
        self.f3 = 0  # number of suctions
        self.f4 = 0  # number of successful suctions
        self.f5 = list(self.environment.rooms.values()).count(
            "dirty")  # number of dirty rooms

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
        result = self.environment.vacuum()
        self.f3 += 1
        print("suction don")
        return result

    def ran_act(self):
        x = random.randint(1, 4)
        if x == 1:
            return self.move_up()
        elif x == 2:
            return self.move_down()
        elif x == 3:
            return self.move_right()
        else:
            return self.move_left()

    def status(self):
        print(f"f1: {self.f1} | f2: {self.f2} | f3: {
              self.f3} | f4: {self.f4} | f5: {self.f5}")


class ag_fullyObs_deterministic_static(agent):
    def run(self):

        self.status()
        last_move = None
        first_act = True

        while not all(value == "clean" for value in self.environment.rooms.values()):

            perception = self.environment.perceive()
            position = perception['position']
            cleanliness = perception["cleanliness"]

            if cleanliness == 'dirty':
                self.clean()
                self.f4 += 1
                if all(value == "clean" for value in self.environment.rooms.values()):
                    self.f5 = list(
                        self.environment.rooms.values()).count("dirty")
                    self.status()
                    print("----------FINISH-----------")
                    break

            if first_act == True:
                ran_chose = random.randint(1, 2)
                if ran_chose == 1:
                    last_move = self.move_right()
                    self.environment.move(last_move)
                else:
                    last_move = self.move_up()
                    self.environment.move(last_move)
                first_act = False

            elif position == (0, 0) and last_move != "left":
                last_move = self.move_right()
                self.environment.move(last_move)
            elif position == (0, 0):
                last_move = self.move_up()
                self.environment.move(last_move)
            elif position == (1, 0):
                last_move = self.move_left()
                self.environment.move(last_move)
            elif position == (0, 1):
                last_move = self.move_down()
                self.environment.move(last_move)

            self.f5 = list(self.environment.rooms.values()).count("dirty")
            self.status()

        else:
            print("----------FINISH-----------")


class ag_fullyObs_deterministic_dynamic(agent):
    def run(self):

        self.status()
        last_move = None

        while not all(value == "clean" for value in self.environment.rooms.values()):

            perception = self.environment.perceive()
            position = perception['position']
            cleanliness = perception["cleanliness"]

            if cleanliness == 'dirty':
                self.clean()
                self.f4 += 1
                if all(value == "clean" for value in self.environment.rooms.values()):
                    self.f5 = list(
                        self.environment.rooms.values()).count("dirty")
                    self.status()
                    print("----------FINISH-----------")
                    break

            ran_chose = random.randint(1, 2)

            if position == (0, 0) and ran_chose == 1:
                last_move = self.move_right()
                self.environment.move(last_move)
            elif position == (0, 0) and ran_chose == 2:
                last_move = self.move_up()
                self.environment.move(last_move)
            elif position == (1, 0):
                last_move = self.move_left()
                self.environment.move(last_move)
            elif position == (0, 1):
                last_move = self.move_down()
                self.environment.move(last_move)

            self.f5 = list(self.environment.rooms.values()).count("dirty")
            self.status()

        else:
            print("----------FINISH-----------")


class ag_fullyObs_stochasticInMove_static(agent):
    def run(self):

        self.status()
        last_move = None
        first_act = True

        while not all(value == "clean" for value in self.environment.rooms.values()):

            perception = self.environment.perceive()
            position = perception['position']
            cleanliness = perception["cleanliness"]

            if cleanliness == 'dirty':
                self.clean()
                self.f4 += 1
                if all(value == "clean" for value in self.environment.rooms.values()):
                    self.f5 = list(
                        self.environment.rooms.values()).count("dirty")
                    self.status()
                    print("----------FINISH-----------")
                    break

            if random.random() > 0.2:
                if first_act == True:
                    ran_chose = random.randint(1, 2)
                    if ran_chose == 1:
                        last_move = self.move_right()
                        self.environment.move(last_move)
                    else:
                        last_move = self.move_up()
                        self.environment.move(last_move)
                    first_act = False

                elif position == (0, 0) and last_move != "left":
                    last_move = self.move_right()
                    self.environment.move(last_move)
                elif position == (0, 0):
                    last_move = self.move_up()
                    self.environment.move(last_move)
                elif position == (1, 0):
                    last_move = self.move_left()
                    self.environment.move(last_move)
                elif position == (0, 1):
                    last_move = self.move_down()
                    self.environment.move(last_move)
            else:
                print("act random")
                last_move = self.ran_act()
                success = self.environment.move(last_move)
                if not success:
                    self.f2 += 1
                    print("hit the wall")

            self.f5 = list(self.environment.rooms.values()).count("dirty")
            self.status()

        else:
            print("----------FINISH-----------")


class ag_fullyObs_stochasticInMove_dynamic(agent):
    def run(self):

        self.status()
        last_move = None

        while not all(value == "clean" for value in self.environment.rooms.values()):

            perception = self.environment.perceive()
            position = perception['position']
            cleanliness = perception["cleanliness"]

            if cleanliness == 'dirty':
                self.clean()
                self.f4 += 1
                if all(value == "clean" for value in self.environment.rooms.values()):
                    self.f5 = list(
                        self.environment.rooms.values()).count("dirty")
                    self.status()
                    print("----------FINISH-----------")
                    break
            if random.random() > 0.2:
                ran_chose = random.randint(1, 2)

                if position == (0, 0) and ran_chose == 1:
                    last_move = self.move_right()
                    self.environment.move(last_move)
                elif position == (0, 0) and ran_chose == 2:
                    last_move = self.move_up()
                    self.environment.move(last_move)
                elif position == (1, 0):
                    last_move = self.move_left()
                    self.environment.move(last_move)
                elif position == (0, 1):
                    last_move = self.move_down()
                    self.environment.move(last_move)
            else:
                print("act random")
                last_move = self.ran_act()
                success = self.environment.move(last_move)
                if not success:
                    self.f2 += 1
                    print("hit the wall")

            self.f5 = list(self.environment.rooms.values()).count("dirty")
            self.status()

        else:
            print("----------FINISH-----------")


class ag_fullyObs_stochasticInVac_static(agent):
    def run(self):

        self.status()
        last_move = None

        while not all(value == "clean" for value in self.environment.rooms.values()):

            perception = self.environment.perceive()
            position = perception['position']
            cleanliness = perception["cleanliness"]

            if cleanliness == 'dirty':
                if random.random() > 0.2:
                    self.clean()
                    self.f4 += 1
                    if all(value == "clean" for value in self.environment.rooms.values()):
                        self.f5 = list(
                            self.environment.rooms.values()).count("dirty")
                        self.status()
                        print("----------FINISH-----------")
                        break
                else:
                    self.f3 += 1
                    print("suction failed")

            ran_chose = random.randint(1, 2)

            if position == (0, 0) and ran_chose == 1:
                last_move = self.move_right()
                self.environment.move(last_move)
            elif position == (0, 0) and ran_chose == 2:
                last_move = self.move_up()
                self.environment.move(last_move)
            elif position == (1, 0):
                last_move = self.move_left()
                self.environment.move(last_move)
            elif position == (0, 1):
                last_move = self.move_down()
                self.environment.move(last_move)

            self.f5 = list(self.environment.rooms.values()).count("dirty")
            self.status()

        else:
            print("----------FINISH-----------")


class ag_fullyObs_stochasticInVac_dynamic(agent):
    def run(self):

        self.status()
        last_move = None

        while not all(value == "clean" for value in self.environment.rooms.values()):

            perception = self.environment.perceive()
            position = perception['position']
            cleanliness = perception["cleanliness"]

            if cleanliness == 'dirty':
                if random.random() > 0.2:
                    self.clean()
                    self.f4 += 1
                    if all(value == "clean" for value in self.environment.rooms.values()):
                        self.f5 = list(
                            self.environment.rooms.values()).count("dirty")
                        self.status()
                        print("----------FINISH-----------")
                        break
                else:
                    self.f3 += 1
                    print("suction failed")

            ran_chose = random.randint(1, 2)

            if position == (0, 0) and ran_chose == 1:
                last_move = self.move_right()
                self.environment.move(last_move)
            elif position == (0, 0) and ran_chose == 2:
                last_move = self.move_up()
                self.environment.move(last_move)
            elif position == (1, 0):
                last_move = self.move_left()
                self.environment.move(last_move)
            elif position == (0, 1):
                last_move = self.move_down()
                self.environment.move(last_move)

            self.f5 = list(self.environment.rooms.values()).count("dirty")
            self.status()

        else:
            print("----------FINISH-----------")


class ag_noPositionSensor_deterministic_static(agent):

    def ran_act(self):
        x = random.randint(1, 4)
        if x == 1:
            return "up"
        elif x == 2:
            return "down"
        elif x == 3:
            return "right"
        else:
            return "left"

    def run(self):

        self.status()
        last_move = None
        mistake = [None]

        while not all(value == "clean" for value in self.environment.rooms.values()):

            perception = self.environment.perceive()
            cleanliness = perception["cleanliness"]

            if cleanliness == 'dirty':
                self.clean()
                self.f4 += 1
                if all(value == "clean" for value in self.environment.rooms.values()):
                    self.f5 = list(
                        self.environment.rooms.values()).count("dirty")
                    self.status()
                    print("----------FINISH-----------")
                    break

            movement = None
            while (movement in mistake ):
                movement = self.ran_act()

            success = self.environment.move(movement)
            self.f1 += 1
            if success :
                last_move = movement

                if last_move == "left":
                    mistake = [None ,"right"]
                elif last_move == "down":
                    mistake = [None ,"up"]
                else :
                    mistake=[None]
            else :
                self.f2 += 1
                mistake.append(movement)
                print("hit the wall")
                print(f"{movement} was mistake")

            self.f5 = list(self.environment.rooms.values()).count("dirty")
            self.status()

        else:
            print("----------FINISH-----------")


class ag_noPositionSensor_deterministic_dynamic(agent):
    
    def ran_act(self):
        x = random.randint(1, 4)
        if x == 1:
            return "up"
        elif x == 2:
            return "down"
        elif x == 3:
            return "right"
        else:
            return "left"

    def run(self):

        self.status()
        mistake = [None]

        while not all(value == "clean" for value in self.environment.rooms.values()):

            perception = self.environment.perceive()
            cleanliness = perception["cleanliness"]

            if cleanliness == 'dirty':
                self.clean()
                self.f4 += 1
                if all(value == "clean" for value in self.environment.rooms.values()):
                    self.f5 = list(
                        self.environment.rooms.values()).count("dirty")
                    self.status()
                    print("----------FINISH-----------")
                    break

            movement = None
            while (movement in mistake ):
                movement = self.ran_act()

            success = self.environment.move(movement)
            self.f1 += 1
            if success :
                mistake=[None]
            else :
                self.f2 += 1
                mistake.append(movement)
                print("hit the wall")
                print(f"{movement} was mistake")

            self.f5 = list(self.environment.rooms.values()).count("dirty")
            self.status()

        else:
            print("----------FINISH-----------")


class ag_noPositionSensor_stochasticInMove_static(agent):
    def ran_act(self):
        x = random.randint(1, 4)
        if x == 1:
            return "up"
        elif x == 2:
            return "down"
        elif x == 3:
            return "right"
        else:
            return "left"

    def run(self):
        self.status()
        last_move = None
        first_act = True

        while not all(value == "clean" for value in self.environment.rooms.values()):
            perception = self.environment.perceive()
            cleanliness = perception.get("cleanliness", None)

            # Cleaning action
            if cleanliness == 'dirty':
                self.clean()
                self.f4 += 1
                if all(value == "clean" for value in self.environment.rooms.values()):
                    self.f5 = list(self.environment.rooms.values()).count("dirty")
                    self.status()
                    print("----------FINISH-----------")
                    break

            if random.random() > 0.2:
                if first_act:
                    ran_chose = random.randint(1, 2)
                    if ran_chose == 1:
                        last_move = self.move_right()
                    else:
                        last_move = self.move_up()
                    self.environment.move(last_move)
                    first_act = False
                else:
                    if last_move == "right":
                        last_move = self.move_up()
                    elif last_move == "up":
                        last_move = self.move_left()
                    elif last_move == "left":
                        last_move = self.move_down()
                    else:
                        last_move = self.move_right()
                    self.environment.move(last_move)
            else:
                print("act random")
                last_move = self.ran_act()
                success = self.environment.move(last_move)
                if not success:
                    self.f2 += 1
                    print("hit the wall")

            self.f5 = list(self.environment.rooms.values()).count("dirty")
            self.status()

        else:
            print("----------FINISH-----------")


class ag_noPositionSensor_stochasticInMove_dynamic(agent):
    def ran_act(self):
        x = random.randint(1, 4)
        if x == 1:
            return "up"
        elif x == 2:
            return "down"
        elif x == 3:
            return "right"
        else:
            return "left"

    def run(self):
        self.status()
        last_move = None
        mistake = [None]
        first_act = True

        while not all(value == "clean" for value in self.environment.rooms.values()):
            perception = self.environment.perceive()
            cleanliness = perception.get("cleanliness", None)

            if cleanliness == 'dirty':
                self.clean()
                self.f4 += 1
                if all(value == "clean" for value in self.environment.rooms.values()):
                    self.f5 = list(self.environment.rooms.values()).count("dirty")
                    self.status()
                    print("----------FINISH-----------")
                    break

            if random.random() > 0.2:
                if first_act:
                    ran_chose = random.randint(1, 2)
                    if ran_chose == 1:
                        last_move = "right"
                    else:
                        last_move = "up"
                    first_act = False
                else:
                    if last_move == "right":
                        last_move = "up"
                    elif last_move == "up":
                        last_move = "left"
                    elif last_move == "left":
                        last_move = "down"
                    else:
                        last_move = "right"

                success = self.environment.move(last_move)
                if success:
                    mistake = [None]
                else:
                    self.f2 += 1
                    mistake.append(last_move)
                    print("hit the wall")
                    print(f"{last_move} was mistake")
            else:
                print("act random")
                movement = None
                while movement in mistake:
                    movement = self.ran_act()
                success = self.environment.move(movement)
                if not success:
                    self.f2 += 1
                    mistake.append(movement)
                    print("hit the wall")
                    print(f"{movement} was mistake")

            self.f5 = list(self.environment.rooms.values()).count("dirty")
            self.status()

        else:
            print("----------FINISH-----------")

class ag_noPositionSensor_stochasticInVac_static(agent):
    def run(self):
        self.status()
        last_move = None

        while not all(value == "clean" for value in self.environment.rooms.values()):

            perception = self.environment.perceive()
            cleanliness = perception["cleanliness"]

            if cleanliness == 'dirty':
                if random.random() > 0.2:
                    self.clean()
                    self.f4 += 1
                    if all(value == "clean" for value in self.environment.rooms.values()):
                        self.f5 = list(self.environment.rooms.values()).count("dirty")
                        self.status()
                        print("----------FINISH-----------")
                        break
                else:
                    self.f3 += 1
                    print("suction failed")

            ran_chose = random.randint(1, 2)

            if ran_chose == 1:
                last_move = self.move_right()
                self.environment.move(last_move)
            else:
                last_move = self.move_up()
                self.environment.move(last_move)

            self.f5 = list(self.environment.rooms.values()).count("dirty")
            self.status()

        else:
            print("----------FINISH-----------")



class ag_noPositionSensor_stochasticInVac_dynamic(agent):
    def run(self):
        self.status()
        last_move = None

        while not all(value == "clean" for value in self.environment.rooms.values()):

            perception = self.environment.perceive()
            cleanliness = perception["cleanliness"]

            if cleanliness == 'dirty':
                if random.random() > 0.2:
                    self.clean()
                    self.f4 += 1
                    if all(value == "clean" for value in self.environment.rooms.values()):
                        self.f5 = list(self.environment.rooms.values()).count("dirty")
                        self.status()
                        print("----------FINISH-----------")
                        break
                else:
                    self.f3 += 1
                    print("suction failed")

            ran_chose = random.randint(1, 2)

            if ran_chose == 1:
                last_move = self.move_right()
                self.environment.move(last_move)
            else:
                last_move = self.move_up()
                self.environment.move(last_move)

            self.f5 = list(self.environment.rooms.values()).count("dirty")
            self.status()

        else:
            print("----------FINISH-----------")


class ag_noCleanSensor_deterministic_static(agent):
    def run(self):

        self.status()
        last_move = None
        first_act = True

        while not all(value == "clean" for value in self.environment.rooms.values()):

            perception = self.environment.perceive()
            position = perception['position']

            if first_act or position != (0, 0):
                result = self.clean()
                if result:
                    self.f4 += 1

                if all(value == "clean" for value in self.environment.rooms.values()):
                    self.f5 = list(
                        self.environment.rooms.values()).count("dirty")
                    self.status()
                    print("----------FINISH-----------")
                    break

            if first_act == True:
                ran_chose = random.randint(1, 2)
                if ran_chose == 1:
                    last_move = self.move_right()
                    self.environment.move(last_move)
                else:
                    last_move = self.move_up()
                    self.environment.move(last_move)
                first_act = False

            elif position == (0, 0) and last_move != "left":
                last_move = self.move_right()
                self.environment.move(last_move)
            elif position == (0, 0):
                last_move = self.move_up()
                self.environment.move(last_move)
            elif position == (1, 0):
                last_move = self.move_left()
                self.environment.move(last_move)
            elif position == (0, 1):
                last_move = self.move_down()
                self.environment.move(last_move)

            self.f5 = list(self.environment.rooms.values()).count("dirty")
            self.status()

        else:
            print("----------FINISH-----------")


class ag_noCleanSensor_deterministic_dynamic(agent):
    def run(self):

        self.status()
        last_move = None

        while not all(value == "clean" for value in self.environment.rooms.values()):

            perception = self.environment.perceive()
            position = perception['position']

            result = self.clean()
            if result:
                self.f4 += 1

            if all(value == "clean" for value in self.environment.rooms.values()):
                self.f5 = list(
                    self.environment.rooms.values()).count("dirty")
                self.status()
                print("----------FINISH-----------")
                break

            ran_chose = random.randint(1, 2)

            if position == (0, 0) and ran_chose == 1:
                last_move = self.move_right()
                self.environment.move(last_move)
            elif position == (0, 0) and ran_chose == 2:
                last_move = self.move_up()
                self.environment.move(last_move)
            elif position == (1, 0):
                last_move = self.move_left()
                self.environment.move(last_move)
            elif position == (0, 1):
                last_move = self.move_down()
                self.environment.move(last_move)

            self.f5 = list(self.environment.rooms.values()).count("dirty")
            self.status()

        else:
            print("----------FINISH-----------")


class ag_noCleanSensor_stochasticInMove_static(agent):
    def run(self):

        self.status()
        last_move = None
        first_act = True

        while not all(value == "clean" for value in self.environment.rooms.values()):

            perception = self.environment.perceive()
            position = perception['position']

            if first_act or position != (0, 0):
                result = self.clean()
                if result:
                    self.f4 += 1

                if all(value == "clean" for value in self.environment.rooms.values()):
                    self.f5 = list(
                        self.environment.rooms.values()).count("dirty")
                    self.status()
                    print("----------FINISH-----------")
                    break

            if random.random() > 0.2:
                if first_act == True:
                    ran_chose = random.randint(1, 2)
                    if ran_chose == 1:
                        last_move = self.move_right()
                        self.environment.move(last_move)
                    else:
                        last_move = self.move_up()
                        self.environment.move(last_move)
                    first_act = False

                elif position == (0, 0) and last_move != "left":
                    last_move = self.move_right()
                    self.environment.move(last_move)
                elif position == (0, 0):
                    last_move = self.move_up()
                    self.environment.move(last_move)
                elif position == (1, 0):
                    last_move = self.move_left()
                    self.environment.move(last_move)
                elif position == (0, 1):
                    last_move = self.move_down()
                    self.environment.move(last_move)
            else:
                print("act random")
                last_move = self.ran_act()
                success = self.environment.move(last_move)
                if not success:
                    self.f2 += 1
                    print("hit the wall")

            self.f5 = list(self.environment.rooms.values()).count("dirty")
            self.status()

        else:
            print("----------FINISH-----------")


class ag_noCleanSensor_stochasticInMove_dynamic(agent):
    def run(self):

        self.status()
        last_move = None

        while not all(value == "clean" for value in self.environment.rooms.values()):

            perception = self.environment.perceive()
            position = perception['position']

            result = self.clean()
            if result:
                self.f4 += 1

            if all(value == "clean" for value in self.environment.rooms.values()):
                self.f5 = list(
                    self.environment.rooms.values()).count("dirty")
                self.status()
                print("----------FINISH-----------")
                break

            if random.random() > 0.2:
                ran_chose = random.randint(1, 2)

                if position == (0, 0) and ran_chose == 1:
                    last_move = self.move_right()
                    self.environment.move(last_move)
                elif position == (0, 0) and ran_chose == 2:
                    last_move = self.move_up()
                    self.environment.move(last_move)
                elif position == (1, 0):
                    last_move = self.move_left()
                    self.environment.move(last_move)
                elif position == (0, 1):
                    last_move = self.move_down()
                    self.environment.move(last_move)
            else:
                print("act random")
                last_move = self.ran_act()
                success = self.environment.move(last_move)
                if not success:
                    self.f2 += 1
                    print("hit the wall")

            self.f5 = list(self.environment.rooms.values()).count("dirty")
            self.status()

        else:
            print("----------FINISH-----------")


class ag_noCleanSensor_stochasticInVac_static(agent):
    def run(self):

        self.status()
        last_move = None

        while not all(value == "clean" for value in self.environment.rooms.values()):

            perception = self.environment.perceive()
            position = perception['position']

            if random.random() > 0.2:
                result = self.clean()
                if result:
                    self.f4 += 1
            else:
                self.f3 += 1
                print("suction failed")

            if all(value == "clean" for value in self.environment.rooms.values()):
                self.f5 = list(
                    self.environment.rooms.values()).count("dirty")
                self.status()
                print("----------FINISH-----------")
                break

            ran_chose = random.randint(1, 2)

            if position == (0, 0) and ran_chose == 1:
                last_move = self.move_right()
                self.environment.move(last_move)
            elif position == (0, 0) and ran_chose == 2:
                last_move = self.move_up()
                self.environment.move(last_move)
            elif position == (1, 0):
                last_move = self.move_left()
                self.environment.move(last_move)
            elif position == (0, 1):
                last_move = self.move_down()
                self.environment.move(last_move)

            self.f5 = list(self.environment.rooms.values()).count("dirty")
            self.status()

        else:
            print("----------FINISH-----------")


class ag_noCleanSensor_stochasticInVac_dynamic(agent):
    def run(self):

        self.status()
        last_move = None

        while not all(value == "clean" for value in self.environment.rooms.values()):

            perception = self.environment.perceive()
            position = perception['position']

            if random.random() > 0.2:
                result = self.clean()
                if result:
                    self.f4 += 1
            else:
                self.f3 += 1
                print("suction failed")

            if all(value == "clean" for value in self.environment.rooms.values()):
                self.f5 = list(
                    self.environment.rooms.values()).count("dirty")
                self.status()
                print("----------FINISH-----------")
                break

            ran_chose = random.randint(1, 2)

            if position == (0, 0) and ran_chose == 1:
                last_move = self.move_right()
                self.environment.move(last_move)
            elif position == (0, 0) and ran_chose == 2:
                last_move = self.move_up()
                self.environment.move(last_move)
            elif position == (1, 0):
                last_move = self.move_left()
                self.environment.move(last_move)
            elif position == (0, 1):
                last_move = self.move_down()
                self.environment.move(last_move)

            self.f5 = list(self.environment.rooms.values()).count("dirty")
            self.status()

        else:
            print("----------FINISH-----------")
