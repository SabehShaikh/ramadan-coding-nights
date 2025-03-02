import click # to create a cli
import json # to save and load tasks
import os # to check if a file exists

TODO_FILE = "todo.json"

def load_tasks():
    if not os.path.exists(TODO_FILE):  # Check if file exists
        return []  # Return an empty list if the file doesn't exist
    with open(TODO_FILE, "r") as file:
        return json.load(file)  # Load JSON file

    
def save_tasks(tasks):    
    with open(TODO_FILE , "w") as file:
        json.dump(tasks, file , indent=4) 


@click.group()
def cli():
    """Simple Todo List Manager"""
    pass


@click.command()
@click.argument("task")
def add(task):
    """Add a new task"""
    tasks = load_tasks()
    tasks.append({"task":  task , "done": False})
    save_tasks(tasks)
    click.echo(f"Task '{task}' added to the todo list.")


@click.command()
def list():
    """List all tasks"""
    tasks = load_tasks()
    if not tasks: # if tasks is empty
        click.echo("No tasks found.")
        return
    
    for index, task in enumerate(tasks, 1):
        status = "Done ✅" if task["done"] else "Not Done ❌"

        click.echo(f"{index}. {task['task']} - {status}")

 
@click.command()
@click.argument("task_number", type=int)
def complete(task_number):
    """Marking task as Completed"""
    tasks = load_tasks()
    if 0 < task_number <= len(tasks):
        tasks[task_number - 1]["done"] = True
        save_tasks(tasks)
        click.echo(f"Task {task_number} marked as completed.") 
    else:
        click.echo("Invalid task number.")  


@click.command()
@click.argument("task_number", type=int)
def delete(task_number):
    """Delete a task"""
    tasks = load_tasks()
    if 0 < task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        save_tasks(tasks)
        click.echo(f"Removed Task '{removed_task['task']}' deleted from the todo list.")
    else:
        click.echo("Invalid task number.")


cli.add_command(add)
cli.add_command(list)
cli.add_command(complete)
cli.add_command(delete)

if __name__ == "__main__":
    cli()