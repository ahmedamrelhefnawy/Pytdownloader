class User:
    '''Used to interact with the user and make sure that his input is correct logically'''
    u_input = 'False'

    @staticmethod
    def get_int_input(message: str, u_range: 'list[int]') -> int:
        User.u_input = input(message)
        User.__int_check(u_range)

        return int(User.u_input)

    def __int_check(u_range: 'list[int]') -> None:
        while True:
            try:
                if int(User.u_input.strip().lower()) in u_range:
                    break
                else:
                    User.u_input = input(
                        f"Invalid Input, Please choose a number from {u_range[0]} to {u_range[-1]}: ")
            except ValueError:
                User.u_input = input(
                        f"Invalid Input, Please choose a number from {u_range[0]} to {u_range[-1]}: ")

    @staticmethod
    def get_bool_input(message: str) -> bool:

        User.u_input = input(message)
        User.__bool_check()

        return True if User.u_input == 'y' else False

    def __bool_check() -> None:

        while True:
            if User.u_input.strip().lower() in ['y', 'n']:
                break
            else:
                User.u_input = input(
                    "Invalid Input, Please enter either 'Y' as Yes or 'N' as No: ")[0]

        
if __name__ == "__main__":
    print(User.get_int_input("test message: ",range(0,5)))