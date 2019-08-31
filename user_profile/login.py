from database_actions import DBActions
from configs import env_variables
from user_profile.manage_password import ManagePassword


class Login:
    def validate_user(user_name, provided_password):
        required_field = "passwd"
        where_clause = " user_name = '" + user_name + "' "
        stored_password = DBActions.fetch_results_from_db(
            env_variables.USER_TABLE, required_field, where_clause)
        if stored_password == None:
            raise Exception("No such user exists in the system")
        else:
            print("User Found\nValidating Credentials")
            if ManagePassword.verify_password(stored_password, provided_password):
                print("Login Successful")
                return True
            else:
                return False
