def last_digit_calculator(*args,**kwargs):
    digits=[n%10 for n in args]
    value=kwargs.get("op")
    if value=="+":
        print(sum(digits))
    elif value=="-":
        result=0
        for n in digits:
            result=n-result
        print(result)
    elif value=="*":
        result=1
        for n in digits:
            result=n*result
        print(result)
last_digit_calculator(423,234,123,453,567,op="+")
last_digit_calculator(423,234,123,453,567,op="-")
last_digit_calculator(423,234,123,453,567,op="*")
