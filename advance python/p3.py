def main():
   try:
    a = int(input("Hey, enter a number: "))
    print(a)

   except Exception as e:
    print(e)
    return

   finally:
    print("I'm inside else")
main()    