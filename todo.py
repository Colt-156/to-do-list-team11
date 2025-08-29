# todo.py

# Step 1: Start with an empty list to hold tasks
tasks = []
completedtasks= []

# Step 2: Add a task
def add_task(task):
    tasks.append(task)

# Step 3: View tasks
def view_tasks():
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")
# Step 4: Delete a task
def delete_tasks():
    Deleted_Tasks=input("Do you want to remove any tasks(y/n)")
    if Deleted_Tasks=="y":
        numtask=int(input("Which task(ex. 1,2,ect.)"))
        print(f"Deleted {tasks[numtask-1]}")
        tasks.pop(numtask-1)
# Step 5: Mark task complete
def mark_complete():
    Completed_Tasks=input("Have you completed any tasks(y/n)")
    if Completed_Tasks=="y":
        numtask=int(input("Which task(ex. 1,2,ect.)"))
        completedtasks.append(numtask-1)





# Demo flow (you can run this file directly: python todo.py)
if __name__ == "__main__":
    add_task("Finish Cyber 201 assignment")
    add_task("Push code to GitHub")
    view_tasks()
    delete_tasks()
    mark_complete()
    view_tasks()