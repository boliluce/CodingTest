def solution(a,b):
    #weeks = ['SUN','MON','TUE','WED','THU','FRI','SAT']
    weeks = ['FRI','SAT','SUN','MON','TUE','WED','THU']
    months = [31,29,31,30,31,30,31,31,30,31,30,31]
    #months = [0,31,60,91,121,152,182,213,244,274,305,335]
    #return weeks[(months[a-1]+b-1)%7]
    return weeks[(sum(months[:a-1])+b-1)%7]

print(solution(5,24))
print(solution(12,29))
print(solution(1,1))