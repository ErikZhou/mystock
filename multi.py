from multiprocessing import Process
import os
import peg
import glob

# 子进程要执行的代码
def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))
    peg.get_peg_from_csv(name)

def create_process (name):
    p = Process(target=run_proc, args=(name,))
    print('Child process will start.')
    p.start()
    p.join()
    print('Child process end.')

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())

path = './'
extension = 'csv'
os.chdir(path)
result = [i for i in glob.glob('output*.{}'.format(extension))]
jobs = []
length = len(result)
print('files count is ',length)
for x in result:
    print(x)
    #jobs.append(x)
    create_process(x)

#print(jobs)
#p = Pool(len(jobs))
#p.map(get_peg_from_csv, jobs)


