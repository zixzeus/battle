import json
class States():
    def __init__(self,obs_side):
        self.obs_side = obs_side
        # self.dic = self.to_dict()
        self.platform_infos = self.obs_side["platforminfos"]
        self.track_infos = self.obs_side["trackinfos"]
        self.missile_infos = self.obs_side["missileinfos"]

    def get_platform_infos(self):
        return self.obs_side["platforminfos"]

    def get_track_infos(self):
        return self.obs_side["trackinfos"]

    def get_missile_infos(self):
        return self.obs_side["missileinfos"]

    @property
    def available_aircrafts(self):
        for obs in self.obs_side:
            pass

    def available_actions(self):
        sim_time = self.platform_infos[0]["CurTime"]
        actions=[]
        attack_list=[]
        target_list=[]

        if sim_time<3:
            actions.append(0)
            actions.append(1)
            # return actions

        if sim_time>=3:
            actions.append(0)
            actions.append(6)
        for pl_info in self.platform_infos:
            if pl_info["Availability"]==1.0 and pl_info["LeftWeapon"]>0:
                attack_list.append(pl_info["ID"])

        for tk_info in self.track_infos:
            if tk_info["Availability"]==1.0:
                target_list.append(tk_info["ID"])

        # actions=[1,2,3,4,5,6]

        return actions



if __name__ == "__main__":
    st = States("obs_side.json")
    print(st.get_platform_infos())
    print(len(st.get_platform_infos()))