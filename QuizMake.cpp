#include <cctype>
#include <iostream>
#include <filesystem>
#include <fstream>
#include <map>
#include <memory>
#include <string>
using namespace std;

class Quiz {
public:
    Quiz() {} // Default Constructor

    string getSubjectFolderPath(string subjectName) {
        return "Subjects\\" + subjectName;
    }

    string getSubjectFolderPathText(string subjectTopic, string subjectName) {
        return "Subjects\\" + subjectTopic + "\\" + subjectName + ".txt";
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
        string subjectName;

        size_t startPosition = mainMenuChoice.find('('); // Find Opening Parenthesis
        if (startPosition == string::npos) { // Check if .find was unsuccessful
            cerr << "\nERROR | missing_open_parenthesis";
        }

        size_t endPosition = mainMenuChoice.find(')'); // Find Closing Parenthesis
        if (endPosition == string::npos) { // Check if .find was unsuccessful
            cerr << "\nERROR | missing_close_parenthesis";
        }

        subjectName = mainMenuChoice.substr(startPosition + 1, startPosition - endPosition - 1); // Get Subject Name
        subjectName.erase(0, subjectName.find_first_not_of(' ')); // Trim Left Whitespaces
        subjectName.erase(subjectName.find_last_not_of(' ' + 1)); // Trim Right Whitespaces

        if (filesystem::create_directory(getSubjectFolderPath(subjectName))) { // Create Folder in Directory
            cout << "\n>> folder created: " << subjectName;
        } else { // Error Handling: Existing Folder
            cerr << "\nERROR | folder_already_exists";
        }

        return subjectName;
    }

    // COMMAND: ENTER INFORMATION
    string enterInformation(string mainMenuChoice) { // Enter Quiz Information
        string word, definition, subjectName, subjectTopic;
        unsigned int wordCount;
        size_t counter = 1;
        bool validInformation, isValidTopic;

        size_t startPosition = mainMenuChoice.find('('); // Find Opening Parenthesis
        if (startPosition == string::npos) { // Check if .find was unsuccessful
            cerr << "\nERROR | missing_open_parenthesis";
        }

        size_t endPosition = mainMenuChoice.find(')'); // Find Closing Parenthesis
        if (endPosition == string::npos) { // Check if .find was unsuccessful
            cerr << "\nERROR | missing_close_parenthesis";
        }

        // Get Subject Name
        subjectTopic = mainMenuChoice.substr(startPosition + 1, startPosition - endPosition - 1); // Get Subject Name
        subjectTopic.erase(0, subjectTopic.find_first_not_of(' ')); // Trim Left Whitespaces
        subjectTopic.erase(subjectTopic.find_last_not_of(' ' + 1)); // Trim Right Whitespaces

        do { // Error Loop
            isValidTopic = true;
            cout << "\nEnter Topic: ";
            getline(cin, subjectName);

            if (subjectName.empty()) {
                isValidTopic = false;
                cerr << "\nERROR | invalid_topic";
            }
        } while (!isValidTopic);

        // Create File Text in Folder
        ofstream fileWriter(getSubjectFolderPathText(subjectTopic, subjectName));

            // Input Content to Text File
            if (fileWriter) {
                cout << "\n>> text file created";
            } else {
                cerr << "\nERROR | cannot_open_file";
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
