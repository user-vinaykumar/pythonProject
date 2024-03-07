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

    def sqrList(self, value1, value2, value3, value4):
        sqrInList = []
        sqrInList.append(value1)
        sqrInList.append(value2)
        sqrInList.append(value3)
        sqrInList.append(value4)
        return sqrInList

    def totalsqr(self, items):
        count = sum(items)
        print(f'the total chadara of the portions are : {count}')

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

vk = vinay.kitchen()
vb = vinay.bathroom()
vd = vinay.deityroom()
vl = vinay.livingroom()


sqr_valuesvinay = vinay.sqrList(vinay.sqr(vinay.kitchen_length, vinay.kitchen_breadth),
                                vinay.sqr(vinay.bathroom_length, vinay.bathroom_breadth),
                                vinay.sqr(vinay.deityroom_length, vinay.deityroom_breadth),
                                vinay.sqr(vinay.livingroom_length, vinay.livingroom_breadth))
vinay.totalsqr(sqr_valuesvinay)
print(f'*******************************************')

sharan = HomePlan(30, 40,
                  10, 10,
                  5, 5,
                  13, 13,
                  3, 5)
print('---------------------')

sk = sharan.kitchen()
sb = sharan.bathroom()
sl = sharan.livingroom()
sd = sharan.deityroom()

sqr_valuessharan = sharan.sqrList(sharan.sqr(sharan.kitchen_length, sharan.kitchen_breadth),
                                  sharan.sqr(sharan.bathroom_length, sharan.bathroom_breadth),
                                  sharan.sqr(sharan.deityroom_length, sharan.deityroom_breadth),
                                  sharan.sqr(sharan.livingroom_length, sharan.livingroom_breadth))


sharan.totalsqr(sqr_valuessharan)
# vinay.sqr(34, 43)

