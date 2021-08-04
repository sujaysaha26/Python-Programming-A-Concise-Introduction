def problem2_8(temp_list):
    sum_ = 0
    for item in range(len(temp_list)):
        sum_ = sum_ + temp_list[item]
        
    average = sum_ / len(temp_list)    
    print("Average:", average)
    print("High:", max(temp_list))
    print("Low:", min(temp_list))
    