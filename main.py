from queenconfig import *
from solution import *

# Steepest Ascent without sideway move method
total = 0
f_steps = 0
f_cnt = 0
sample_sequences = []
sample_problems = []
for _ in range(500):
    r = steepest_ascent(Problem())
    total += r['outcome']
    f_steps += len(r['solution'])
    f_cnt += abs(1 - r['outcome'])
    if r['outcome']:
        if (r['problem'] not in sample_problems) and (len(sample_problems) < 3):
            sample_problems.append(r['problem'])
            sample_sequences.append(r['solution'])
print('--------Steepest Ascent without sideway move method----------')
print('Success Rate: {:.2f}% | Failure Rate: {:.2f}%'.format(total/5, 100 - total/5))
if f_cnt > 0:
    print('Average steps when it fails: {:.2f}'.format(f_steps/f_cnt))
else:
    print('No fail sample!')
print('Sample search sequences:')
for i, ss in enumerate(sample_sequences):
    print('{}.'.format(i+1))
    for z in ss:
        print(z)
        print('---------------')

# Steepest Ascent with Sideway move up to 100 moves
total = 0
f_steps = 0
f_cnt = 0
sample_sequences = []
sample_problems = []
for _ in range(500):
    r = steepest_ascent(Problem(), allow_sideways=True)
    total += r['outcome']
    f_steps += len(r['solution'])
    f_cnt += abs(1 - r['outcome'])
    if r['outcome']:
        if (r['problem'] not in sample_problems) and (len(sample_problems) < 3):
            sample_problems.append(r['problem'])
            sample_sequences.append(r['solution'])
print('--------Steepest move with sideway move--------')
print('Success Rate: {:.2f}% | Failure Rate: {:.2f}%'.format(total/5, 100 - total/5))
if f_cnt > 0:
    print('Average steps when it fails: {:.2f}'.format(f_steps/f_cnt))
else:
    print('No fail sample!')
print('Sample search sequences:')
for i, ss in enumerate(sample_sequences):
    print('{}.'.format(i+1))
    for z in ss:
        print(z)
        print('---------------')

# Steepest Ascent with Random Restart (no sideway move)
total = 0
f_steps = 0
f_cnt = 0
sample_sequences = []
sample_problems = []
for _ in range(500):
    r = random_restart(Problem().__class__)
    total += r['outcome']
    f_steps += len(r['solution'])
    f_cnt += abs(1 - r['outcome'])
    if r['outcome']:
        if (r['problem'] not in sample_problems) and (len(sample_problems) < 3):
            sample_problems.append(r['problem'])
            sample_sequences.append(r['solution'])
print('------------Steepest ascent with Random Restart----------------')
print('Success Rate: {:.2f}% | Failure Rate: {:.2f}%'.format(total/5, 100 - total/5))
if f_cnt > 0:
    print('Average steps when it fails: {:.2f}'.format(f_steps/f_cnt))
else:
    print('No fail sample!')
print('Sample search sequences:')
for i, ss in enumerate(sample_sequences):
    print('{}.'.format(i+1))
    for z in ss:
        print(z)
        print('---------------')
