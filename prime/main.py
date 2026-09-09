def run(n: int) -> bool:
    # TODO
i=2
    while(i<n/2):
        if(n%i==0):
            return False
        else:
            i=i+1
    
    return True 


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
