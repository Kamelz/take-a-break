import time
import webbrowser

#  ------------------------- App functions --------------------------------

# opens the requested url in the browser


def OpenInBrowser(url):
    webbrowser.open(url)


# evaluating the requested job and runs the targeted function.


def run(job):
    eval(job)

# run a job with with a timeout by seconds


def operation(job, timer):
    run(job)
    time.sleep(timer)

# schedule repeatativ or nonrepetativ job with a timeout by seconds


def ScheduleJob(job, time, repeat=False):
    if(repeat):
        while True:
            operation(job, timer)
    else:
        operation(job, timer)


# -------------------------Main app body--------------------------------

url = 'https://www.youtube.com/watch?v=ejvpVhvKesM'

# 2h
timer = 7200

job = "OpenInBrowser('" + url + "')"

ScheduleJob(job, timer, True)
