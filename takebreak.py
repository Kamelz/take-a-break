import webbrowser
import time


#  ------------------------- App functions --------------------------------

# opens the requested url in the browser


def OpenInBrowser(url):
    webbrowser.open(url)


# evaluating the requested job and runs the targeted function.


def run(job):
    eval(job)

# run a job with a timeout by seconds


def operation(job, timer):
    time.sleep(timer)
    run(job)


# schedule repeatativ or nonrepetativ job with a timeout by seconds


def ScheduleJob(job, timer, repeat=False):
    if(repeat):
        while True:
            print(time.ctime())
            operation(job, timer)
    else:
        print(time.ctime())
        operation(job, timer)


# -------------------------Main app body--------------------------------

url = 'https://www.youtube.com/watch?v=JGwWNGJdvx8'

# 2h
# timer = 7200
timer = 6

job = "OpenInBrowser('" + url + "')"

ScheduleJob(job, timer, True)
