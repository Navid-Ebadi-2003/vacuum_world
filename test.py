import environments
import agents

print("-------fullyObs_deterministic_static-------")

#                                     clean or dirty  (0,0),   (1,0),   (0,1)
env = environments.env_fullyObs_deterministic_static("dirty", "clean", "dirty")
agent = agents.ag_fullyObs_deterministic_static(env)

agent.run()
print("\n")


# print("-------fullyObs_deterministic_dynamic-------")

# #                                     clean or dirty  (0,0),   (1,0),   (0,1)
# env = environments.env_fullyObs_deterministic_dynamic("dirty", "clean", "dirty")
# agent = agents.ag_fullyObs_deterministic_dynamic(env)

# agent.run()
# print("\n")