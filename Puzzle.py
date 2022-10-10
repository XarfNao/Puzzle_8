from tkinter import *

"""
Puzzle 8 solving app

This app is able to solve many solvable cases of puzzle 8
It can also recognize, if the specific case is solvable or not

Author: Thomas Bozek (XarfNao), 2021
"""
class Puzzle:
    # Executes after the Puzzle class is called
    def __init__(self):
        # Used for checking problems in the algorithm
        self.states = []
        # Creating List which will be filled with made steps later on
        self.stepsHistory = []
        # Window inicialization
        self.windowInicialization()
        # Creating window content
        self.windowContent()
        # Mainloop - UI
        self.window.mainloop()

    # Window inicialization
    def windowInicialization(self):
        # Creating window
        self.window = Tk()
        # Creating window title
        self.window.title("Puzzle 8 solver - XarfNao, 2021")
        # Implementing icon
        self.window.iconbitmap("puzzle_icon.ico")

    # Changes state to the one selected in the listbox
    def listcallback(self, event):
        selection = event.widget.curselection()
        if selection:
            index = selection[0]
            selectedState = event.widget.get(index)
            if "Start" in selectedState:
                selectedStateOk = selectedState.split("Start - ", -1)
                selectedState = selectedStateOk[1]
            # Creating canvas that shows state
            self.puzzleState.destroy()
            self.puzzleState = Canvas(self.window, width=210, height=210)
            self.puzzleState.create_text(35, 35, font="Helvetica 36 bold", text=selectedState[0])
            self.puzzleState.create_text(35, 105, font="Helvetica 36 bold", text=selectedState[3])
            self.puzzleState.create_text(35, 175, font="Helvetica 36 bold", text=selectedState[6])
            self.puzzleState.create_text(105, 35, font="Helvetica 36 bold", text=selectedState[1])
            self.puzzleState.create_text(105, 105, font="Helvetica 36 bold", text=selectedState[4])
            self.puzzleState.create_text(105, 175, font="Helvetica 36 bold", text=selectedState[7])
            self.puzzleState.create_text(175, 35, font="Helvetica 36 bold", text=selectedState[2])
            self.puzzleState.create_text(175, 105, font="Helvetica 36 bold", text=selectedState[5])
            self.puzzleState.create_text(175, 175, font="Helvetica 36 bold", text=selectedState[8])
            self.puzzleState.grid(row=0, column=2, rowspan=8, columnspan=6, padx=5, pady=5)
        else:
            # Creating canvas that shows state
            self.puzzleState.destroy()
            self.puzzleState = Canvas(self.window, width=210, height=210)
            self.puzzleState.create_text(35, 35, font="Helvetica 36 bold", text="?")
            self.puzzleState.create_text(35, 105, font="Helvetica 36 bold", text="?")
            self.puzzleState.create_text(35, 175, font="Helvetica 36 bold", text="?")
            self.puzzleState.create_text(105, 35, font="Helvetica 36 bold", text="?")
            self.puzzleState.create_text(105, 105, font="Helvetica 36 bold", text="?")
            self.puzzleState.create_text(105, 175, font="Helvetica 36 bold", text="?")
            self.puzzleState.create_text(175, 35, font="Helvetica 36 bold", text="?")
            self.puzzleState.create_text(175, 105, font="Helvetica 36 bold", text="?")
            self.puzzleState.create_text(175, 175, font="Helvetica 36 bold", text="?")
            self.puzzleState.grid(row=0, column=2, rowspan=8, columnspan=6, padx=5, pady=5)

    # Creating window content
    def windowContent(self):
        # Creating start state label
        self.startLabel = Label(self.window, text="Start state:")
        # Creating end state label
        self.endLabel = Label(self.window, text="End state:")
        # Creating number of steps label
        self.stepsLabel = Label(self.window, text="Number of steps: --")
        # Creating number of nodes label
        self.nodesLabel = Label(self.window, text="Number of nodes: --")
        # Creating solvable info label
        self.solvableLabel = Label(self.window, text="Solvable: --")
        # Creating listbox label
        self.listLabel = Label(self.window, text="Individual steps:")
        # Creating start state input variable
        self.input = StringVar()
        # Creating start state entry
        self.inputEntry = Entry(self.window, textvariable=self.input)
        # Creating end state input variable
        self.inputEnd = StringVar()
        # Creating end state entry
        self.inputEndEntry = Entry(self.window, textvariable=self.inputEnd)
        # Creating start button
        self.startButton = Button(self.window, text="Start solving", command=self.inputControl, width=16, height=2, bg="#5CB85C")
        # Creating start button
        self.stepsList = Listbox(self.window, height=14, font="TkDefaultFont 9 bold")

        # Creating canvas that shows state
        self.puzzleState = Canvas(self.window, width=210, height=210)
        self.puzzleState.create_text(35, 35, font="Helvetica 36 bold", text="?")
        self.puzzleState.create_text(35, 105, font="Helvetica 36 bold", text="?")
        self.puzzleState.create_text(35, 175, font="Helvetica 36 bold", text="?")
        self.puzzleState.create_text(105, 35, font="Helvetica 36 bold", text="?")
        self.puzzleState.create_text(105, 105, font="Helvetica 36 bold", text="?")
        self.puzzleState.create_text(105, 175, font="Helvetica 36 bold", text="?")
        self.puzzleState.create_text(175, 35, font="Helvetica 36 bold", text="?")
        self.puzzleState.create_text(175, 105, font="Helvetica 36 bold", text="?")
        self.puzzleState.create_text(175, 175, font="Helvetica 36 bold", text="?")

        # Creating warning label
        self.warningLabel = Label(self.window, text="Warning: Input can only be digits 0-8 without repetition!"
                                                    "\n0 represents blank spot... Both entries need to be filled!")
        # Creating error label
        self.errorLabel = Label(self.window, text="")

        # Putting all GUI content to its place
        self.startLabel.grid(row=0, column=0, padx=10, sticky="W")
        self.inputEntry.grid(row=1, column=0, padx=10)
        self.endLabel.grid(row=2, column=0, padx=10, sticky="W")
        self.inputEndEntry.grid(row=3, column=0, padx=10)
        self.nodesLabel.grid(row=4, column=0, padx=10, pady=2, sticky="W")
        self.stepsLabel.grid(row=5, column=0, padx=10, sticky="W")
        self.solvableLabel.grid(row=6, column=0, padx=10, sticky="W")
        self.startButton.grid(row=7, column=0, padx=5, pady=5)
        self.listLabel.grid(row=0, column=1, padx=10, pady=4)
        self.stepsList.grid(row=1, column=1, rowspan=7, padx=10, pady=4)
        self.puzzleState.grid(row=0, column=2, rowspan=8, columnspan=6, padx=5, pady=5)
        self.warningLabel.grid(row=8, column=1, columnspan=7, pady=2, padx=2)
        self.errorLabel.grid(row=8, column=0)

    # Solves current state using A* algorithm (using heuristic - Hamming priority function)
    def solve(self):
        targetState = self.inputEnd.get()
        currentState = self.input.get()
        blankIndex = 0
        count = 0
        nodeCount = 0
        while currentState != targetState:
            if len(self.stepsHistory) >= 6 and self.stepsHistory[-1] == self.stepsHistory[-3] and self.stepsHistory[-2] == self.stepsHistory[-4]:
                for i in range(len(self.stepsHistory)):
                    if self.stepsHistory[i+2] == self.stepsHistory[i+4] and self.stepsHistory[i+3] == self.stepsHistory[i+5]:
                        recurChange = list(self.stepsHistory[i])
                        curState = ""
                        for z in range(9):
                            curState += recurChange[z]
                        currentState = curState
                        self.stepsHistory = self.stepsHistory[0:i+2]
                        break

            count += 1
            for i in range(len(currentState)):
                if currentState[i] == "0":
                    blankIndex = i
                    break
            if blankIndex == 0:
                nodeCount += 2
                value_one = self.valueCounter(0, 1, currentState, targetState)
                value_two = self.valueCounter(0, 3, currentState, targetState)
                if value_one > 9 and value_two > 9:
                    currentState = self.goBack()
                elif value_one <= value_two:
                    currentState = self.stateChanger(0, 1, currentState)
                elif value_two <= value_one:
                    currentState = self.stateChanger(0, 3, currentState)
            elif blankIndex == 1:
                nodeCount += 3
                value_one = self.valueCounter(1, 0, currentState, targetState)
                value_two = self.valueCounter(1, 4, currentState, targetState)
                value_three = self.valueCounter(1, 2, currentState, targetState)
                if value_one > 9 and value_two > 9 and value_three > 9:
                    currentState = self.goBack()
                elif value_one <= value_two and value_one <= value_three:
                    currentState = self.stateChanger(1, 0, currentState)
                elif value_two <= value_one and value_two <= value_three:
                    currentState = self.stateChanger(1, 4, currentState)
                elif value_three <= value_one and value_three <= value_two:
                    currentState = self.stateChanger(1, 2, currentState)
            elif blankIndex == 2:
                nodeCount += 2
                value_one = self.valueCounter(2, 1, currentState, targetState)
                value_two = self.valueCounter(2, 5, currentState, targetState)
                if value_one > 9 and value_two > 9:
                    currentState = self.goBack()
                elif value_one <= value_two:
                    currentState = self.stateChanger(2, 1, currentState)
                elif value_two <= value_one:
                    currentState = self.stateChanger(2, 5, currentState)
            elif blankIndex == 3:
                nodeCount += 3
                value_one = self.valueCounter(3, 0, currentState, targetState)
                value_two = self.valueCounter(3, 4, currentState, targetState)
                value_three = self.valueCounter(3, 6, currentState, targetState)
                if value_one > 9 and value_two > 9 and value_three > 9:
                    currentState = self.goBack()
                elif value_one <= value_two and value_one <= value_three:
                    currentState = self.stateChanger(3, 0, currentState)
                elif value_two <= value_one and value_two <= value_three:
                    currentState = self.stateChanger(3, 4, currentState)
                elif value_three <= value_one and value_three <= value_two:
                    currentState = self.stateChanger(3, 6, currentState)
            elif blankIndex == 4:
                nodeCount += 4
                value_one = self.valueCounter(4, 3, currentState, targetState)
                value_two = self.valueCounter(4, 7, currentState, targetState)
                value_three = self.valueCounter(4, 5, currentState, targetState)
                value_four = self.valueCounter(4, 1, currentState, targetState)
                if value_one > 9 and value_two > 9 and value_three > 9 and value_four > 9:
                    currentState = self.goBack()
                elif value_one <= value_two and value_one <= value_three and value_one <= value_four:
                    currentState = self.stateChanger(4, 3, currentState)
                elif value_two <= value_one and value_two <= value_three and value_two <= value_four:
                    currentState = self.stateChanger(4, 7, currentState)
                elif value_three <= value_one and value_three <= value_two and value_three <= value_four:
                    currentState = self.stateChanger(4, 5, currentState)
                elif value_four <= value_one and value_four <= value_two and value_four <= value_three:
                    currentState = self.stateChanger(4, 1, currentState)
            elif blankIndex == 5:
                nodeCount += 3
                value_one = self.valueCounter(5, 2, currentState, targetState)
                value_two = self.valueCounter(5, 4, currentState, targetState)
                value_three = self.valueCounter(5, 8, currentState, targetState)
                if value_one >= 100000 and value_two >= 100000 and value_three >= 100000:
                    currentState = self.goBack()
                elif value_one <= value_two and value_one <= value_three:
                    currentState = self.stateChanger(5, 2, currentState)
                elif value_two <= value_one and value_two <= value_three:
                    currentState = self.stateChanger(5, 4, currentState)
                elif value_three <= value_one and value_three <= value_two:
                    currentState = self.stateChanger(5, 8, currentState)
            elif blankIndex == 6:
                nodeCount += 2
                value_one = self.valueCounter(6, 3, currentState, targetState)
                value_two = self.valueCounter(6, 7, currentState, targetState)
                if value_one >= 100000 and value_two >= 100000:
                    currentState = self.goBack()
                elif value_one <= value_two:
                    currentState = self.stateChanger(6, 3, currentState)
                elif value_two <= value_one:
                    currentState = self.stateChanger(6, 7, currentState)
            elif blankIndex == 7:
                nodeCount += 3
                value_one = self.valueCounter(7, 4, currentState, targetState)
                value_two = self.valueCounter(7, 6, currentState, targetState)
                value_three = self.valueCounter(7, 8, currentState, targetState)
                if value_one >= 100000 and value_two >= 100000 and value_three >= 100000:
                    currentState = self.goBack()
                elif value_one <= value_two and value_one <= value_three:
                    currentState = self.stateChanger(7, 4, currentState)
                elif value_two <= value_one and value_two <= value_three:
                    currentState = self.stateChanger(7, 6, currentState)
                elif value_three <= value_one and value_three <= value_two:
                    currentState = self.stateChanger(7, 8, currentState)
            elif blankIndex == 8:
                nodeCount += 2
                value_one = self.valueCounter(8, 5, currentState, targetState)
                value_two = self.valueCounter(8, 7, currentState, targetState)
                if value_one >= 100000 and value_two >= 100000:
                    currentState = self.goBack()
                elif value_one <= value_two:
                    currentState = self.stateChanger(8, 5, currentState)
                elif value_two <= value_one:
                    currentState = self.stateChanger(8, 7, currentState)
            if len(self.states) != 0 and currentState == self.states[-1]:
                currentState = ""
                break
            else:
                self.states.append(currentState)
                self.stepsList.insert(END, currentState)

        # If the current state is same as the end state, the solving is done
        if currentState == targetState:
            # GUI says that the solving has ended
            self.errorLabel.destroy()
            self.stepsLabel.destroy()
            self.nodesLabel.destroy()
            self.errorLabel = Label(self.window, text="Solving done!", font="TkDefaultFont 10 bold")
            self.errorLabel.grid(row=8, column=0)
            self.nodesLabel = Label(self.window, text="Number of nodes: " + str(nodeCount))
            self.nodesLabel.grid(row=4, column=0, padx=10, pady=2, sticky="W")
            self.stepsLabel = Label(self.window, text="Number of steps: " + str(count))
            self.stepsLabel.grid(row=5, column=0, padx=10, sticky="W")
            self.stepsHistory = [self.input.get(), self.inputEnd.get()]
            self.states = []
        elif currentState == "":
            # GUI says that an error has occured
            self.errorLabel.destroy()
            self.errorLabel = Label(self.window, text="An error has occured!", font="TkDefaultFont 10 bold")
            self.errorLabel.grid(row=8, column=0)
            self.states = []
            self.stepsHistory = [self.input.get(), self.inputEnd.get()]

    # Method controls input (if its in a correct form and solvable)
    # If the input is ok, it calls the solve() method
    def inputControl(self):
        # Creating lists that will be used for checking the input later on
        nice_numbers_one = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]
        nice_numbers_two = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]
        if len(self.input.get()) == 9 and len(self.inputEnd.get()) == 9:
            # Is it 9 characters long and does it only contain 0-8?
            for i in range(9):
                if self.input.get()[i] in nice_numbers_one:
                    nice_numbers_one.remove(self.input.get()[i])
                if self.inputEnd.get()[i] in nice_numbers_two:
                    nice_numbers_two.remove(self.inputEnd.get()[i])
            if len(nice_numbers_one) == 0 and len(nice_numbers_two) == 0:
                # Is it solvable? - isSolvable() method
                if self.isSolvable():
                    if len(self.stepsHistory) != 0 and self.stepsHistory[0] == self.input.get() and self.stepsHistory[1] == self.inputEnd.get():
                        self.errorLabel.destroy()
                        self.errorLabel = Label(self.window, text="Input different states!", font="TkDefaultFont 10 bold")
                        self.errorLabel.grid(row=8, column=0)
                    else:
                        self.stepsHistory = []
                        # GUI says that the solving has started
                        self.errorLabel.destroy()
                        self.stepsList.destroy()
                        self.solvableLabel.destroy()
                        self.solvableLabel = Label(self.window, text="Solvable: True")
                        self.solvableLabel.grid(row=6, column=0, padx=10, sticky="W")
                        self.errorLabel = Label(self.window, text="Solving in process...", font="TkDefaultFont 10 bold")
                        self.errorLabel.grid(row=8, column=0)
                        self.stepsList = Listbox(self.window, height=14, font="TkDefaultFont 9 bold")
                        # Binding function that will execute on change of selection in the listbox
                        self.stepsList.bind('<<ListboxSelect>>', self.listcallback)
                        self.stepsList.grid(row=1, column=1, rowspan=7, padx=10, pady=4)
                        self.stepsList.insert(0, "Start - " + self.input.get())
                        # If solvable - solve
                        self.solve()
                # If not solvable - inform
                else:
                    self.errorLabel.destroy()
                    self.solvableLabel.destroy()
                    self.errorLabel = Label(self.window, text="This isn't solvable!", font="TkDefaultFont 10 bold")
                    self.errorLabel.grid(row=8, column=0)
                    self.solvableLabel = Label(self.window, text="Solvable: False")
                    self.solvableLabel.grid(row=6, column=0, padx=10, sticky="W")
            # If bad input - error
            else:
                self.errorLabel.destroy()
                self.errorLabel = Label(self.window, text="Input error! →", font="TkDefaultFont 10 bold")
                self.errorLabel.grid(row=8, column=0)
        # If bad input - error
        else:
            self.errorLabel.destroy()
            self.errorLabel = Label(self.window, text="Input error! →", font="TkDefaultFont 10 bold")
            self.errorLabel.grid(row=8, column=0)

    # Method controls, if the current input is solvable
    def isSolvable(self) -> bool:
        count_start = 0
        count_end = 0
        # Following block of code checks, if the input start state has odd of even number of inversions considering the solved state
        for i in range(len(self.input.get())):
            if self.input.get()[i] == "0":
                pass
            else:
                for y in range(len(self.input.get())):
                    if self.input.get()[y] == "0":
                        pass
                    elif int(self.input.get()[i]) > int(self.input.get()[y]):
                        count_start += 1
        # Following block of code checks, if the input end state has odd of even number of inversions considering the solved state
        for i in range(len(self.inputEnd.get())):
            if self.inputEnd.get()[i] == "0":
                pass
            else:
                for y in range(len(self.inputEnd.get())):
                    if self.inputEnd.get()[y] == "0":
                        pass
                    elif int(self.inputEnd.get()[i]) > int(self.inputEnd.get()[y]):
                        count_start += 1
        # If both input states have odd number of inversions or if they both have even number of them, the case is solvable
        if count_start % 2 == 0 and count_end % 2 == 0:
            return True
        elif count_start % 2 == 1 and count_end % 2 == 1:
            return True
        # If they don't, the case isn't solvable
        else:
            return False

    # Counts, how much does the possible state differ from the end state (heuristic - how many tiles aren't in their possitions)
    def valueCounter(self, first, second, currentState, targetState) -> int:
        value = 0
        tryState = list(currentState)
        tryState[first] = tryState[second]
        tryState[second] = "0"
        finalState = ""
        for i in range(len(tryState)):
            finalState += tryState[i]
        tryHistory = currentState+finalState
        if tryHistory in self.stepsHistory:
            value = 100000
        else:
            for i in range(len(tryState)):
                if tryState[i] != targetState[i] and tryState[i] != "0":
                    value += 1
        return value

    # Changes state according to the input and returns it
    def stateChanger(self, first, second, currentState) -> str:
        changeState = list(currentState)
        changeState[first] = changeState[second]
        changeState[second] = "0"
        finalState = ""
        for y in range(len(changeState)):
            finalState += changeState[y]
        # Adding step into stepsHistory
        self.stepsHistory.append(currentState+finalState)
        return finalState

    # Returns last state
    def goBack(self) -> str:
        recurChange = list(self.stepsHistory[-1])
        curState = ""
        for z in range(9):
            curState += recurChange[z]
        return curState

if __name__ == '__main__':
    Puzzle()
