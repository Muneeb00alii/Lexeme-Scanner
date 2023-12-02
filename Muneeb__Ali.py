"""
This Code Mainly Performs 3 Tasks.

1. Get a Source Code Written in a txt File Named "Code" and Remove:
          
        1. Import Statements
        2. Docstring
        3. All Comments
        4. All Input Statements
        5. Blank Lines
        6. Empty Spaces

And Save the Modified Code in txt File Named "Output.01" and Also Print it on the Console.

2. Get the Modified Code Written in the txt File Named "Output.01" Which we have Saved in it in Task:01 then Put All the Code 
   into One Line With Semicolons at the end of each Line and "$" at the End of the Code and Save it in txt File Named "Output.02".

3. Get the Modified Code Written in the txt File Named "Output.02" Which we have Saved in it in Task:02 then Find All
   the Tokens And Put them in a List and Print Them on the Console As Well Count them And Print The Total Number of Tokens
   and then Print "The End".
"""

class FileReader:
    def __init__(self, file_path):
        self.file_path = file_path

    def read(self):
        with open(self.file_path, 'r') as file:
            return file.read()


class FileWriter:
    def __init__(self, file_path):
        self.file_path = file_path

    def write(self, code):
        with open(self.file_path, 'w') as file:
            file.write(code)


class CodeCleaner:
    def clean(self, code):
        lines = code.split('\n')
        cleaned_lines = []

        for line in lines:
            line_one_by_one = line.strip()
            if 'input' in line or 'import' in line or '#' in line or '"""' in line or "'''" in line:
                continue
            if line_one_by_one and not line_one_by_one.startswith(('import ', '#', '"""', "'''")):
                cleaned_lines.append(line)

        return '\n'.join(cleaned_lines)


class CodeJoiner:
    def join_lines(self, lines, separator, sentinel):
        lines = [line.strip() for line in lines if line.strip()]  # Removing empty lines
        joined_lines = separator.join(lines) + sentinel
        return joined_lines


class TokenMaker:
    def make_tokens(self, code):
        tokens = []
        current_token = ''
        docstring = False

        for word in code:
            if docstring:
                if '*/' in word:
                    docstring = False
            elif '/*' in word:
                docstring = True
            elif word.isalnum() or word == '_':
                current_token += word
            else:
                if current_token:
                    tokens.append(current_token)  # Filling the Tokens List
                    current_token = ''
                if word.isspace():  # Finding the Spaces in the Code
                    continue
                elif word == '#':  # Finding the Comments in the Code
                    while word != '\n':
                        word = next(code)
                else:
                    tokens.append(word)

        if current_token:
            tokens.append(current_token)

        return tokens


class CodeProcessor:
    def process_and_make_tokens(self, reader , writer_1, writer_2, cleaner, joiner, token_maker):
        input_code = reader.read()

        # Task 1: Cleaning Code
        cleaned_code = cleaner.clean(input_code)
        writer_1.write(cleaned_code)
        print(f"\nThis is the Output for Task:01\n\n{cleaned_code}\n")

        # Task 2: Joining Lines
        joined_lines_code = joiner.join_lines(cleaned_code.split('\n'), ' ; ', '$')
        writer_2.write(joined_lines_code)
        print(f"This is the Output for Task:02\n\n{joined_lines_code}\n")

        # Task 3: Finding Tokens
        tokens = token_maker.make_tokens(iter(cleaned_code))
        print(f"This is the Output for Task:03\n")

        counting = 0
        for token in tokens:
            counting = counting + 1
            print(f"{counting}.Lexeme: {token}")

        print(f"\nThe Total Number of Lexemes are:{counting}")

        print(f"\nThe End\n")

# Defining the File Paths (Use these Variables Instead of File Paths in the Code)

Source_Code_File_Path = "C:\\Users\\92321\\OneDrive\\Desktop\\Assignment.02\\Code.txt"
Output_01_File_Path = "C:\\Users\\92321\\OneDrive\\Desktop\\Assignment.02\\Output.01.txt"
Output_02_File_Path = "C:\\Users\\92321\\OneDrive\\Desktop\\Assignment.02\\Output.02.txt"

# # This is the Main Class in Which Class Relationship(Composition) is Applied.

# # This is Doing The Following Tasks:

# # 1.Processing
# # 2.Cleaning Code
# # 3.Joining Lines
# # 4.Making Tokens.

class Main():
    def processing(self):
        # Creating Instances of All Classes
        File_Reader = FileReader(Source_Code_File_Path)
        File_Writer_01 = FileWriter(Output_01_File_Path)
        File_Writer_02 = FileWriter(Output_02_File_Path)
        Code_Cleaner = CodeCleaner()
        Code_Joiner = CodeJoiner()
        Token_Maker = TokenMaker()
        Code_Processor = CodeProcessor()

        Code_Processor.process_and_make_tokens(File_Reader,File_Writer_01,File_Writer_02,Code_Cleaner,Code_Joiner,Token_Maker)

Main().processing()