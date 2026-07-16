from collections import deque


class event_manager():

    def __init__(self):
        self.queue =deque()

    def add_event(self,event_name):
        self.queue.append(event_name)
        print(f"Event {event_name} added into queue")

    def process_next_event(self):
        if self.queue:
            processing_event = self.queue.popleft()
            print (f"Processing event :{processing_event}")
        else:
            print ("No events to process")

    def display_pending_events(self):
        if self.queue:
            for index,event in enumerate(self.queue, start=1):
                print (f"Sr_no.:{index}  Event: {event}" )
        else:
            print (f"No process in the queue")

    def Cancel_event(self,event_name):
        if event_name in self.queue:
            self.queue.remove(event_name)
            print (f"Removed {event_name} from queue")
        else:
            print("Elemnt not found")


def main ():

    system = event_manager()
        
    while True:
         print("-------EVENT_MANAGER-------")
         print()  
         print ("1. Add a event")
         print ("2. Process next event")
         print ("3. Display upcoming event")
         print ("4. Cancel a event")
         print ("5. Exit")
         print("----------------------------------")
         print()

         choice = int(input(f"Enter a choice between 1-5:  \n"))

         if choice == 1:
             event_name = input("enter event name: \n")
             system.add_event(event_name)

         elif choice ==2:
             system.process_next_event()

         elif choice == 3:
             system.display_pending_events()

         elif choice == 4:
             event_cancel = input("Enter the event name which is to be cancelled ")
             system.Cancel_event(event_cancel)

         elif choice == 5:
             print("Exiting Goodbye")
             break

         else:
             print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
             
            
       


             
             


           
        


        


