class Locators:
    # Login page objects
    username_textbox_id = 'MemberLoginForm_LoginForm_Email'
    password_textbox_id = 'MemberLoginForm_LoginForm_Password'
    login_button_id = 'MemberLoginForm_LoginForm_action_doLogin'

    # Home page objects
    logout_button = '//*[@id="cms-menu"]/div[1]/div[2]/a[2]'

    # Moodle_sandbox Login page objects
    usn_textbox_id = 'username'
    pwd_textbox_id = 'password'
    signIn_button_id = 'loginbtn'

    # Moodle_sandbox Home page objects
    admin_user_dropdown = 'dropdown-1'
    logout_option = '#actionmenuaction-6'
