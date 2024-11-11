#Navid Ebadi 401222093
#Sara Akbarzade 401222155

import environments
import agents

print("-------fullyObs_deterministic_static-------")

#                                     clean or dirty  (0,0),   (1,0),   (0,1)
env = environments.env_fullyObs_deterministic_static("dirty", "clean", "dirty")
agent = agents.ag_fullyObs_deterministic_static(env)

agent.run()
print("\n")


print("-------fullyObs_deterministic_dynamic-------")

#                                     clean or dirty  (0,0),   (1,0),   (0,1)
env = environments.env_fullyObs_deterministic_dynamic("dirty", "clean", "dirty")
agent = agents.ag_fullyObs_deterministic_dynamic(env)

agent.run()
print("\n")


print("-------fullyObs_stochasticInMove_static-------")

#                                        clean or dirty  (0,0),   (1,0),   (0,1)
env = environments.env_fullyObs_stochasticInMove_static("dirty", "clean", "dirty")
agent = agents.ag_fullyObs_stochasticInMove_static(env)

agent.run()
print("\n")


print("-------fullyObs_stochasticInMove_dynamic-------")

#                                         clean or dirty  (0,0),   (1,0),   (0,1)
env = environments.env_fullyObs_stochasticInMove_dynamic("dirty", "clean", "dirty")
agent = agents.ag_fullyObs_stochasticInMove_dynamic(env)

agent.run()
print("\n")


print("-------fullyObs_stochasticInVac_static-------")

#                                       clean or dirty  (0,0),   (1,0),   (0,1)
env = environments.env_fullyObs_stochasticInVac_static("dirty", "clean", "dirty")
agent = agents.ag_fullyObs_stochasticInVac_static(env)

agent.run()
print("\n")


print("-------fullyObs_stochasticInVac_dynamic-------")

#                                        clean or dirty  (0,0),   (1,0),   (0,1)
env = environments.env_fullyObs_stochasticInVac_dynamic("dirty", "clean", "dirty")
agent = agents.ag_fullyObs_stochasticInVac_dynamic(env)

agent.run()
print("\n")


print("-------noCleanSensor_deterministic_static-------")

#                                          clean or dirty  (0,0),   (1,0),   (0,1)
env = environments.env_noCleanSensor_deterministic_static("dirty", "clean", "dirty")
agent = agents.ag_noCleanSensor_deterministic_static(env)

agent.run()
print("\n")


print("-------noCleanSensor_deterministic_dynamic-------")

#                                           clean or dirty  (0,0),   (1,0),   (0,1)
env = environments.env_noCleanSensor_deterministic_dynamic("dirty", "clean", "dirty")
agent = agents.ag_noCleanSensor_deterministic_dynamic(env)

agent.run()
print("\n")


print("-------noCleanSensor_stochasticInMove_static-------")

#                                             clean or dirty  (0,0),   (1,0),   (0,1)
env = environments.env_noCleanSensor_stochasticInMove_static("dirty", "clean", "dirty")
agent = agents.ag_noCleanSensor_stochasticInMove_static(env)

agent.run()
print("\n")


print("-------noCleanSensor_stochasticInMove_dynamic-------")

#                                              clean or dirty  (0,0),   (1,0),   (0,1)
env = environments.env_noCleanSensor_stochasticInMove_dynamic("dirty", "clean", "dirty")
agent = agents.ag_noCleanSensor_stochasticInMove_dynamic(env)

agent.run()
print("\n")


print("-------noCleanSensor_stochasticInVac_static-------")

#                                            clean or dirty  (0,0),   (1,0),   (0,1)
env = environments.env_noCleanSensor_stochasticInVac_static("dirty", "clean", "dirty")
agent = agents.ag_noCleanSensor_stochasticInVac_static(env)

agent.run()
print("\n")


print("-------noCleanSensor_stochasticInVac_dynamic-------")

#                                             clean or dirty  (0,0),   (1,0),   (0,1)
env = environments.env_noCleanSensor_stochasticInVac_dynamic("dirty", "clean", "dirty")
agent = agents.ag_noCleanSensor_stochasticInVac_dynamic(env)

agent.run()
print("\n")


print("-------noPositionSensor_deterministic_static-------")

#                                             clean or dirty  (0,0),   (1,0),   (0,1)
env = environments.env_noPositionSensor_deterministic_static("dirty", "clean", "dirty")
agent = agents.ag_noPositionSensor_deterministic_static(env)

agent.run()
print("\n")


print("-------noPositionSensor_deterministic_dynamic-------")

#                                              clean or dirty  (0,0),   (1,0),   (0,1)
env = environments.env_noPositionSensor_deterministic_dynamic("dirty", "clean", "dirty")
agent = agents.ag_noPositionSensor_deterministic_dynamic(env)

agent.run()
print("\n")

print("-------noPositionSensor_stochasticInMove_static-------")

#                                                clean or dirty  (0,0),   (1,0),   (0,1)
env = environments.env_noPositionSensor_stochasticInMove_static("dirty", "clean", "dirty")
agent = agents.ag_noPositionSensor_stochasticInMove_static(env)

agent.run()
print("\n")


print("-------noPositionSensor_stochasticInMove_dynamic-------")

#                                                 clean or dirty  (0,0),   (1,0),   (0,1)
env = environments.env_noPositionSensor_stochasticInMove_dynamic("dirty", "clean", "dirty")
agent = agents.ag_noPositionSensor_stochasticInMove_dynamic(env)

agent.run()
print("\n")


print("-------noPositionSensor_stochasticInVac_static-------")

#                                               clean or dirty  (0,0),   (1,0),   (0,1)
env = environments.env_noPositionSensor_stochasticInVac_static("dirty", "clean", "dirty")
agent = agents.ag_noPositionSensor_stochasticInVac_static(env)

agent.run()
print("\n")


print("-------noPositionSensor_stochasticInVac_dynamic-------")

#                                                clean or dirty  (0,0),   (1,0),   (0,1)
env = environments.env_noPositionSensor_stochasticInVac_dynamic("dirty", "clean", "dirty")
agent = agents.ag_noPositionSensor_stochasticInVac_dynamic(env)

agent.run()
print("\n")



# 100 tests
print("testing 100 steps")


def run_simulation(env, agent, steps=100):
    total_f1 = 0
    total_f2 = 0
    total_f3 = 0
    total_f4 = 0
    total_f5 = 0

    for _ in range(steps):
        agent.run()  
        total_f1 += agent.f1
        total_f2 += agent.f2
        total_f3 += agent.f3
        total_f4 += agent.f4
        total_f5 += agent.f5

    print(f"Total f1: {total_f1}, Total f2: {total_f2}, Total f3: {total_f3}, Total f4: {total_f4}, Total f5: {total_f5}")
    print("\n")



print("-------fullyObs_deterministic_static-------")
env = environments.env_fullyObs_deterministic_static("dirty", "clean", "dirty")
agent = agents.ag_fullyObs_deterministic_static(env)
run_simulation(env, agent)

print("-------fullyObs_deterministic_dynamic-------")
env = environments.env_fullyObs_deterministic_dynamic("dirty", "clean", "dirty")
agent = agents.ag_fullyObs_deterministic_dynamic(env)
run_simulation(env, agent)

print("-------fullyObs_stochasticInMove_static-------")
env = environments.env_fullyObs_stochasticInMove_static("dirty", "clean", "dirty")
agent = agents.ag_fullyObs_stochasticInMove_static(env)
run_simulation(env, agent)

print("-------fullyObs_stochasticInMove_dynamic-------")
env = environments.env_fullyObs_stochasticInMove_dynamic("dirty", "clean", "dirty")
agent = agents.ag_fullyObs_stochasticInMove_dynamic(env)
run_simulation(env, agent)

print("-------fullyObs_stochasticInVac_static-------")
env = environments.env_fullyObs_stochasticInVac_static("dirty", "clean", "dirty")
agent = agents.ag_fullyObs_stochasticInVac_static(env)
run_simulation(env, agent)

print("-------fullyObs_stochasticInVac_dynamic-------")
env = environments.env_fullyObs_stochasticInVac_dynamic("dirty", "clean", "dirty")
agent = agents.ag_fullyObs_stochasticInVac_dynamic(env)
run_simulation(env, agent)

print("-------noCleanSensor_deterministic_static-------")
env = environments.env_noCleanSensor_deterministic_static("dirty", "clean", "dirty")
agent = agents.ag_noCleanSensor_deterministic_static(env)
run_simulation(env, agent)

print("-------noCleanSensor_deterministic_dynamic-------")
env = environments.env_noCleanSensor_deterministic_dynamic("dirty", "clean", "dirty")
agent = agents.ag_noCleanSensor_deterministic_dynamic(env)
run_simulation(env, agent)

print("-------noCleanSensor_stochasticInMove_static-------")
env = environments.env_noCleanSensor_stochasticInMove_static("dirty", "clean", "dirty")
agent = agents.ag_noCleanSensor_stochasticInMove_static(env)
run_simulation(env, agent)

print("-------noCleanSensor_stochasticInMove_dynamic-------")
env = environments.env_noCleanSensor_stochasticInMove_dynamic("dirty", "clean", "dirty")
agent = agents.ag_noCleanSensor_stochasticInMove_dynamic(env)
run_simulation(env, agent)

print("-------noCleanSensor_stochasticInVac_static-------")
env = environments.env_noCleanSensor_stochasticInVac_static("dirty", "clean", "dirty")
agent = agents.ag_noCleanSensor_stochasticInVac_static(env)
run_simulation(env, agent)

print("-------noCleanSensor_stochasticInVac_dynamic-------")
env = environments.env_noCleanSensor_stochasticInVac_dynamic("dirty", "clean", "dirty")
agent = agents.ag_noCleanSensor_stochasticInVac_dynamic(env)
run_simulation(env, agent)

print("-------noPositionSensor_deterministic_static-------")
env = environments.env_noPositionSensor_deterministic_static("dirty", "clean", "dirty")
agent = agents.ag_noPositionSensor_deterministic_static(env)
run_simulation(env, agent)

print("-------noPositionSensor_deterministic_dynamic-------")
env = environments.env_noPositionSensor_deterministic_dynamic("dirty", "clean", "dirty")
agent = agents.ag_noPositionSensor_deterministic_dynamic(env)
run_simulation(env, agent)

print("-------noPositionSensor_stochasticInMove_static-------")
env = environments.env_noPositionSensor_stochasticInMove_static("dirty", "clean", "dirty")
agent = agents.ag_noPositionSensor_stochasticInMove_static(env)
run_simulation(env, agent)

print("-------noPositionSensor_stochasticInMove_dynamic-------")
env = environments.env_noPositionSensor_stochasticInMove_dynamic("dirty", "clean", "dirty")
agent = agents.ag_noPositionSensor_stochasticInMove_dynamic(env)
run_simulation(env, agent)

print("-------noPositionSensor_stochasticInVac_static-------")
env = environments.env_noPositionSensor_stochasticInVac_static("dirty", "clean", "dirty")
agent = agents.ag_noPositionSensor_stochasticInVac_static(env)
run_simulation(env, agent)

print("-------noPositionSensor_stochasticInVac_dynamic-------")
env = environments.env_noPositionSensor_stochasticInVac_dynamic("dirty", "clean", "dirty")
agent = agents.ag_noPositionSensor_stochasticInVac_dynamic(env)
run_simulation(env, agent)
