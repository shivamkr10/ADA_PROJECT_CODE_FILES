from graph import *

class Patient:
    def __init__(self):
        self.user_id=0
        self.password=''
        self.name=''
        self.don_name=''
        self.matched='NO'
        self.don_blood=''
        #self.pair_matched=Vertex(0)
        self.pref_list=[]
    
    def getdata(self,user_id,password):
        self.user_id=user_id
        self.password=password

    def getnames(self,name,don_name,blood):
        self.name=name
        self.don_name=don_name
        self.don_blood=blood

    # def setdata(self,matched_pair=Vertex):
    #     self.pair_matched=matched_pair
    #     if matched_pair:
    #         self.matched='Yes'
    #     else:
    #         self.matched='No'
    
    def get_pref(self,pref_list):
        self.pref_list=pref_list.split(',')

    def check_pass(self,uid,confirm):
        if(self.password==confirm and self.user_id==uid):
            return True
        else:
            return False


class admin:
    def __init__(self):
        self.user_name=''
        self.password=''

    def getdata(self,user_name,password):
        self.user_name=user_name
        self.password=password

    def check_pass(self,uid,confirm):
        if(self.password==confirm and self.user_id==uid):
            return True
        else:
            return False

    