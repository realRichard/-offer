def log(*args, **kwargs):
    print(*args, **kwargs)


def ensure(condition, message):
    if condition:
        log('success')
    else:
        log('fail', message)
