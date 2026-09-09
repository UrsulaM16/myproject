def run(target_x: int, target_y: int) -> int:
    x=0
    y=0
    i=0
    if(target_x==0 and target_y== 0):
        return 0
    while True:
        i+=1
        x=x+2
        y=y+1
        if(x==target_x and y==target_y):
            return i
        i+=1
        y=y+2
        x=x+1
        if(x==target_x and y==target_y):
            return i
        if(x>target_x or y> target_y):
            return -1 

# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
