from intermediate_nanodegree.exercise_exceptions.exception.invalid_password_error import InvalidPasswordError

INVALID_PASSWORDS = (
    'password',
    'abc123',
    '123abc',
)


def validate_password(username, password):
    if password != username and password not in INVALID_PASSWORDS:
        return True
    else:
        raise InvalidPasswordError('Invalid password')


def create_account(username, password):
    return (username, password)


def main(username, password):
    try:
        valid = validate_password(username, password)
    except InvalidPasswordError as e:
        print("Error: {0}".format(e))
        valid = False
    else:
        account = create_account(username, password)
    finally:
        print("Validated password against username and collection")


if __name__ == '__main__':
    main('jim', 'jam')
    main('admin', 'password')  # Oh no!
    main('guest', 'guest')  # Oh no!