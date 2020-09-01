Values from outside of your application

Connecting to a database
Determining the operating system
Settings which need to change
Sensitive data

*What happens if database is renamed?*
- You need to be able to change that value, without going back into the application to update that.

*What happens if I need  to read something ftom the operating system?*
- E.g need the current directory.
- Figure out what operating system we're running on.
- I don't want to hardcode that in, I what to read that from somewhere external to my application, and thats where environmental variable come into play.

Our operating system, has a whole host of environmental variable, they might be broken down to:
- System level.
- User level: e.g one that are specific to you.
- The way you are going to reas them is same.


There are other things to read apart from OS, like API keys, passwords.
you can manage this using dotenv

# DOTENV

whats great about dotenv that it gives you the opportunity to set and store those environmental variables inside of a text file.
 This way you will never hardcode anything and you are not checking in those sensitive values into your source control.

 # Final notes

Don't hard code sensitive information **EVER**
Use dotenv for a simple solution.
Add .env to .gitignore
Consider full encription options e.g Azure key vault

.env file is a series of key value pairs that is used for environmental variable.