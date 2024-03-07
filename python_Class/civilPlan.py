# create a class and instances with initializing the constructor.

class HomePlan:
    def __init__(self, length, breadth, kitchen_length, kitchen_breadth,
                 bathroom_length, bathroom_breadth,
                 deityroom_length, deityroom_breadth,
                 livingroom_length, livingroom_breadth):
        self.length = length
        self.breadth = breadth
        self.kitchen_length = kitchen_length
        self.kitchen_breadth = kitchen_breadth
        self.bathroom_length = bathroom_length
        self.bathroom_breadth = bathroom_breadth
        self.livingroom_length = livingroom_length
        self.livingroom_breadth = livingroom_breadth
        self.deityroom_length = deityroom_length
        self.deityroom_breadth = deityroom_breadth



    def sqr(self, item1, item2):
        return (item1 * item2) / 100

    def totalsqr(self, items):
        count = 0
        for i in items:
            count+=i
        return count

    def kitchen(self):
        kitchensqr = HomePlan.sqr(self, self.kitchen_length, self.kitchen_breadth)
        print(f'the sqr of kitchen is : {kitchensqr}')


    def bathroom(self):
        bathroomsqr = HomePlan.sqr(self, self.bathroom_length, self.bathroom_breadth)
        print(f'the sqr of bathroom is : {bathroomsqr}')

    def livingroom(self):
        livingroomsqr = HomePlan.sqr(self, self.livingroom_length, self.livingroom_breadth)
        print(f'the sqr of livingroom is : {livingroomsqr}')

    def deityroom(self):
        deityroomsqr = HomePlan.sqr(self, self.deityroom_length, self.deityroom_breadth)
        print(f'the sqr of deityroom is : {deityroomsqr}')


vinay = HomePlan(40, 30,
                 9,9,
                 6, 6,
                 5, 3,
                 13, 18)

vinay.kitchen()
vinay.bathroom()
vinay.deityroom()
vinay.livingroom()
# vinay.sqr(34, 43)