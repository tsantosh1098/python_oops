def main():
    try:
        a=1
        b=0
        c=a/b
        print("DEBUG:we are here")
    except Exception as err:
        print("Exception encountered" , err)
    else:
        print("input numbers: {},{}".format(a,b))

if __name__=="__main__":
    main()