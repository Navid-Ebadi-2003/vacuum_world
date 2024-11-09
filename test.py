import environments
import agents

# print("-------fullyObs_deterministic_static-------")

# #                                     clean or dirty  (0,0),   (1,0),   (0,1)
# env = environments.env_fullyObs_deterministic_static("dirty", "clean", "dirty")
# agent = agents.ag_fullyObs_deterministic_static(env)

# agent.run()
# print("\n")


# print("-------fullyObs_deterministic_dynamic-------")

# #                                     clean or dirty  (0,0),   (1,0),   (0,1)
# env = environments.env_fullyObs_deterministic_dynamic("dirty", "clean", "dirty")
# agent = agents.ag_fullyObs_deterministic_dynamic(env)

# agent.run()
# print("\n")


# print("-------fullyObs_stochasticInMove_static-------")

# #                                     clean or dirty  (0,0),   (1,0),   (0,1)
# env = environments.env_fullyObs_stochasticInMove_static("dirty", "clean", "dirty")
# agent = agents.ag_fullyObs_stochasticInMove_static(env)

# agent.run()
# print("\n")


# print("-------fullyObs_stochasticInMove_dynamic-------")

# #                                     clean or dirty  (0,0),   (1,0),   (0,1)
# env = environments.env_fullyObs_stochasticInMove_dynamic("dirty", "clean", "dirty")
# agent = agents.ag_fullyObs_stochasticInMove_dynamic(env)

# agent.run()
# print("\n")


# print("-------fullyObs_stochasticInVac_static-------")

# #                                     clean or dirty  (0,0),   (1,0),   (0,1)
# env = environments.env_fullyObs_stochasticInVac_static("dirty", "clean", "dirty")
# agent = agents.ag_fullyObs_stochasticInVac_static(env)

# agent.run()
# print("\n")


# print("-------fullyObs_stochasticInVac_dynamic-------")

# #                                     clean or dirty  (0,0),   (1,0),   (0,1)
# env = environments.env_fullyObs_stochasticInVac_dynamic("dirty", "clean", "dirty")
# agent = agents.ag_fullyObs_stochasticInVac_dynamic(env)

# agent.run()
# print("\n")


# print("-------noCleanSensor_deterministic_static-------")

# #                                     clean or dirty  (0,0),   (1,0),   (0,1)
# env = environments.env_noCleanSensor_deterministic_static("dirty", "clean", "dirty")
# agent = agents.ag_noCleanSensor_deterministic_static(env)

# agent.run()
# print("\n")


# print("-------noCleanSensor_deterministic_dynamic-------")

# #                                     clean or dirty  (0,0),   (1,0),   (0,1)
# env = environments.env_noCleanSensor_deterministic_dynamic("dirty", "clean", "dirty")
# agent = agents.ag_noCleanSensor_deterministic_dynamic(env)

# agent.run()
# print("\n")


# print("-------noCleanSensor_stochasticInMove_static-------")

# #                                     clean or dirty  (0,0),   (1,0),   (0,1)
# env = environments.env_noCleanSensor_stochasticInMove_static("dirty", "clean", "dirty")
# agent = agents.ag_noCleanSensor_stochasticInMove_static(env)

# agent.run()
# print("\n")


# print("-------noCleanSensor_stochasticInMove_dynamic-------")

# #                                     clean or dirty  (0,0),   (1,0),   (0,1)
# env = environments.env_noCleanSensor_stochasticInMove_dynamic("dirty", "clean", "dirty")
# agent = agents.ag_noCleanSensor_stochasticInMove_dynamic(env)

# agent.run()
# print("\n")


# print("-------noCleanSensor_stochasticInVac_static-------")

# #                                     clean or dirty  (0,0),   (1,0),   (0,1)
# env = environments.env_noCleanSensor_stochasticInVac_static("dirty", "clean", "dirty")
# agent = agents.ag_noCleanSensor_stochasticInVac_static(env)

# agent.run()
# print("\n")


# print("-------noCleanSensor_stochasticInVac_dynamic-------")

# #                                     clean or dirty  (0,0),   (1,0),   (0,1)
# env = environments.env_noCleanSensor_stochasticInVac_dynamic("dirty", "clean", "dirty")
# agent = agents.ag_noCleanSensor_stochasticInVac_dynamic(env)

# agent.run()
# print("\n")


print("-------noPositionSensor_deterministic_static-------")

#                                     clean or dirty  (0,0),   (1,0),   (0,1)
env = environments.env_noPositionSensor_deterministic_static("dirty", "clean", "dirty")
agent = agents.ag_noPositionSensor_deterministic_static(env)

agent.run()
print("\n")