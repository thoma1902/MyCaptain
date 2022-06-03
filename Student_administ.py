import csv
def write_into_csv(info_list):
    with open('st_info.csv','a',newline='')as csv_file:
        writer=csv.writer(csv_file)
        
        if csv_file.tell()==0:
            writer.writerow(["Name","Age","Mob.No.","E-mail_ID"])
            
        writer.writerow(info_list)
if __name__=='__main__':
    condition=True
    st_no=1
    while (condition):
            st_info=input("Enter the Student informationfor the student {} in the following order (Name Age Mob.No. E-mail_ID): ".format(st_no))
            st_info_list=st_info.split(' ')
            print("Entered information is\nName:{}\nAge:{}\nMob.No.:{}\nE-mail_ID:{}".format(st_info_list[0],st_info_list[1],st_info_list[2],st_info_list[3]))

            choice=input("Is the entered info correct Yes/No: ")
            if choice =='yes':
                write_into_csv(st_info_list)

                repeat=input("Enter (Yes/No) if you want to enter informationn for another student: ")
                if repeat=='yes':
                    condition=True
                    st_no=st_no+1
                elif repeat=='no':
                    condition=False
            elif choice=='no':
                print("...Re-enter the values...")
