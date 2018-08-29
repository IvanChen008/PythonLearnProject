'''
    真正的并行执行多任务只能在多核CPU上实现，但由于任务数量远远多于核心数量，所以操作系统也会自动把很多任务轮流调度到每个核心上执行。
    对于操作系统来说，一个任务就是一个进程Process，比如打开一个浏览器就是启动一个浏览器进程，有些进程还不止同时干一件事，在一个进程内部，要同时
    干多件事情，就需要同时运行多个子任务，我们把进程内的这些子任务称为线程Thread。
    由于每个进程至少要干一件事，所以一个进程至少有一个线程。当然，就像word这种复杂进程可以有多个线程，多个线程可以同时执行，多线程的执行方式和
    多进程是一样的，也是有操作系统在多个线程之间快速切换，让每个线程都短暂的交替运行，看起来就像同时执行一样。当然，真正地同时执行多线程需要多核cpu才可能实现。

    如果我们要同时执行多个任务怎么办？
    有两种解决方案：
    一种是启动多个进程，每个进程虽然只有一个线程，但多个进程可以一块执行多个任务。
    还有一种方法是启动一个进程，在一个进程内启动多个线程，这样，多个线程也可以一块执行多个任务。
    当然还有第三种方法，就是启动多个进程，每个进程再启动多个线程，这样同时执行的任务就更多了，当然种模型更复杂，实际很少采用。
    同时执行多个任务通常各个任务间并不是没有关联的，而是需要相互通信和协调，有时，任务1必须要暂停等待任务2完成后才能继续执行，有时，任务3和
    任务4又不能同时执行，所以，多进程和多线程的程序的复杂程度要远远高于我们前面写的单进程的程序。
    因为复杂度高，调试困难，所以，不是迫不得已，我们也不想写多任务。但是，有很多时候，没有多任务还真不行。

    线程是最小的执行单元，而进程至少有一个线程，如何调度进程和线程，完全由操作系统决定，程序不能决定什么时候执行执行多长时间。
'''
# 多进程
'''
    想要通过Python程序实现多进程（multiprocessing），需要了解相关的操作系统的知识。
    Unix/Linux操作系统提供了一个fork()系统调用，它非常特殊。普通的函数调用，调用一次，返回一次，但是fork()调用一次，
    返回两次，因为操作系统自动把当前进程（称为父进程）复制了一份（称为子进程），然后，分别在父进程和子进程内返回。
    子进程永远返回0，而父进程返回子进程的ID。这样做的理由是，一个父进程可以fork出很多的子进程，所以父进程要记下每个
    子进程的ID，而子进程只需要调用getppid()就可以拿到父进程的ID。
    Python的os模块封装了常见的系统调用，其中就包括fork，可以在Python程序中轻松创建子进程。
# =====================================
import os

print('Process (%s) start...' % os.getpid())
# Only works on Unix/Linux/Mac:
pid = os.fork()
if pid==0:
    print('I am child process (%s) and my parent is %s.' % (os.getpid(),os.getppid()))
else:
    print('I (%s) just created a child process (%s).' % (os.getpid(),pid)) 
# =====================================
    由于Windows没有fork调用，上面的代码在Windows上无法运行。由于Mac系统是基于BSD（Unix的一种）内核，所以，在Mac下运行
    是没有问题的，推荐大家用Mac学Python！
    有了fork调用，一个进程在接到新任务时就可以复制出一个子进程来处理新任务，常见的Apache服务器就是由父进程监听端口，每当
    有新的Http请求时，就fork出子进程来处理新的http请求。
'''
# multiprocessing
'''
    如果打算编写多进程的服务程序，Unix/Linux无疑是正确的选择。由于Windows没有fork调用，难道在windows上无法用Python编写
    多进程的程序？
    由于Python是跨平台的，自然也应该提供一个跨平台的多进程支持。multiprocessing模块就是跨平台版本的多进程模块。
    multiprocessing模块提供了一个Process类来代表一个进程对象，下面的例子演示了启动一个子进程并等待它结束。

'''
# ====================================
# from multiprocessing import Process
# from multiprocessing import Process
# import os

# def run_proc(name):
#     print('Run child process %s (%s)...' % (name,os.getpid()))

# if __name__=='__main__':
#     print('Parent process %s.' % os.getpid())
#     p = Process(target=run_proc,args=('test',))
#     print('Child process will start.')
#     p.start()
#     p.join()
#     print('Child process end.')
# ====================================
# 2018年8月15日13:25:34
# 多进程 处理 
# 执行结果如下：
# ***********************************
# D:\GitHub\PythonLearnProject\多线程>python 进程和线程.pyParent process 2672.
# Child process will start.
# Run child process test (9696)...
# Child process end.
# ***********************************
# Pool
'''
    如果要启动大量的子进程，可以用进程池的方式批量创建子进程。

from multiprocessing import Pool
import os,time,random

def long_time_task(name):
    print('Run task %s (%s) ...' % (name,os.getpid()))
    start=time.time()
    time.sleep(random.random()*3)
    end=time.time()
    print('Task %s runs %0.2f seconds.' % (name,(end-start)))

if __name__=="__main__":
    print('Parent process %s.' % os.getpid())
    p=Pool(4)
    for i in range(5):
        p.apply_async(long_time_task,args=(i,))
    print('Waiting for all subprocesses done ...')
    p.close()
    p.join()
    print('All subprocesses done.')
'''
# 进程池示例
# 2018年8月15日 13:27:01
# 执行结果如下：
# ***********************************
# D:\GitHub\PythonLearnProject\多线程>python 进程和线程.py
# Parent process 17416.
# Waiting for all subprocesses done ...
# Run task 0 (10504) ...
# Run task 1 (14952) ...
# Run task 2 (15716) ...
# Run task 3 (1892) ...
# Task 1 runs 1.00 seconds.
# Run task 4 (14952) ...
# Task 4 runs 1.46 seconds.
# Task 3 runs 2.80 seconds.
# Task 0 runs 2.85 seconds.
# Task 2 runs 3.00 seconds.
# All subprocesses done.
# ***********************************
'''
    对Pool对象调用join()方法会等待所有子进程执行完毕，调用join()之前必须先调用close()，调用close()之后
    就不能继续添加新的Process了。
    可以注意到输出结果，task 0,1,2,3 是立刻执行的，而task 4要等待前面某个task完成后才执行，这是因为Pool
    的默认大小在我的电脑上是4，因此，最多同时执行4个进程。这是Pool有意设计的限制，并不是操作系统的限制。
    由于Pool的默认大小是CPU的核数，如果你不幸拥有8核CPU，你要提交至少9个子进程才能看到上面的等待效果。
'''
# 子进程
'''
    很多时候，子进程并不是自身，而是一个外部进程。我们创建了子进程后，还需要控制子进程的输入和输出。
    subprocess模块可以让我们非常方便地启动一个子进程，然后控制其输入和输出。
'''
# 进程间通信
'''
    Process之间肯定是需要通信的，操作系统提供了很多机制来实现进程之间的通信。Python的multiprocess模块包装了
    底层的机制，提供了Queue、Pipes等多种方式来交换数据。我们以Queue为例，在父进程中创建两个子进程，一个往Queue
    一个从Queue读数据。

from multiprocessing import Process, Queue
import os,time,random

def write(q):
    print('Process to write: %s' % os.getpid())
    for value in ['A','B','C']:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())

def read(q):
    print('Process to read:%s' % os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from queue.' % value)

if __name__ == '__main__':
    # 父进程创建Queue，并传给各个子进程
    q=Queue()
    pw = Process(target=write,args=(q,))
    pr = Process(target=read,args=(q,))
    pw.start()
    pr.start()
    pw.join()
    pr.terminate()
# =============================
# 2018年8月16日11:04:49
# 进程间的通信测试
# 输出结果：
Process to write: 18616
Put A to queue...
Process to read:3436
Get A from queue.
Put B to queue...
Get B from queue.
Put C to queue...
Get C from queue.
# =============================
# 小结：
# 在Unix/Linux下，multiprocessing模块封装了fork()调用，使我们不需要关注fork()的细节。由于Windows没有
# fork调用，因此，multiprocessing需要模拟出fork的效果，父进程所有Python对象都必须通过pickle序列化再传
# 到子进程去，所以，如果multiprocessing在Windows下调用失败了，要先考虑是不是pickle失败了。
# 
# '''
