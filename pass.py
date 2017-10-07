def pass_storage(hot_key):
    def capsule_protection(password):
        if password == "hotkey":
            return hot_key()
        else:
            print("your pass is incorrect")

    return capsule_protection

@pass_storage

def protected_pass():
    print("your pass is correct.")

if __name__ == '__main__':
    print("==========================================")
    password = str(raw_input("enter your password: "))
    protected_pass(password)
