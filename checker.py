class IDChecker():
    def __init__(self, turkish_id):
        self.turkish_id = turkish_id
        
    def convert(id):
        """Gets user input, Turkish National ID
            and returns integer array filled with digits of the input
        
        Parameters
        ----------
        id : str
            User input. Turkish National ID in string format

        Returns
        -------
        list
            a list of integers split digit-by-digit
        """
        num = []
        for i in range(len(id)):
            num.append(int(id[i]))

        return num

    def takesum(id):
        """Gets integer array
            and returns sums for specific calculations.
        
        Parameters
        ----------
        id : list
            User input. Turkish National ID as list of integers

        Returns
        -------
        result : int
            The remainder from: 
            The sum of: 1st, 3rd, 5th, 7th and 9th digits multiplied by seven,
            decremented by the sum of: 2nd, 4th, 6th and 8th digits, 
            divided by 10
        
        result_ten : int
            The remainder from the sum of the first 10 digits, 
            divided by 10
        """
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
        """Gets user input, Turkish National ID
            and returns the result of validation
        
        Parameters
        ----------
        id : str
            User input. Turkish National ID in string format

        Returns
        -------
        str
            Validation result
        """
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