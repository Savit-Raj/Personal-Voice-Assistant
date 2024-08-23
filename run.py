# To run Voyage
import multiprocessing


def startVoyage():
    # code for process 1
    print("Process 1 is running")
    from main import start
    start()

# To run HotWord
def listenHotWord():
    # code for process 2
    print("Process 2 is running")
    from engine.features import hotword
    hotword()

if __name__ == '__main__':
    p1 = multiprocessing.Process(target = startVoyage)
    p2 = multiprocessing.Process(target = listenHotWord)

    p1.start()
    p2.start()
    p1.join()

    if p2.is_alive():
        p2.terminate()
        p2.join()

    print("System Stopped")