from collections import deque

class CallCenterQueue:
    def __init__(self):
        # We use deque for high-performance FIFO operations
        self.queue = deque()

    def addCall(self):
        customer_id = input("Enter Customer ID: ")
        try:
            call_time = float(input("Enter Call Time (minutes): "))
            # Store as a dictionary to keep data linked
            call = {"id": customer_id, "time": call_time}
            self.queue.append(call)
            print(f"Call from {customer_id} added to the queue.")
        except ValueError:
            print("Invalid input! Please enter a number for call time.")

    def answerCall(self):
        if not self.isQueueEmpty():
            # popleft() removes the oldest call (First-In, First-Out)
            answered = self.queue.popleft()
            print(f"Answering call from Customer ID: {answered['id']}")
            print(f"Call duration expected: {answered['time']} minutes.")
        else:
            print("The queue is empty! No calls to answer.")

    def viewQueue(self):
        if not self.isQueueEmpty():
            print("\n--- Current Call Queue ---")
            for i, call in enumerate(self.queue, start=1):
                print(f"{i}. ID: {call['id']} | Time: {call['time']} min")
        else:
            print("The queue is currently empty.")

    def isQueueEmpty(self):
        return len(self.queue) == 0

def main():
    cc = CallCenterQueue()

    while True:
        print("\n===== Call Center Simulation System =====")
        print("1. Add a Call")
        print("2. Answer Next Call")
        print("3. View Current Queue")
        print("4. Check if Queue is Empty")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            cc.addCall()
        elif choice == "2":
            cc.answerCall()
        elif choice == "3":
            cc.viewQueue()
        elif choice == "4":
            if cc.isQueueEmpty():
                print("Status: The queue is currently empty.")
            else:
                print(f"Status: There are {len(cc.queue)} calls waiting.")
        elif choice == "5":
            print("Exiting System... Goodbye!")
            break
        else:
            print("Invalid choice! Please select 1-5.")

if __name__ == "__main__":
    main()