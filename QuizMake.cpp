#include <cctype>
#include <iostream>
#include <fstream>
#include <map>
#include <memory>
#include <string>
using namespace std;

class Quiz {
public:
    Quiz() {} // Default Constructor

    string getSubjectFolderPath(string subjectName) {
        return "subjects\\" + subjectName + ".txt";
    }

    // DISPLAY: MAIN MENU
    void displayMainMenu() {
        string mainMenuChoice, subjectInput;
        do {
            // Display Header
            cout << "\n ---------- | QuizMake | ----------";
            cout << "\ntype '/help' to display command list";
            cout << "\n>> ";
            getline(cin, mainMenuChoice);

            if (mainMenuChoice == "/help") {
                displayCommandList();
            }

            if (mainMenuChoice.substr(0, 4) == "/sub") {
                subjectInput = enterSubject(mainMenuChoice);
            }

            if (mainMenuChoice.substr(0, 6) == "/enter") {
                enterInformation(mainMenuChoice);
            }

        } while (true);
    }

    // VALIDATION: EXIT CODE
    string exitCode() {
        string input;
        getline(cin, input);
        if (input == "/r") {
            displayMainMenu();
        }
        if (input == "/exit") {
            exit(0);
        }
        return input;
    }

    // DISPLAY: COMMAND LIST
    void displayCommandList() { // Display the Command List
        cout << "\n  ---------- | QuizMake | ----------";
        cout << "\n           [ Command List ]";
        cout << "\n~ /sub() | enter subject";
        cout << "\n~ /enter() | enter content information";
        cout << "\n~ /set items() | set # of test items";
        cout << "\n~ /set type() | set quiz type(MC, Enum, T or F)";
        cout << "\n~ /set focus() | set quiz focus(Word, Definitiion, Both)";
        cout << "\n~ /start() | start the quiz";
        cout << "\n~ /help | display the command list";
        cout << "\n~ /r | return to main menu";
        cout << "\n~ /exit | exit the program";
        cout << "\n--------------------------------------";
    }

    // COMMAND: ENTER SUBJECT
    string enterSubject(string mainMenuChoice) { // Enter Subject
        string subject, subjectRead;
        for (int i = 4; i < mainMenuChoice.size(); i++) {
            if (!isalnum(mainMenuChoice[i])) { // If '('
                subjectRead += mainMenuChoice[i + 1]; // Read A Digit After
                if (!isalnum(mainMenuChoice[i + 2])) { // If ')' After a Digit
                } else {
                    subjectRead += mainMenuChoice[6];
                }
                break;
            }
        }
        return subjectRead;
    }

    // COMMAND: ENTER INFORMATION
    void enterInformation(string mainMenuChoice) { // Enter Quiz Information
        unsigned int wordCount;
        string word, definition, subjectName;
        bool validInformation;

        for (int i = 0; i < mainMenuChoice.size(); i++) {
            if (!isalnum(mainMenuChoice[6])) { // If '('
                while (isalnum(mainMenuChoice[6 + i]) || isspace(mainMenuChoice[6 + i])) {
                    subjectName += mainMenuChoice[6 + i]; // Read Subsequent Input
                }
            }
        }

        // Create File Text in Folder
        ofstream fileWriter(getSubjectFolderPath(subjectName));

            // Input Content to Text File
            if (fileWriter) {
                cout << "\n>> text file created";
            } else {
                cerr << "\ncannot_open_file";
            }

        // Display Header
        cout << "\n  ---------- | QuizMake | ----------";
        cout << "\n        [ Enter Information ]";
        cout << "\n[ Enter '|' at the end of definition ]";

        do { // Sentinel Loop
            do { // Error Loop: Valid Information
                validInformation = true;
                // Prompt Word
                cout << "\nWord: ";
                word = exitCode(); // Input Check: Exit Code
                // Error Check
                if (word.empty()) {
                    validInformation = false;
                }
                // Prompt Definition
                cout << "\nDefinition:\n";
                definition = exitCode(); // Input Check: Exit Code
                // Error Check
                if (definition.empty()) {
                    validInformation = false;
                }
            } while (!validInformation);

            fileWriter << wordCount + 1 << ". " << word << "\n";
            fileWriter << "---------------\n";
            fileWriter << "\t" << definition << "\n";

            wordCount++; // Increment
        } while (definition.back() != '|');

        cout << "\nTotal Words: " << wordCount;
    }
};

int main() {
    unique_ptr<Quiz> startProgram = make_unique<Quiz>();
    startProgram->displayMainMenu();
    // [DEBUGGING]
    return 0;
}