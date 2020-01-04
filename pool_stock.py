from multiprocessing import Pool
import os, time, random
import peg
import glob


def long_time_task(name, x):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    #time.sleep(random.random() * 3)
    peg.get_peg_from_csv(x)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))

def run():
    print('Parent process %s.' % os.getpid())
    path = './'
    extension = 'csv'
    os.chdir(path)
    result = [i for i in glob.glob('output*.{}'.format(extension))]
    length = len(result)
    print('files count is ',length)

    p = Pool(length)
    i = 0
    for x in result:
        print(x)
        p.apply_async(long_time_task, args=(i,x,))
        ++i
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')

if __name__=='__main__':
    run()
