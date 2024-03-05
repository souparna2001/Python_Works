def helo_decorator(fn):
     def wrapper(user):
         data="Hello "+fn(user)
         return data
     return wrapper

@helo_decorator
def morning_greeting(user):
    return f"good morning {user}"

@helo_decorator
def afternoon_greeting(user):
    return f"good afternoon {user}"
 
@helo_decorator
def evening_greeting(user):
    return f"good evening {user}"

@helo_decorator
def night_greeting(user):
    return f"good night {user}"

print(morning_greeting("souparna"))
print(afternoon_greeting("najiya"))
print(evening_greeting("mugadhri"))
print(night_greeting("sandra"))


