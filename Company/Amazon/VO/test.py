class Solution:
    def __init__(self, num_string):
        self.string = num_string

    def decode_num(self):
        return self.helper(self.string)

    def helper(self, num):
        if not len(num):
            return ['']
        if len(num) == 1:
            return [self.num_to_alpha(int(num))]
        num1 = num[1:]
        list1 = [self.num_to_alpha(int(num[0])) + x for x in self.helper(num1)]
        num2 = num[2:]
        list2 = [self.num_to_alpha(int(num[0:2])) + x for x in self.helper(num2)] if int(num[0:2]) <= 26 else []
        return list1 + list2

    @staticmethod
    def num_to_alpha(num):
        return chr(num + 96)


a = Solution('123')
print(a.decode_num())