def create_task(list, dict):
    task = input('Enter task : ').strip()
    if not task:
        print("!!\tTask is Empty\t!!")
        return(list, dict)
    list.append(task)
    dict = convert(list, dict)
    print('\t\t>>>>> NEW TASK ADDED <<<<<')
    display_tasks(list, dict)
    return (list, dict)

def update_task(list, dict):
    x = int(input("Which task u want to update? : "))
    x-=1
    try:
        list[x]=0
    except IndexError as e:
        if len(list)==0:
            display_tasks(list, dict)
        else:
            print(f'!!\tNo task numbered {x+1}\t!!')
        return(list, dict)
    list[x]=input("Enter new task : ")
    dict=convert(list, dict)
    print(f'\t\t>>>>> TASK {x+1} UPDATED <<<<<')
    display_tasks(list, dict)
    return (list, dict)

def delete_task(list, dict):
    x = int(input("Which task you want to delete? : "))
    x-=1
    # deleted = False
    try:
        list.pop(x)
        dict.pop(x+1)
        # deleted = True
    except Exception as e:
        if len(list)==0:
            display_tasks(list, dict)
        else:
            print(f'!!\tNo Task is numbered {x+1}\t!!')
        return(list, dict)
    # print('-----------------------')
    # print(list)
    # print('-----------------------')
    newd = {}
    for i in range(len(list)):
        newd[i+1]=list[i]
    dict=newd
    # print('-----------------------')
    # print(dict)
    # print('-----------------------')
    if len(list)==0:
        i=0
        print(f'\t\t>>>>> TASK {x+1} DELETED <<<<<')
    else:
        print(f'\t\t>>>>> TASK {x+1} DELETED <<<<<')
    display_tasks(list,dict)
    return (list, dict)

def display_tasks(list, dict):
    if len(list)==0:
        print('\t-->No Tasks as of now<--')
    for i in dict:
        print('\t\t\t[', i, ']', ' ', dict[i])

def convert(task_list, task_dict):
    lenght = len(task_list)
    for i in range(lenght-1,-1,-1):
        task_dict[i+1]=task_list[i]
    return task_dict

def main():

    task_list = []
    task_dict={}
    cnt=5


    flag=True
    # print("\033[4mhello\033[0m")
    # print("\033[9mThis text is strikethrough\033[0m")
    print('\t\t\t\t***********')
    print("\t\t\t\t| WELCOME |")
    print('\t\t\t\t***********')
    while flag:
        if cnt==5:
            print('\t\t\t---------------------------')
            print('\t\t\t1. Create\t2. Update\n\t\t\t3. Mark as Done\t4. Display\n\t\t\t5. Exit')
            print('\t\t\t---------------------------')
            cnt=0
        cnt+=1

        choice = int(input('Enter your choice : '))

        if choice==5:
            flag=False
            continue
        elif choice==1:
            (task_list, task_dict) = create_task(task_list, task_dict)
        elif choice==2:
            (task_list, task_dict) = update_task(task_list, task_dict)
        elif choice==3:
            (task_list, task_dict) = delete_task(task_list, task_dict)
        elif choice==4:
            display_tasks(task_list, task_dict)
if __name__=='__main__':
    main()