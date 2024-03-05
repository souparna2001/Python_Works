def start_end(fn):
    def wrapper():
        data=f"<b>{fn()}</b>"
        return data
    return wrapper    


@start_end
def get_hello():
    return "hello"

@start_end
def get_hai():
    return "hai"

print(get_hai())
print(get_hello())