def same_frequency(num1, num2):
    result_for_num = []
    result = []
    for num_1 in str(num1):
        for num_2 in str(num2):
            # print('num_1 is ' + num_1)
            # print('num_2 is ' + num_2)
            # print('result before')
            # print(result_for_num)
            if num_1 == num_2:
                result_for_num.append(True)
                # print('result after ')
                # print(result_for_num)
            else:
                result_for_num.append(False)
        if any(result_for_num):
            result.append(True)
            result_for_num = []
            # print('fffffffffffinal result is ')
            # print (result)
        else:
            result.append(False)
            result_for_num = []
            # print('fffffffffffinal result is ')
            # print (result)
    if all(result):
        return True
        # print('the freq is the same!')
    else:
        return False
    

    # """Do these nums have same frequencies of digits?
    
    #     >>> same_frequency(551122, 221515)
    #     True
        
    #     >>> same_frequency(321142, 3212215)
    #     False
        
    #     >>> same_frequency(1212, 2211)
    #     True
    # """