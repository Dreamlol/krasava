class Student(object):
    exam = 0
    
    def __init__(self, name, di):
        self.name = name
        self.di=di
        self.labs=[0  for i in range(0,di['lab_num'])]
        
    def make_lab(self, mark, number = None):
        self.mark=mark
        if mark > self.di['lab_max']:
            self.mark = self.di['lab_max']
        if number == None:
            for j in range(len(self.labs)):
                if self.labs[j] == 0:
                    self.labs[j] = self.mark
                break
        else:
            self.labs[number-1] = self.mark
    
    def make_exam(self, exam):
        self.exam = exam
        if exam > self.di['exam_max']:
            self.exam = self.di['exam_max']
        return self.exam    
    
    def is_certified(self):
        su = sum(self.labs)
    
dictionary = {
'exam_max': 30,
'lab_max': 7,
'lab_num': 10,
'k': 0.61,
}
a=Student('Vasya', dictionary)
a.make_lab(6.5,7)
a.make_lab(4)
a.make_exam(43)
a.is_certified()
