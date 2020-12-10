#Write a function called oops that explicitly raises an IndexError exception when called.
# Then write another function that calls oops inside a try/except state­ment to catch the error.
# What happens if you change oops to raise KeyError instead of IndexError?

def oops():
    raise IndexError()


def catch_oops():
    try:
        oops()
    except IndexError as err:
        print(f'Catch it! \n {type(err)}')
    except:
        print('Houston, we have problem!!!')
        raise

catch_oops()