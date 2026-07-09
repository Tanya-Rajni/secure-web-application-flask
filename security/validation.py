
import re



class Validator:


    @staticmethod
    def validate_username(username):
        """
        Username rules:
        - Minimum 3 characters
        - Only letters and numbers
        """

        if len(username) < 3:

            return False


        pattern = r"^[a-zA-Z0-9]+$"


        return bool(
            re.match(
                pattern,
                username
            )
        )



    @staticmethod
    def validate_email(email):
        """
        Basic email validation.
        """

        pattern = (
            r"^[\w\.-]+@[\w\.-]+\.\w+$"
        )


        return bool(
            re.match(
                pattern,
                email
            )
        )



    @staticmethod
    def validate_password(password):
        """
        Password security rules:

        Minimum:
        - 8 characters
        - One uppercase
        - One lowercase
        - One number
        - One special character
        """


        if len(password) < 8:

            return False



        if not re.search(
            r"[A-Z]",
            password
        ):

            return False



        if not re.search(
            r"[a-z]",
            password
        ):

            return False



        if not re.search(
            r"[0-9]",
            password
        ):

            return False



        if not re.search(
            r"[!@#$%^&*]",
            password
        ):

            return False



        return True



    @staticmethod
    def sanitize_input(value):
        """
        Remove unwanted spaces.
        """

        return value.strip()