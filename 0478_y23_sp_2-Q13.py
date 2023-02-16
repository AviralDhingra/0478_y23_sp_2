# INITIALISATION OF ARRAYS

import numpy as np

StudentName = np.array(['John', 'Mary', 'Peter', 'Susan',
                       'Jane', 'Tom', 'Alice', 'Bob', 'Bill', 'Jack'])

SubjectNo = 5
ClassSize = StudentName.shape[0]

StudentMark = np.random.randint(1, 100, (ClassSize, SubjectNo))

# PROGRAM

# 1. calculates the combined total mark for each student for all their subjects


def TotalMark(StudentMark):
    return np.sum(StudentMark, axis=1)

# 2. calculates the average mark for each student for all their subjects


def AverageMark(StudentMark):
    return np.mean(StudentMark, axis=1)

# 3. calculates the combined total mark for each subject for all students


def TotalSubjectMark(StudentMark):
    return np.sum(StudentMark, axis=0)

# 4. calculates grade awarded through average marks for each student for all their subjects


def Grade(StudentMark):
    AverageMark = np.mean(StudentMark, axis=1)
    Grade = np.where(AverageMark >= 70, 'Distinction',
                     np.where(AverageMark >= 55, 'Merit',
                              np.where(AverageMark >= 40, 'Pass', 'Fail')
                              ))
    return Grade


if __name__ == '__main__':
    import pprint
    pr = pprint.PrettyPrinter(indent=4)

    print('Student Names: ', StudentName)
    print('Student Marks: ', end='')
    pr.pprint((StudentMark))
    print('\n\n')

    for i in range(StudentName.shape[0]):
        Student = StudentName[i]
        print(f'Name: {Student}')
        print(f'Combined Total Mark: {TotalMark(StudentMark)[i]}')
        print(f'Average Mark: {AverageMark(StudentMark)[i]}')
        print(f'Grade Awarded: {Grade(StudentMark)[i]}')
        print('--------------------------')
