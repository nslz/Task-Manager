tasks = [] 
    
def add_task():
    print('-'*20)
    enter_task = input("Enter task to add it in list: ")
    task_info = {'task': enter_task,'status': False}
    tasks.append(task_info)
    print('Task added to list successfully....')

def mark_task():
    print('-'*20)
    tasks_not_complete = []
    for i in tasks:
        if i['status'] == False:
            tasks_not_complete.append(i)

    if len(tasks_not_complete) == 0:
        print('No tasks to mark as complete')
        return
    
    for i,task in enumerate(tasks_not_complete,1):
        print(f"{i} - {task['task']}")
    try:
        mark = int(input("Enter the number of task to mark as complete: "))
        if mark < 1 or mark > len(tasks_not_complete):
            print(f"{'-'*20}\nInvalid input, please choose from avaliable tasks")
            return
        tasks_not_complete[mark - 1]['status'] = True
    except ValueError:
        print(f"{'-'*20}\nInvalid input, please enter a number")
        return
    
    print(f"{tasks_not_complete[mark - 1]['task']} has been completed")
   
def view_task():
    if len(tasks) == 0:
        print('-'*20)
        print('No tasks to view')
        return
    
    print('-'*20)
    for i,task in enumerate(tasks,1):
        if task['status'] == True:
            state = 'Complete'
        else:
            state = 'Incomplete'
        print(f"{i}- {task['task']} ({state})")

def main():
    while True:
        print('-'* 20)
        print('1 - add tasks to list')
        print('2 - mark task as complete')
        print('3 - view tasks')
        print('4 - quit of task manager')

        user_enter = input('Enter what would like to do: ')

        if user_enter == '1':
            add_task()
        elif user_enter == '2':
            mark_task()
        elif user_enter == '3':
            view_task()
        elif user_enter == '4':
            break
        else:
            print('-'*20)
            print('Invalid choice, please enter number from "1-4"')

if __name__ == "__main__":
    main()