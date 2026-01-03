password = "user123"
correct_password = "p@ssword123"
login_message_successful = "Login successful!"
login_message_incorrect = "Incorrect password, try again."

login_message = login_message_successful if password == correct_password else login_message_incorrect

# Testing
print("Login Status:", login_message)