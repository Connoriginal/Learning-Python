class BringLogin:

    @staticmethod
    def load_members():
        file_ = open("members.txt","r")
        members={}
        for line in file_:
            name, moneyleft, wins, playtime= line.strip("\n").split(",")
            members[name] = (moneyleft, wins, playtime)
        file_.close()
        return members

    @staticmethod
    def store_members(members):
        file_ = open('members.txt',"w")
        names = members.keys()
        for name in names:
            moneyleft = members[name][0]
            wins = members[name][1]
            playtime = members[name][2]
            line = name + "," + str(moneyleft) + "," +str(wins)+","+str(playtime)+ "\n"
            file_.write(line)
        file_.close()
