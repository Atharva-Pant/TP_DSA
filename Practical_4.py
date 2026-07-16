class Text_editor:


    def __init__(self):

        self.undo_stack = []
        self.redo_stack = [] 
        self.current_text = ""

    def write(self,text_to_add):
        
        self.undo_stack.append(self.current_text)
        self.current_text = self.current_text + text_to_add
        self.redo_stack.clear()
        #print statement to write 
    def undo(self):

        if len(self.undo_stack) == 0:
            print("[UNDO] failed , Nothing to undo ")
            return
        self.redo_stack.append(self.current_text)
        self.current_text = self.undo_stack.pop()
        print(f"[Undo Executed] -> Current Document: '{self.current_text}'")

    def redo(self):
        # If there's nothing to redo, just stop.
        if len(self.redo_stack) == 0:
            print("[Redo Failed] Nothing to redo.")
            return

        # Step 1: Save the current state to the Undo stack
        self.undo_stack.append(self.current_text)
        
        # Step 2: Pop the state from the Redo stack and put it on the screen
        self.current_text = self.redo_stack.pop()
        
        print(f"[Redo Executed] -> Current Document: '{self.current_text}'")

    # ==========================================
    # 4. Display Document State
    # ==========================================
    def display(self):
        print(f"\n--- Editor State ---")
        print(f"Document: '{self.current_text}'")
        print(f"Undo Stack (Bottom to Top): {self.undo_stack}")
        print(f"Redo Stack (Bottom to Top): {self.redo_stack}")
        print("--------------------\n")

# ==========================================
# Testing the Application
# ==========================================
editor = Text_editor()

# Typing some text
editor.write("Hello")
editor.write(" World")
editor.write("!")
editor.display()

# Let's undo the exclamation mark and " World"
editor.undo()
editor.undo()
editor.display()

# Wait, let's bring back " World"
editor.redo()
editor.display()

# Now type something new (This will destroy the exclamation mark in the Redo stack)
editor.write(" Python")
editor.display()

 

    
    
    
     

 