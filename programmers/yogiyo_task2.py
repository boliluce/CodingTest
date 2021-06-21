import re

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
def solution(s):
    count = 0;
    file = re.sub(r"\n ", '\n', re.sub(r" + ", ' ', s)).split('\n')
    for i in file:
        tmp = i.split(' ')
        if tmp[0]=='': continue
        if int(tmp[3]) < 1990: continue
        if months.index(tmp[2]) < 1: continue
        # 31 Jan 1990 이상
        if 240*2**10 <= int(tmp[0]):
            count+=1

    return "NO FILES" if count==0 else count


s = """ 
1779091968 23 Sep 2009 system.zip
 779091968 23 Sep 2009 system.zip
 284164096 14 Aug 2013 to-do-list.xml
 714080256 19 Jun 2013 blockbuster.mpeg
       329 12 Dec 2010 notes.html
 444596224 17 Jan 1950 delete-this.zip
       641 24 May 1987 setup.png
    245760 16 Jul 2005 archive.zip
 839909376 31 Jan 1990 library.dll
 """

print(solution(s))

# print(s)
# s = re.sub(r" + ", ' ', s)
# print(s)