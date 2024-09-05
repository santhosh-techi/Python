Incorrect_amount_tickets_prize_list=[12,21,31,13,23,25]

def _corrected_amount_and_sum(list):
    Total_sum=0
    correct_amount_tickets_prize_list=[]
    for i in range(len(list)):
        Num=str(list[i])
        correct_number=int(Num[::-1])
        Total_sum+=correct_number
        correct_amount_tickets_prize_list.append(correct_number)
    return correct_amount_tickets_prize_list, Total_sum

corrected_list,amount_sum=_corrected_amount_and_sum(Incorrect_amount_tickets_prize_list)
print(f'the corrected ticket prize list is : {corrected_list} and the total amount collected for the day is {amount_sum}')