zoo = ('python', 'elephant', 'penguin')
new_zoo = ('pig', 'monkey', zoo)

print('zoo  is', zoo)
print('zoo length is', len(zoo))
print('new_zoo length is', len(new_zoo))
print('animal count in new_zoo is', len(new_zoo)-1 + len(zoo))