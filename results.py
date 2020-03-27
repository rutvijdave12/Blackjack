from player import *
class Results:
    #player_final_value = 0
    #computer_final_value = 0

    def Decipher(self,cards):
        nums = []
        for name,val in cards:
            if type(val) is int:
                nums.append(val)
            else:
                nums.append(val[1])
                   
        return nums
        

    def total_check(self,value,nums):
        #print(value)
        if value>21:
            if 11 in nums:
                nums[nums.index(11)] = 1
                return self.total_check(sum(nums),nums)
            else:    
                return value
        elif value<=21:
            #Results.player_final_value = value
            return value  



    # def Decipher_comp(self,cards):
    #     nums = []
    #     for name,val in cards:
    #         if type(val) is int:
    #             nums.append(val)
    #         else:
    #             nums.append(val[1]) 

    #     return self.comp_total_check(sum(nums),nums)



    # def comp_total_check(self,value,nums):
    #     #print(value)
    #     if value>21:
    #         if 11 in nums:
    #             nums[nums.index(11)] = 1
    #             return self.total_check(sum(nums),nums)
    #         else:    
    #             return value
    #     elif value<=21:
    #         Results.computer_final_value = value
    #         return value  


    def final_result(self,comp_final_value,player_final_value):
        if comp_final_value>player_final_value:
            print("Computer won!")
        elif player_final_value>comp_final_value:
            return True
        else:
            print("PUSH")   
            return "PUSH"     

