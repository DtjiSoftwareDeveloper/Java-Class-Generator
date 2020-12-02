"""
This file contains source code of the application "Java Class Generator".
Author: DtjiSoftwareDeveloper
"""


# Importing necessary library

import sys


# Creating static functions


def first_is_capital(string: str) -> str:
    return string[0].capitalize() + string[1::]


def generate_getter(attribute_name: str, attribute_type: str) -> str:
    return """
    public """ + str(attribute_type) + """ get""" + first_is_capital(str(attribute_name)) + """() {
        return """ + str(attribute_name) + """;
    }
"""


def generate_setter(attribute_name: str, attribute_type: str) -> str:
    return """
    public void set""" + first_is_capital(str(attribute_name)) + """(""" + str(attribute_type) + """ """ + str(attribute_name) + """) {
        this.""" + str(attribute_name) + """ = """ + str(attribute_name) + """;
    }
"""


# Creating the main function to run the application


def main():
    """
    This main function is used to run the application.
    :return: None
    """

    print("Welcome to 'Java Class Generator' by 'DtjiSoftwareDeveloper'.")
    print("In this application, you will generate a Java class in a short time.")
    print("The Java class generated will automatically have two constructors (one default and one taking ")
    print("all class attributes as parameters) and also getters and setters for all class attributes.")

    print("Enter 'Y' for yes.")
    print("Enter anything else for no.")
    continue_using: str = input("Do you want to continue using 'Java Class Generator'? ")
    while continue_using == "Y":
        class_name: str = input("Please enter the name of class you want to generate: ")
        class_attribute_names: list = []  # initial value
        class_attribute_types: list = []  # initial value
        class_attribute_visibilities: list = []  # initial value
        java_file_script: str = """
public class """ + str(class_name) + """ {
"""

        num_class_attributes: int = int(input("Please enter number of class attributes you want in your class: "))
        for i in range(num_class_attributes):
            class_attribute_name: str = input("Please enter name of the class attribute you want to add: ")
            class_attribute_type: str = input("Please enter the type of the class attribute you want to add: ")
            class_attribute_visibility: str = input("Please enter the visibility level of the class attribute "
                                                    "you want to add: ")
            class_attribute_names.append(class_attribute_name)
            class_attribute_types.append(class_attribute_type)
            class_attribute_visibilities.append(class_attribute_visibility)

        for i in range(num_class_attributes):
            java_file_script += """
    """ + str(class_attribute_visibilities[i]) + """ """ + str(class_attribute_types[i]) + """ """ + str(class_attribute_names[i]) + """; 
"""
        java_file_script += """
    public """ + str(class_name) + """(){
    
    }     
"""
        in_brackets: str = ""  # initial value
        for i in range(num_class_attributes):
            in_brackets += str(class_attribute_types[i]) + " " + str(class_attribute_names[i])
            if i < num_class_attributes - 1:
                in_brackets += ", "

        in_constructor_body: str = ""  # initial value
        for i in range(num_class_attributes):
            in_constructor_body += """
        this.""" + str(class_attribute_names[i]) + " = " + str(class_attribute_names[i]) + """;
"""

        java_file_script += """
    public """ + str(class_name) + """(""" + str(in_brackets) + """){
        """ + str(in_constructor_body) + """
    }        
"""

        for i in range(num_class_attributes):
            attribute_name: str = class_attribute_names[i]
            attribute_type: str = class_attribute_types[i]
            java_file_script += generate_getter(attribute_name, attribute_type)
            java_file_script += generate_setter(attribute_name, attribute_type)

        java_file_script += """
        
}"""

        file = open(str(class_name) + ".java", "w")
        file.write(java_file_script)
        file.close()

        print("Enter 'Y' for yes.")
        print("Enter anything else for no.")
        continue_using = input("Do you want to continue using 'Java Class Generator'? ")
    sys.exit()


if __name__ == '__main__':
    main()
