class IDChecker():
    def __init__(self, turkish_id):
        self.turkish_id = turkish_id
        
    def convert(id):
        num = []
        for i in range(len(id)):
            num.append(int(id[i]))

        return num

    def takesum(id):
        sum = 0
        sum_ten = 0
        for idx in range(len(id) - 2):
            if ((idx+1) % 2 != 0):
                sum += id[idx] * 7
                sum_ten += id[idx]
            else:
                sum -= id[idx]
                sum_ten += id[idx]

        sum_ten += id[-2]

        result = sum % 10
        result_ten = sum_ten % 10

        return result, result_ten

    def takeID(id):
        res = 0
        id = list(id)
        if (len(id) == 11 and id[0] != '0'):
            try:
                num_id = IDChecker.convert(id)
                res, res_ten = IDChecker.takesum(num_id)

                if (num_id[-2] == res and num_id[-1] == res_ten):
                    return "Valid!"
                else:
                    return "Not a valid ID!"

            except:
                return "ID should contain only integers."
        else:
            return "Please enter a valid id"