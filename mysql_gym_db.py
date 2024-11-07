#1. Gym Database Management with Python and SQL

import mysql.connector

from mysql.connector import Error


#Task 1: Add a Member

#Write a Python function to add a new member to the 'Members' table in the gym's database.
    # Example code structure
 #   def add_member(id, name, age):
        # SQL query to add a new member
        # Error handling for duplicate IDs or other constraints
#Expected Outcome: A Python function that successfully adds a new member to the 'Members' table
#  in the gym's database. The function should handle errors gracefully,
#  such as duplicate member IDs or violations of other constraints.

db_name = "fitness_center_db"
user = "root"
password = "Babinz2023!"
host = "localhost"

def add_member(cursor, member_id, name, age):
    try:
       new_member = (member_id, name, age)
       query = "INSERT INTO Members(member_id, name, age) VALUES (%s, %s, %s)"
       
       cursor.execute(query, new_member)
       
       
    except Error as e:
         print(f"An exception occurred: \n {e}")


#Task 2: Add a Workout Session

#Develop a Python function to add 
#a new workout session to the 'WorkoutSessions' table for a specific member.


def add_workout_session(cursor, session_id, member_id, session_date, duration_minutes, calories_burned):
        # SQL query to add a new workout session
        # Error handling for invalid member ID or other constraints
    try:
        new_session = (session_id, member_id, session_date, duration_minutes, calories_burned)
        query = "INSERT INTO WorkoutSessions(session_id, member_id, session_date, duration_minutes, calories_burned) VALUES (%s, %s, %s, %s, %s)"
       
        cursor.execute(query, new_session)

    except mysql.connector.Error as db_err:
        print(f' Database Error: \n {db_err}')
       
       
    except Exception as e:
         print(f"An exception occurred:\n {e}")

#Task 3: Updating Member Information

#Implement a function to update the age of a member.
#Ensure that your function checks if the member exists before attempting the update.



def update_member_age(cursor, member_id, new_age):
        # SQL query to update age
        # Check if member exists
        # Error handling
        try:
           

            update_member = (member_id, new_age)
           # update_member holds the values from input for the member_id and updated age

            query = "UPDATE Members SET age = %s WHERE member_id = %s;"

            # query to update Members table, set age to placeholder, with WHERE condition to match member_id
            cursor.execute(query, update_member)
             # execute query

        except mysql.connector.Error as db_err:
            print(f' Database Error: \n {db_err}')
       
        except Exception as e:
            print(f"An exception occurred:\n {e}")



#ask 4: Delete a Workout Session

#Create a Python function to delete a workout session based on its session ID.
#Include error handling for cases where the session ID does not exist.
#


def delete_workout_session(cursor, session_id):
        # SQL query to delete a session
        # Error handling for non-existent session ID
    try:
        delete_session = (session_id)
        query = "DELETE FROM WorkoutSessions(session_id) VALUES (%s);"
       
        cursor.execute(query, delete_session)
    
    except mysql.connector.Error as db_err:
        print(f' Database Error: \n {db_err}')
       
       
    except Exception as e:
         print(f"An exception occurred: {e}")

### ******************************************************************

## 2. Advanced Data Analysis in Gym Management System

# Task 1: SQL BETWEEN Usage

#Problem Statement: Retrieve the details of members whose ages fall between 25 and 30.


def get_members_in_age_range(cursor, start_age, end_age):
        # SQL query using BETWEEN
        # Execute and fetch results
    try:
        age_range = (start_age, end_age)
        query = "SELECT * FROM Members WHERE age BETWEEN (%s) AND (%s);"
       
        cursor.execute(query, age_range)
    
    except mysql.connector.Error as db_err:
        print(f' Database Error: \n {db_err}')
       
       
    except Exception as e:
         print(f"An exception occurred: {e}")






def main():
    # establish connection
    conn = mysql.connector.connect(
            database = db_name,
            user = user,
            password = password,
            host = host
            )
    if conn is not None:
        print("*** Welcome to CT Fitness Center Database ***")
        print("Menu: ")
        print("1. Add a Member. ")
        print("2. Add a Workout Session. ")
        print("3. Update Member Age. ")
        print("4. Delete a Workout Session. ")
        print("5. View Members within age range. ")
    
        choice = input("Select an Option (1-5)")

        

        try:
            cursor = conn.cursor()

            if choice == "1":

                member_id = input("Enter new member id #. ")
                name = input("Enter member name: ")
                age = input("Enter member age: ")

                add_member(cursor, member_id, name, age)
            
                conn.commit()

            elif choice == "2":
                session_id = input("Enter Session Id: ")
                member_id = input("Enter Member Id: ")
                date = input("Enter a date for Workout: ")
                duration_minutes = input("How long (minutes) is this Session? ")
                calories_burned = input("How many calories will be burned? ")
                

                add_workout_session(cursor, session_id, member_id, date, duration_minutes, calories_burned)
            
                conn.commit()

            elif choice == "3":
                member_id = input("Enter Member Id: ")
               
                new_age = input(f"Enter update age for Member: \n")
                update_member_age(cursor, member_id, new_age)
            
                conn.commit()

            elif choice == "4":

                session_id = input("Enter Session Id for Workout to delete: ")
                
               
                delete_workout_session(cursor, session_id)
            
                conn.commit()
            
            elif choice == "5":
                start_age = input("Enter start age: ")
                end_age = input("Enter end age: ")
               
                
                get_members_in_age_range(cursor, start_age, end_age)
            
                conn.commit()

        except mysql.connector.Error as db_err:
            print(f' Database Error: \n {db_err}')
         
     
        except Exception as e:
            print(f'An exception occurred {e}')

        finally:
            if conn and conn.is_connected():
                conn.close()
                print("MySQL connection closed.")

    

           

if __name__ == "__main__":
     main()