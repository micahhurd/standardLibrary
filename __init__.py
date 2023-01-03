# File Functions ---------------------------------------
def check_if_module_imported(modulename):
    import sys

    if modulename not in sys.modules:
        return False
    else:
        return True


def return_cwd():
    import os

    cwd = os.getcwd() + "\\"
    return cwd


def readConfigFile(filename, searchTag, sFunc="", default_value='', errorVal='Searched term could not be found'):
    output = errorVal

    try:
        searchTag = searchTag.lower()
        # print("Search Tag: ",searchTag)

        # Open the file
        with open(filename, "r") as filestream:
            # Loop through each line in the file

            for line in filestream:

                if line[0] != "#":

                    currentLine = line
                    equalIndex = currentLine.find('=')
                    if equalIndex != -1:

                        tempLength = len(currentLine)
                        # print("{} {}".format(equalIndex,tempLength))
                        tempIndex = equalIndex
                        configTag = currentLine[0:(equalIndex)]
                        configTag = configTag.lower()
                        configTag = configTag.strip()
                        # print(configTag)

                        configField = currentLine[(equalIndex + 1):]
                        configField = configField.strip()
                        # print(configField)

                        # print("{} {}".format(configTag,searchTag))
                        if configTag == searchTag:

                            # Split each line into separated elements based upon comma delimiter
                            # configField = configField.split(",")

                            # Remove the newline symbol from the list, if present
                            lineLength = len(configField)
                            lastElement = lineLength - 1
                            try:
                                if configField[lastElement] == "\n":
                                    configField.remove("\n")
                            except:
                                configField.strip()
                            # Remove the final comma in the list, if present
                            lineLength = len(configField)
                            lastElement = lineLength - 1

                            try:
                                if configField[lastElement] == ",":
                                    configField = configField[0:lastElement]
                            except:
                                pass

                            lineLength = len(configField)
                            lastElement = lineLength - 1

                            # Apply string manipulation functions, if requested (optional argument)
                            if sFunc != "":
                                sFunc = sFunc.lower()

                                if sFunc == "listout":
                                    configField = configField.split(",")

                                if sFunc == "stringout":
                                    configField = configField.strip("\"")

                                if sFunc == "int":
                                    configField = int(configField)

                                if sFunc == "float":
                                    configField = float(configField)

                            output = configField

        filestream.close()
    except Exception as e:
        print(f'Configuration Read Error: {e}')
        time.sleep(5)
        output = default_value

    if output == errorVal and default_value != '':
        output = default_value


    return output


class readConfigFileV2:

    def __init__(self, config_file_filepath, default_value='', errorVal='Searched term could not be found'):
        self.config_file_filepath = config_file_filepath
        self.default_value = default_value
        self.errorVal = errorVal

    def get(self, searchTag, sFunc="", default_value="", errorVal=""):
        if default_value == "":
            default_value = self.default_value

        if errorVal == "":
            errorVal = self.errorVal

        output = errorVal

        try:
            searchTag = searchTag.lower()
            # print("Search Tag: ",searchTag)

            # Open the file
            with open(self.config_file_filepath, "r") as filestream:
                # Loop through each line in the file

                for line in filestream:

                    if line[0] != "#":

                        currentLine = line
                        equalIndex = currentLine.find('=')
                        if equalIndex != -1:

                            tempLength = len(currentLine)
                            # print("{} {}".format(equalIndex,tempLength))
                            tempIndex = equalIndex
                            configTag = currentLine[0:(equalIndex)]
                            configTag = configTag.lower()
                            configTag = configTag.strip()
                            # print(configTag)

                            configField = currentLine[(equalIndex + 1):]
                            configField = configField.strip()
                            # print(configField)

                            # print("{} {}".format(configTag,searchTag))
                            if configTag == searchTag:

                                # Split each line into separated elements based upon comma delimiter
                                # configField = configField.split(",")

                                # Remove the newline symbol from the list, if present
                                lineLength = len(configField)
                                lastElement = lineLength - 1
                                try:
                                    if configField[lastElement] == "\n":
                                        configField.remove("\n")
                                except:
                                    configField.strip()
                                # Remove the final comma in the list, if present
                                lineLength = len(configField)
                                lastElement = lineLength - 1

                                try:
                                    if configField[lastElement] == ",":
                                        configField = configField[0:lastElement]
                                except:
                                    pass

                                lineLength = len(configField)
                                lastElement = lineLength - 1

                                # Apply string manipulation functions, if requested (optional argument)
                                if sFunc != "":
                                    sFunc = sFunc.lower()

                                    if sFunc == "listout":
                                        configField = configField.split(",")

                                    if sFunc == "stringout":
                                        configField = configField.strip("\"")

                                    if sFunc == "int":
                                        configField = int(configField)

                                    if sFunc == "float":
                                        configField = float(configField)

                                output = configField

            filestream.close()
        except Exception as e:
            print(f'Configuration Read Error: {e}')
            output = default_value

        if output == errorVal and default_value != '':
            output = default_value


        return output


def check_and_create_path(path, autocreate=True):
    import os
    path = os.path.dirname(path)
    error_info = ''
    if not os.path.exists(path):
        if autocreate:
            try:
                os.mkdir(path)
                return True, error_info
            except Exception as error:
                return False, error
        else:
            return False, error_info
    else:
        return True, error_info


def file_check_exists(file):
    import os
    if not os.path.exists(file):
        return False
    else:
        return True


def clear():  # Clears the console
    # for windows
    from os import system, name
    if name == 'nt':
        _ = system('cls')

        # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def readTxtFile(filename, outputFormat="list"):
    # Place contents of text files into variable

    if outputFormat == "str":
        output_list = ""
        with open(filename, "r") as f:
            for item in f:
                output_list += item
        return output_list

    elif outputFormat == "list":
        f = open(filename, 'r')
        x = f.readlines()
        f.close()
        return x

    else:
        return ""


def write_str_to_file(str_data, filepathName, writemode="rename"):

    success_bool = False
    try:
        check_and_create_path(filepathName, autocreate=True)

        if writemode == "rename":
            filepathName = rename_if_file_exists(filepathName)
            writemode = 'w'

        if writemode == 'w':
            try:
                with open(filepathName, 'w') as filehandle:
                    filehandle.write(str_data)

            except Exception as err:
                print(err)
                with open(filepathName, 'a') as filehandle:
                    filehandle.write(str_data)
        else:
            try:
                with open(filepathName, 'a') as filehandle:
                    filehandle.write(str_data)
            except Exception as err:
                with open(filepathName, 'w') as filehandle:
                    filehandle.write(str_data)

        success_bool = True

    except Exception as err:
        printLog(f"Failed to write file:\n\n{filepathName}\n\ndue to Exception:\n\n{err}")

    return (success_bool, filepathName)


def import_txt_file(file_path: str) -> list:
    output_list = []

    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            for item in f:
                cleaned_item = item.strip('\n')
                output_list.append(cleaned_item)

    return output_list


def standardize_file_path_format(input_file_path_string):
    import ntpath
    # I wrote this module to standardize file path strings used inside Python programs
    # This allows the differeces between UNIX and Windows style file paths to be eliminated
    # requires the ntpath module
    path, file = ntpath.split(input_file_path_string)
    if path[0] == '\\' and path[1] == '\\':
        path_slash = '\\'
        windows_network_path = True
    elif path[0] == '/' and path[1] == '/':
        path_slash = '\\'
        windows_network_path = True
    else:
        windows_network_path = False
        path_slash = '/'

    if windows_network_path:
        path = path.replace('/', '\\')
    else:
        path = path.replace('\\', '/')

    new_path = ''
    for index, character in enumerate(path):
        last_character = path[index-1]

        if index > 1:
            if character == path_slash and last_character == path_slash:
                character = ''

        new_path += character

    return f'{new_path}{path_slash}{file}'


def init_log(log_file_name="logfile.log"):
    global log
    import logging as log
    logFile = log_file_name
    log.basicConfig(filename=logFile, filemode='a', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    datefmt='%d-%b-%y %H:%M:%S', level=log.INFO)
    log.info("=========================== New Porgram Instance ===========================")


def printLog(stringMessage, errorInfo=False, console=True):


    # This module allows for printing to the console and to the log in a single line of code; reduces code clutter
    # To use this function you must have imported the logging module and configured it. For example:
    # import logging as log
    # log.basicConfig(filename=logFile, filemode='a', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', level=logging.INFO)
    if not 'log' in globals():
        init_log()

    if console:
        print(stringMessage)

    if errorInfo:
        log.info(stringMessage, exc_info=errorInfo)
    else:
        log.info(stringMessage)


def rename_if_file_exists(filename):
    import os
    import pathlib
    new_filename = filename

    file_exists = os.path.exists(filename)

    cntr = 0
    while file_exists:
        cntr+=1
        file_extension = pathlib.Path(new_filename).suffix
        filename_wout_extension = filename.strip(file_extension)

        copy_str = " - Copy("
        if copy_str in filename_wout_extension:
            index_loc = filename_wout_extension.find(copy_str)
            filename_wout_extension = filename_wout_extension[:index_loc]

        new_filename = f'{filename_wout_extension} - Copy({cntr}){file_extension}'

        file_exists = os.path.exists(new_filename)

    return new_filename


def copy_file(srcFile, dstFolder):
    import shutil
    import os

    cwd = return_cwd()
    relative_directory = "./"

    srcFile = standardize_file_path_format(srcFile)

    baseFilename = os.path.basename(srcFile)

    newFilenamePath = f"{dstFolder}/{baseFilename}"
    newFilenamePath = standardize_file_path_format(newFilenamePath)

    if relative_directory in srcFile:
        srcFile = srcFile.replace(relative_directory, cwd)
        srcFile = standardize_file_path_format(srcFile)

    if relative_directory in newFilenamePath:
        newFilenamePath = newFilenamePath.replace(relative_directory, cwd)
        newFilenamePath = standardize_file_path_format(newFilenamePath)

    print(f"Old Filename: {newFilenamePath}")

    newFilenamePath = rename_if_file_exists(newFilenamePath)

    print(f"New Filename: {newFilenamePath}")

    success_flag, error = check_and_create_path(newFilenamePath, autocreate=True)
    # input(error)

    # 2nd option
    shutil.copy(srcFile, newFilenamePath)  # dst can be a folder; use shutil.copy2() to preserve timestamp


def writeListToFile(filename, my_list, write_type='w'):
    def ensure_file_exists(filepath):
        if not os.path.exists(filepath):
            with open(filepath, 'w') as fp:
                pass

    def write_list_normal(filename, write_type):
        with open(filename, write_type) as f:
            for item in my_list:
                f.write("%s\n" % item)

    def write_list_utf8(filename, write_type):
        with open(filename, write_type, encoding="utf-8") as f:
            for item in my_list:
                f.write("%s\n" % item)

    ensure_file_exists(filename)

    try:
        write_list_normal(filename, write_type)
    except Exception as e:
        error = f'{e}'
        error = error.lower()
        if 'permission denied' in error:
            temp_str = f'Access Denied for file: {filename}\n\n' \
                       f'Please ensure the file is not in use by another program before proceeding!'
            msg_box_simple(temp_str)
            write_list_normal(filename, write_type)
        else:
            write_list_utf8(filename, write_type)


def verify_file_paths(file_check_list):
    overall_temp_bool = True
    false_list = []
    for item in file_check_list:
        tempBool = file_check_exists(item)

        if tempBool == False:
            overall_temp_bool = False
            printLog(f'File or Folder path from configuration file does not exist: {item}')
            false_list.append(item)

    if overall_temp_bool == False:

        temp_str = f'One or more configuration File or Folder path did not exist: \n\n'
        for item in false_list:
            temp_str = temp_str + f'- {item}\n'

        temp_str = temp_str + f'\nPlease fix the broken files / paths and re-run the program.'
        printLog(temp_str)
        error_and_exit(temp_str)


def is_file_empty(filepath):
    # check if file exists
    if os.path.exists(filepath):
        # check if size of file is 0
        if os.stat(filepath).st_size == 0:
            return True
        else:
            return False
    else:
        return True


# UI Functions ----------------------------------------
def userInterfaceHeader(program, cs_num, version, cwd, logFile, msg=""):
    print(program + ", Version " + str(version))
    print(f"Procedure: {cs_num}")
    print("Current Working Directory: " + str(cwd))
    print("Log file located at working directory: " + str(logFile))
    print("=======================================================================")
    if msg != "":
        print(msg)
        print("_______________________________________________________________________")
    return 0


def printInLine(inputString):
    import os
    maxLength = 121
    os.system('mode con: cols={} lines=40'.format(maxLength+1))
    inputString = str(inputString)
    inputStringLength = len(inputString)
    stringAdder = maxLength - inputStringLength
    if stringAdder < 0:
        inputString = inputString[:stringAdder]
        stringAdder = 0

    inputString += (" " * stringAdder)
    print("{}\r\r".format(inputString), end="")


def list_selection_box(input_list, field1='', field2='', window_title='', button_label='Select', width=150, height=30):

    import PySimpleGUI as sg

    """
        Allows you to "browse" through the Theme settings.  Click on one and you'll see a
        Popup window using the color scheme you chose.  It's a simple little program that also demonstrates
        how snappy a GUI can feel if you enable an element's events rather than waiting on a button click.
        In this program, as soon as a listbox entry is clicked, the read returns.
    """

    sg.theme('System Default')

    layout = [[sg.Text(field1)],
              [sg.Text(field2)],
              ### [sg.Listbox(values=sg.theme_list(), size=(150, 30), key='-LIST-', enable_events=True)],
              [sg.Listbox(values=input_list, size=(width, height), key='-LIST-', enable_events=True)],
              [sg.Button(button_label)]]

    window = sg.Window(window_title, layout, keep_on_top=True)

    while True:  # Event Loop
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Select'):
            # sg.theme(values['-LIST-'][0])
            # sg.popup_get_text('This is {}'.format(values['-LIST-'][0]))
            selected = format(values['-LIST-'][0])
            # print(f'selected: {selected}')
            break

    window.close()

    return selected


def text_entry_box(title='test', field1='field1', field2='field2'):
    import PySimpleGUI as sg

    sg.theme('System Default')  # Add some color to the window

    # Very basic window.  Return values using auto numbered keys

    layout = [
        [sg.Text(field1)],
        [sg.Text(field2, size=(15, 1)), sg.InputText()],
        # [sg.Text('Address', size=(15, 1)), sg.InputText()],
        # [sg.Text('Phone', size=(15, 1)), sg.InputText()],
        # [sg.Submit(), sg.Cancel()]
        [sg.Submit()]
    ]

    window = sg.Window(title, layout, keep_on_top=True)
    event, values = window.read()
    window.close()
    # print(event, values[0], values[1], values[2])  # the input data looks like a simple list when auto numbered
    return values[0]


def msg_box_simple(message_string):
    import PySimpleGUI as sg

    sg.theme('System Default')  # Add some color to the window

    sg.Popup(message_string, keep_on_top=True)


def yes_no_popup_simple(message_string):
    import PySimpleGUI as sg

    sg.theme('System Default')  # Add some color to the window

    window = sg.popup_yes_no(message_string, keep_on_top=True)
    tempBool = True if window == 'Yes' else False

    return tempBool


def yes_no_other_popup(message_string, other_str_text='  Skip ', btn_focus=1, window_title='Message Prompt', lineLength=40):
    import PySimpleGUI as sg
    y_focus = False
    n_focus = False
    o_focus = False

    btn_focus_type_check = f'{type(btn_focus)}'
    if not 'int' in btn_focus_type_check:
        btn_focus = 1

    if btn_focus == 1:
        y_focus = True
    elif btn_focus == 0:
        n_focus = True
    else:
        o_focus = True

    # lineLength = 40

    formatted_msg = ''
    cntr = 0
    for index, item in enumerate(message_string):
        formatted_msg += item
        cntr += 1

        if item == " ":
            spliced_str = message_string[index+1:]
            cntr2 = 0
            for item in spliced_str:
                if item == " ":
                    break
                cntr2+=1

            if cntr + cntr2 >= lineLength:
                formatted_msg += '\n'
                cntr = 0

        elif cntr >= lineLength:
            if not message_string[index+1] == " ":
                formatted_msg += '-\n'
            else:
                formatted_msg += '\n'
            cntr = 0


    sg.theme('System Default')

    layout = [[sg.Text(formatted_msg)],
              [sg.Text(' ' * lineLength)],
              [sg.Button('  Yes  ', key='-yes-', focus=y_focus), sg.Button('  No   ', key='-no-', focus=n_focus), sg.Button(other_str_text, key='-other-', focus=o_focus)],
              ]
    # Create the Window
    window = sg.Window(window_title, layout, keep_on_top=True, use_default_focus=False)

    while True:
        event, values = window.read()
        event_str = f'{event}'
        print(f'event: {event_str}')
        if 'yes' in event_str:
            return_val = 1
            break
        elif 'no' in event_str:
            return_val = 0
            break
        elif 'other' in event_str:
            return_val = -1
            break

        if event in (sg.WIN_CLOSED, 'Continue'):
            break
        if event == 'close':
            break

    window.close()

    return return_val


def file_browse_window(ext_description='ALL Files', ext_type='*.*', intial_folder='', title='', message='Click button below to choose file',
                       button_text='Browse'):
    import PySimpleGUI as sg

    sg.theme('System Default')

    file_browse_parameters = sg.FileBrowse(button_text = button_text,
        file_types = ((ext_description, ext_type),),
        initial_folder = intial_folder,
        )

    layout = [[sg.Text(message)],
              [sg.Input(key='-FILE-', visible=False, enable_events=True), file_browse_parameters]]

    event, values = sg.Window(title, layout).read(close=True)

    return f'{values["-FILE-"]}'


def error_and_exit(messag='', pause_time=1, pause=False):
    temp_string = f'Fatal Error!\n\n{messag}\n\nProgram will now terminate.'
    try:
        msg_box_simple(temp_string)
    except:
        pass
    
    if pause:
        printLog(temp_string)
        input("Press Enter to exit...")
    else:
        printLog(temp_string)
        print(f'Closing in {pause_time} seconds...')
        time.sleep(pause_time)
    exit()


def plot_data(input_filepath, output_filepath, plt_x=15, plt_y=8):
    import matplotlib.pyplot as plt
    import math

    input_data_list = readTxtFile(input_filepath)

    for index, item in enumerate(input_data_list):
        item = item.strip()
        input_data_list[index] = item

    # Delete first line of the data, which contains the header info
    del input_data_list[0]

    nominal_step = []
    nominal_val = []
    msmt_val = []
    upper_limit = []
    lower_limit = []
    upper_unc = []
    lower_unc = []
    for item in input_data_list:
        temp_list = item.split(",")
        # print(temp_list)

        step = float(temp_list[0])

        mw_lower = float(temp_list[3])
        mw_msd = float(temp_list[4])
        mw_upper = float(temp_list[5])
        mw_unc = float(temp_list[6])
        mw_nom = (mw_lower + mw_upper) / 2

        dbm_lower = 10*math.log10(mw_lower)
        dbm_msd = 10 * math.log10(mw_msd)
        dbm_upper = 10 * math.log10(mw_upper)
        dbm_nom = 10 * math.log10(mw_nom)

        dbm_unc_lower = 10 * math.log10((mw_msd - mw_unc))
        dbm_unc_upper = 10 * math.log10((mw_msd + mw_unc))

        msd_normalized = dbm_msd - dbm_nom

        limit_normalized_lower = dbm_lower - dbm_nom
        limit_normalized_upper = dbm_upper - dbm_nom

        unc_normalized_lower = dbm_unc_lower - dbm_nom
        unc_normalized_upper = dbm_unc_upper - dbm_nom

        nominal_step.append(step)
        nominal_val.append(0)
        msmt_val.append(msd_normalized)
        lower_limit.append(limit_normalized_lower)
        upper_limit.append(limit_normalized_upper)
        lower_unc.append(unc_normalized_lower)
        upper_unc.append(unc_normalized_upper)


    plot_filename = output_filepath
    plt.rcParams["figure.figsize"] = (plt_x, plt_y)
    ax = plt.gca()
    ax.grid(True)
    plt.plot(nominal_step, nominal_val, '.', label="Nominal", color='green')
    plt.plot(nominal_step, msmt_val, label="DUT Msd.")
    plt.plot(nominal_step, upper_limit, 'b-', label="Limit", color='red')
    plt.plot(nominal_step, lower_limit, 'b-', color='red')
    plt.plot(nominal_step, upper_unc, '-.', label="Unc", color='orange')
    plt.plot(nominal_step, lower_unc, '-.', color='orange')
    plt.xticks(rotation=-90)
    # naming the x axis
    plt.xlabel('Linearity Step (dBm)')
    plt.xticks(nominal_step)
    # naming the y axis
    plt.ylabel('Delta Nominal (dB)')
    # giving a title to my graph
    plt.title(f'Linearity Test Result\n'
              f'File: {output_filepath}')

    # show a legend on the plot
    plt.legend()

    # Save the smoothing plot
    plt.savefig(plot_filename)
    # plt.show()
    try:
        plt.cla()
    except:
        pass
    try:
        plt.clf()
    except:
        pass
    try:
        plt.close()
    except:
        pass

    return plot_filename


def set_console_size(x=120, y=50):
    import os

    cmd = f'mode {x},{y}'
    os.system(cmd)


def printProgressBar(iteration, total, prefix='', suffix='', decimals=1, length=100, fill='█', printEnd="\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end=printEnd)
    # Print New Line on Complete
    if iteration == total:
        print()


def DisplayImage_pysimplegui(img_filename, text="", title='Image Viewer', button_name="Continue", xSize=800, ySize=600):
    from PIL import Image
    import io
    import PySimpleGUI as sg

    if not os.path.exists(img_filename):
        error_and_exit(f"Image at \n\n{img_filename}\n\n does not exist!")

    image = Image.open(img_filename)
    image.thumbnail((ySize, xSize))
    bio = io.BytesIO()
    image.save(bio, format="PNG")



    layout = [
        [sg.Image(key="-IMAGE-", data=bio.getvalue())],

        [
            sg.Text(text),
            # sg.Input(size=(25, 1), key="-FILE-"),
            # sg.FileBrowse(file_types=file_types),

        ],
        [sg.Button(button_name)]
    ]
    window = sg.Window(title, layout)

    while True:
        event, values = window.read()
        if event == button_name or event == sg.WIN_CLOSED:
            break

    window.close()


# Math Functions --------------------------------------
def dBm_to_percent(dBm_initial, dBm_delta):
    dB = dBm_delta - dBm_initial
    percent = ((10 ** (dB / 10)) - 1) * 100
    return percent


def dBm_mW(dBm):
    value_mW = 10**(dBm/10)
    return value_mW


def mW_dBm(mW):
    import math

    value_dBm = 10 * math.log10(mW)
    return value_dBm


def percent_to_dB(value_as_a_percent):
    import math
    dB = 10 * math.log10((value_as_a_percent + 100) / 100)
    return dB


def dBtoPercent(dB_input):
    return ((10 ** ((dB_input) / 10)) - 1) * 100


def SwrToRho(InputValue):
    return (InputValue - 1)/(InputValue + 1)


def RhoToSwr(InputValue):
    return (1 + InputValue) / (1 - InputValue)


def dbToRho(InputValue):
    InputValue = abs(InputValue)
    return 10 ** ((InputValue * -1) / 20)


def RhoToDb(InputValue):
    import math
    InputValue = abs(InputValue)
    # PrintAndLog("Rho To Db Conversion Input: {}".format(InputValue), logFile, debugBool)
    result = -20 * math.log(InputValue,10)
    # PrintAndLog("Rho To Db Conversion Output: {}".format(result), logFile, debugBool)
    return result


def SwrToDb(InputValue):
    import math
    swr_To_Rho = (InputValue - 1)/(InputValue + 1)
    rho_To_Db = (-20 * math.log(swr_To_Rho,10))
    return rho_To_Db


def dbToSwr(InputValue):
    InputValue = abs(InputValue)
    db_To_Rho = 10 ** ((InputValue * -1) / 20)
    rho_To_SWR = (1 + db_To_Rho) / (1 - db_To_Rho)
    return rho_To_SWR


def ConvertRadiansToDegrees(ValueInRadians):
    # Converts a given value in radians to degrees
    import math
    ValueInDegrees = ValueInRadians * (180 / math.pi)
    return ValueInDegrees


def calc_resol_qty(input_float, additonal_res=4, debug=False):
    try:
        input_float = float(input_float)
    except:
        print(f"Input value {input_float} is not a float!")
        return 0

    input_str = f'{input_float}'

    cntr = 0
    found_period = False
    for character in input_str:
        if debug:
            print(character)
        if not (character == "0" or character == ".") and found_period == False:
            break

        elif character == ".":
            found_period = True

        elif found_period:
            if character == "0":
                cntr+=1
            else:
                break

    if debug:
        print(f'Found {cntr} zeroes')
    res_qty = cntr + additonal_res
    return (res_qty)


def RhoToSwr_Uncertainty(Rho_Value, Rho_Unc):
    UpperRange = Rho_Value + Rho_Unc
    ConvertedUpperRange = (1 + UpperRange) / (1 - UpperRange)
    ConvertedMeasuredValue = (1 + Rho_Value) / (1 - Rho_Value)

    return abs(ConvertedUpperRange - ConvertedMeasuredValue)


def RhoToDb_Uncertainty(Rho_Value, Rho_Unc):
    import math

    UpperRange = Rho_Value + Rho_Unc
    ConvertedUpperRange = -20 * math.log(UpperRange, 10)
    ConvertedMeasuredValue = -20 * math.log(Rho_Value, 10)

    return abs(ConvertedUpperRange - ConvertedMeasuredValue)


def DbToRho_Uncertainty(dB_Value, dB_Unc):
    import math

    UpperRange = dB_Value + dB_Unc
    ConvertedUpperRange = dbToRho(UpperRange)
    ConvertedMeasuredValue = dbToRho(dB_Value)

    return abs(ConvertedUpperRange - ConvertedMeasuredValue)


def convert_to_eng_notation(input_val):
    # outputs a string
    import decimal
    x = decimal.Decimal(input_val)
    x = x.normalize()
    x = x.to_eng_string()
    return x



# Metrology Functions --------------------------------
def setSigDigits(value, qtySigDigitsRequired):
    import math

    valueAsFloat = float(value)

    if qtySigDigitsRequired < 1:
        qtySigDigitsRequired = 1

    SciNotationDigits = qtySigDigitsRequired - 1

    NewValue = "{:0.{}e}".format(valueAsFloat, SciNotationDigits)

    index = NewValue.find("e")
    qtyOfZeros = NewValue[(index + 1):]
    qtyOfZeros = int(qtyOfZeros)

    if qtyOfZeros < 0:
        qtyOfZeros = abs(qtyOfZeros) - 1
        BaseNumber = str(NewValue[:index])
        BaseNumber = BaseNumber.replace(".", "")

        NewStringValue = "0."
        for i in range(qtyOfZeros):
            NewStringValue += "0"
        NewStringValue += BaseNumber
    elif qtyOfZeros == 0:
        NewStringValue = NewValue[:index]
    elif qtyOfZeros > 0:
        NewStringValue = float(NewValue)
        CheckString = str(NewStringValue)
        FloorValue = math.floor(NewStringValue)

        remainder = NewStringValue - FloorValue
        if remainder == 0:
            NewStringValue = int(NewStringValue)

    return str(NewStringValue)


def Students_T_Lookup(DegreesOfFreedom, Confidence=95.45):
    # This function pulls the student's T coverage factor from a series of lists, corresponding to the user input
    # degrees of freedom and a selectable confidence interval of 90%, 95%, 95.45%, 99%, 99.5%, 99.73%, and 99.9%
    # The function defaults to 95.45% if no confidence interval is entered
    # If degrees of freedom is set to zero then the function assigns infinite degrees of freedom

    Confidence_90 = [1.645, 6.314, 2.920, 2.353, 2.132, 2.015, 1.943, 1.895, 1.860, 1.833, 1.812, 1.796, 1.782, 1.771,
                     1.761, 1.753, 1.746, 1.740, 1.734, 1.729, 1.725, 1.721, 1.717, 1.714, 1.711, 1.708, 1.706, 1.703,
                     1.701, 1.699, 1.697, 1.696, 1.694, 1.692, 1.691, 1.690, 1.688, 1.687, 1.686, 1.685, 1.684, 1.683,
                     1.682, 1.681, 1.680, 1.679, 1.679, 1.678, 1.677, 1.677, 1.676, 1.675, 1.675, 1.674, 1.674, 1.673,
                     1.673, 1.672, 1.672, 1.671, 1.671, 1.670, 1.670, 1.669, 1.669, 1.669, 1.668, 1.668, 1.668, 1.667,
                     1.667, 1.667, 1.666, 1.666, 1.666, 1.665, 1.665, 1.665, 1.665, 1.664, 1.664, 1.664, 1.664, 1.663,
                     1.663, 1.663, 1.663, 1.663, 1.662, 1.662, 1.662, 1.662, 1.662, 1.661, 1.661, 1.661, 1.661, 1.661,
                     1.661, 1.660, 1.660]
    Confidence_95 = [1.960, 12.706, 4.303, 3.182, 2.776, 2.571, 2.447, 2.365, 2.306, 2.262, 2.228, 2.201, 2.179, 2.160,
                     2.145, 2.131, 2.120, 2.110, 2.101, 2.093, 2.086, 2.080, 2.074, 2.069, 2.064, 2.060, 2.056, 2.052,
                     2.048, 2.045, 2.042, 2.040, 2.037, 2.035, 2.032, 2.030, 2.028, 2.026, 2.024, 2.023, 2.021, 2.020,
                     2.018, 2.017, 2.015, 2.014, 2.013, 2.012, 2.011, 2.010, 2.009, 2.008, 2.007, 2.006, 2.005, 2.004,
                     2.003, 2.002, 2.002, 2.001, 2.000, 2.000, 1.999, 1.998, 1.998, 1.997, 1.997, 1.996, 1.995, 1.995,
                     1.994, 1.994, 1.993, 1.993, 1.993, 1.992, 1.992, 1.991, 1.991, 1.990, 1.990, 1.990, 1.989, 1.989,
                     1.989, 1.988, 1.988, 1.988, 1.987, 1.987, 1.987, 1.986, 1.986, 1.986, 1.986, 1.985, 1.985, 1.985,
                     1.984, 1.984, 1.984]
    Confidence_9545 = [2.000, 13.968, 4.527, 3.307, 2.869, 2.649, 2.517, 2.429, 2.366, 2.320, 2.284, 2.255, 2.231,
                       2.212, 2.195, 2.181, 2.169, 2.158, 2.149, 2.140, 2.133, 2.126, 2.120, 2.115, 2.110, 2.105, 2.101,
                       2.097, 2.093, 2.090, 2.087, 2.084, 2.081, 2.079, 2.076, 2.074, 2.072, 2.070, 2.068, 2.066, 2.064,
                       2.063, 2.061, 2.060, 2.058, 2.057, 2.056, 2.055, 2.053, 2.052, 2.051, 2.050, 2.049, 2.048, 2.047,
                       2.046, 2.046, 2.045, 2.044, 2.043, 2.043, 2.042, 2.041, 2.040, 2.040, 2.039, 2.039, 2.038, 2.037,
                       2.037, 2.036, 2.036, 2.035, 2.035, 2.034, 2.034, 2.033, 2.033, 2.033, 2.032, 2.032, 2.031, 2.031,
                       2.031, 2.030, 2.030, 2.029, 2.029, 2.029, 2.028, 2.028, 2.028, 2.028, 2.027, 2.027, 2.027, 2.026,
                       2.026, 2.026, 2.026, 2.025]
    Confidence_99 = [2.576, 63.657, 9.925, 5.841, 4.604, 4.032, 3.707, 3.499, 3.355, 3.250, 3.169, 3.106, 3.055, 3.012,
                     2.977, 2.947, 2.921, 2.898, 2.878, 2.861, 2.845, 2.831, 2.819, 2.807, 2.797, 2.787, 2.779, 2.771,
                     2.763, 2.756, 2.750, 2.744, 2.738, 2.733, 2.728, 2.724, 2.719, 2.715, 2.712, 2.708, 2.704, 2.701,
                     2.698, 2.695, 2.692, 2.690, 2.687, 2.685, 2.682, 2.680, 2.678, 2.676, 2.674, 2.672, 2.670, 2.668,
                     2.667, 2.665, 2.663, 2.662, 2.660, 2.659, 2.657, 2.656, 2.655, 2.654, 2.652, 2.651, 2.650, 2.649,
                     2.648, 2.647, 2.646, 2.645, 2.644, 2.643, 2.642, 2.641, 2.640, 2.640, 2.639, 2.638, 2.637, 2.636,
                     2.636, 2.635, 2.634, 2.634, 2.633, 2.632, 2.632, 2.631, 2.630, 2.630, 2.629, 2.629, 2.628, 2.627,
                     2.627, 2.626, 2.626]
    Confidence_995 = [2.807, 127.321, 14.089, 7.453, 5.598, 4.773, 4.317, 4.029, 3.833, 3.690, 3.581, 3.497, 3.428,
                      3.372, 3.326, 3.286, 3.252, 3.222, 3.197, 3.174, 3.153, 3.135, 3.119, 3.104, 3.091, 3.078, 3.067,
                      3.057, 3.047, 3.038, 3.030, 3.022, 3.015, 3.008, 3.002, 2.996, 2.990, 2.985, 2.980, 2.976, 2.971,
                      2.967, 2.963, 2.959, 2.956, 2.952, 2.949, 2.946, 2.943, 2.940, 2.937, 2.934, 2.932, 2.929, 2.927,
                      2.925, 2.923, 2.920, 2.918, 2.916, 2.915, 2.913, 2.911, 2.909, 2.908, 2.906, 2.904, 2.903, 2.902,
                      2.900, 2.899, 2.897, 2.896, 2.895, 2.894, 2.892, 2.891, 2.890, 2.889, 2.888, 2.887, 2.886, 2.885,
                      2.884, 2.883, 2.882, 2.881, 2.880, 2.880, 2.879, 2.878, 2.877, 2.876, 2.876, 2.875, 2.874, 2.873,
                      2.873, 2.872, 2.871, 2.871]
    Confidence_9973 = [3.000, 235.784, 19.206, 9.219, 6.620, 5.507, 4.904, 4.530, 4.277, 4.094, 3.957, 3.850, 3.764,
                       3.694, 3.636, 3.586, 3.544, 3.507, 3.475, 3.447, 3.422, 3.400, 3.380, 3.361, 3.345, 3.330, 3.316,
                       3.303, 3.291, 3.280, 3.270, 3.261, 3.252, 3.244, 3.236, 3.229, 3.222, 3.216, 3.210, 3.204, 3.199,
                       3.194, 3.189, 3.184, 3.180, 3.175, 3.171, 3.168, 3.164, 3.160, 3.157, 3.154, 3.151, 3.148, 3.145,
                       3.142, 3.140, 3.137, 3.135, 3.132, 3.130, 3.128, 3.126, 3.123, 3.121, 3.120, 3.118, 3.116, 3.114,
                       3.112, 3.111, 3.109, 3.108, 3.106, 3.105, 3.103, 3.102, 3.100, 3.099, 3.098, 3.096, 3.095, 3.094,
                       3.093, 3.092, 3.091, 3.090, 3.089, 3.087, 3.086, 3.085, 3.085, 3.084, 3.083, 3.082, 3.081, 3.080,
                       3.079, 3.078, 3.078, 3.077]
    Confidence_999 = [3.291, 636.619, 31.599, 12.924, 8.610, 6.869, 5.959, 5.408, 5.041, 4.781, 4.587, 4.437, 4.318,
                      4.221, 4.140, 4.073, 4.015, 3.965, 3.922, 3.883, 3.850, 3.819, 3.792, 3.768, 3.745, 3.725, 3.707,
                      3.690, 3.674, 3.659, 3.646, 3.633, 3.622, 3.611, 3.601, 3.591, 3.582, 3.574, 3.566, 3.558, 3.551,
                      3.544, 3.538, 3.532, 3.526, 3.520, 3.515, 3.510, 3.505, 3.500, 3.496, 3.492, 3.488, 3.484, 3.480,
                      3.476, 3.473, 3.470, 3.466, 3.463, 3.460, 3.457, 3.454, 3.452, 3.449, 3.447, 3.444, 3.442, 3.439,
                      3.437, 3.435, 3.433, 3.431, 3.429, 3.427, 3.425, 3.423, 3.421, 3.420, 3.418, 3.416, 3.415, 3.413,
                      3.412, 3.410, 3.409, 3.407, 3.406, 3.405, 3.403, 3.402, 3.401, 3.399, 3.398, 3.397, 3.396, 3.395,
                      3.394, 3.393, 3.392, 3.390]

    if DegreesOfFreedom > 100:
        DegreesOfFreedom = 100
    elif DegreesOfFreedom < 0:
        DegreesOfFreedom = 1

    if Confidence == 90:
        CoverageFactor = Confidence_90[DegreesOfFreedom]
    elif Confidence == 95:
        CoverageFactor = Confidence_95[DegreesOfFreedom]
    elif Confidence == 99:
        CoverageFactor = Confidence_99[DegreesOfFreedom]
    elif Confidence == 99.5:
        CoverageFactor = Confidence_995[DegreesOfFreedom]
    elif Confidence == 99.73:
        CoverageFactor = Confidence_9973[DegreesOfFreedom]
    elif Confidence == 99.9:
        CoverageFactor = Confidence_999[DegreesOfFreedom]
    else:
        CoverageFactor = Confidence_9545[DegreesOfFreedom]

    return CoverageFactor


def calc_uncertainty(nom_value, type_a_pct, drift_test_pct, sample_qty, attenuator_unc_pct=0, bias_sdev_pct=0):
    # Enter all uncertainty contributors as percent
    # convert the attenuator uncertainties to 1 Sigma

    # Convert percentages to nominal UOM
    attenuator_unc = nom_value / 100 * attenuator_unc_pct

    type_a = nom_value / 100 * type_a_pct

    drift_test = nom_value / 100 * drift_test_pct

    bias_sdev = nom_value / 100 * bias_sdev_pct


    # Get values to 1 Sigma as necessary

    attenuator_unc = attenuator_unc / 2

    # Combine all contributors at 1s
    sum_sq = (attenuator_unc ** 2) + (type_a ** 2) + (drift_test ** 2) + (bias_sdev ** 2)
    sum_contributors = attenuator_unc + type_a + drift_test + bias_sdev

    unc_1s = math.sqrt(sum_sq)

    # Lookup the coverage factor
    degrees_freedom = sample_qty - 1

    coverage_factor = Students_T_Lookup(degrees_freedom, Confidence=95.45)

    # Expand uncertainty to 2s
    unc_2s = unc_1s * coverage_factor

    # Perform uncertainty budget lookup
    unc_2s_pct = unc_2s / (nom_value / 100)
    nom_value_dBm = mW_dBm(nom_value)
    log.info(f'Uncertainty before budget lookup: {unc_2s_pct:.4f} %, {unc_2s:.2E} mW')
    new_unc_2s_pct = UncertaintyBudget.lookup(linBudgetTxtFile, unc_2s_pct, 50_000_000, nom_value_dBm)
    new_unc_2s = (nom_value / 100) * new_unc_2s_pct
    log.info(f'Uncertainty after budget lookup: {new_unc_2s_pct:.4f} %, {new_unc_2s:.2E} mW')

    temp_str = f'\n\nUnc_Eval: attenuator_unc: {attenuator_unc:.1E} mW ({(attenuator_unc / sum_contributors * 100):.2f}%), ' \
               f'degrees_freedom: {degrees_freedom:.0f}, ' \
               f'coverage_factor: {coverage_factor:.4f}, ' \
               f'type_a: {type_a:.2E} mW ({(type_a / sum_contributors * 100):.2f}%), ' \
               f'drift_test: {drift_test:.2E} mW ({(drift_test / sum_contributors * 100):.2f}%), ' \
               f'bias_sdev: {bias_sdev:.2E} mW ({(bias_sdev / sum_contributors * 100):.2f}%), ' \
               f'unc_1s: {unc_1s:.2E} mW, ' \
               f'unc_2s: {unc_2s:.2E} mW' \
               f'unc_2s (after lookup): {new_unc_2s:.2E} mW' \
               f'\nNote: percentages in parenthesis indicate what percent of the total uncertainty the item contributes.' \
               f'\n\nunc_2s: {unc_2s:.2E} mW, {(unc_2s / nom_value * 100):.2f}% of nominal' \
               f'\nunc_2s (after budget lookup): {new_unc_2s:.2E} mW, {(new_unc_2s / nom_value * 100):.2f}% of nominal\n'


    printLog(temp_str, console=verbose_flag)

    return new_unc_2s


def Pass_Fail_Eval(MsmtValue, LowerLimit, UpperLimit, uncertainty):
    Evaluation = ''
    FailFlag = False
    # Make sure the upper and lower limits aren't swapped
    temp_upper = UpperLimit
    temp_lower = LowerLimit
    if LowerLimit > UpperLimit:
        UpperLimit = temp_lower
        LowerLimit = temp_upper

    Pass_Upper = UpperLimit - uncertainty
    UGB1_Upper = UpperLimit
    UGB2_Upper = UpperLimit + uncertainty
    Pass_Lower = LowerLimit + uncertainty
    UGB1_Lower = LowerLimit
    UGB2_Lower = LowerLimit - uncertainty


    if MsmtValue <= Pass_Upper and MsmtValue >= Pass_Lower:
        Evaluation = "Pass"
    elif MsmtValue > UGB2_Upper or MsmtValue < UGB2_Lower:
        Evaluation = "Fail"
        FailFlag = True
    elif MsmtValue > Pass_Upper and MsmtValue <= UGB1_Upper:
        Evaluation = "UGB1"
    elif MsmtValue < Pass_Lower and MsmtValue >= UGB1_Lower:
        Evaluation = "UGB1"
    elif MsmtValue > UGB1_Upper and MsmtValue <= UGB2_Upper:
        Evaluation = "UGB2"
        FailFlag = True
    elif MsmtValue < UGB1_Lower and MsmtValue >= UGB2_Lower:
        Evaluation = "UGB2"
        FailFlag = True

    return (Evaluation, FailFlag)


class UncertaintyBudget:
    @staticmethod
    def GetUOM(budgetTxtFile):
        f = open(budgetTxtFile, 'r')
        budgetData = f.readlines()
        f.close()

        for line in budgetData:
            searchLine = line.lower()
            searchLine = searchLine.strip()
            if "uom" in searchLine:
                searchLine = searchLine.split(",")
                return searchLine[1]
        return "Unknown"

    @staticmethod
    def check_is_expired(budgetTxtFile):
        import datetime
        from datetime import date
        # Place contents of XML files into variable
        f = open(budgetTxtFile, 'r')
        budgetData = f.readlines()
        f.close()

        # Strip any existing whitespace out of the list elements
        for index, element in enumerate(budgetData):
            if element == "\n":
                del budgetData[index]
            else:
                newElement = element.strip()
                budgetData[index] = newElement

        # Placed current date into variable
        today = date.today()
        currentDate = today.strftime("%Y-%m-%d")

        # Obtain the line containing the expiration date of the budget file
        tempList = budgetData[0]
        tempList = tempList.strip()
        tempList = tempList.split(",")
        fileDate = tempList[1]
        fileDate = fileDate.split("-")  # Store date elements into a list
        currentDate = currentDate.split("-")  # Also store today's date elements into list

        # Convert dates into formats which can be compared against
        fileDateInFormat = datetime.datetime(int(fileDate[0]), int(fileDate[1]), int(fileDate[2]))
        currentDateInFormat = datetime.datetime(int(currentDate[0]), int(currentDate[1]), int(currentDate[2]))

        # Check to see if the file date has been exceeded
        if currentDateInFormat > fileDateInFormat:
            return True
        else:
            return False

    @staticmethod
    def lookup(budgetTxtFile, uncVal, uncFreq, uncMsmt=0.0):
        import datetime
        from datetime import date

        # Suppress scientific notation (this code ended up being unnecessary)
        # uncVal = f'{uncVal:.20f}'                       # 20 digits, because why not?
        # uncFreq = f'{uncFreq:.0f}'                      # Frequency in Hz should have no resolution after the decimal

        # Place contents of XML files into variable
        f = open(budgetTxtFile, 'r')
        budgetData = f.readlines()
        f.close()

        # Strip any existing whitespace out of the list elements
        for index, element in enumerate(budgetData):
            if element == "\n":
                del budgetData[index]
            else:
                newElement = element.strip()
                budgetData[index] = newElement

        # Placed current date into variable
        today = date.today()
        currentDate = today.strftime("%Y-%m-%d")

        # Obtain the line containing the expiration date of the budget file
        tempList = budgetData[0]
        tempList = tempList.strip()
        tempList = tempList.split(",")
        fileDate = tempList[1]
        fileDate = fileDate.split("-")  # Store date elements into a list
        currentDate = currentDate.split("-")  # Also store today's date elements into list

        # Convert dates into formats which can be compared against
        fileDateInFormat = datetime.datetime(int(fileDate[0]), int(fileDate[1]), int(fileDate[2]))
        currentDateInFormat = datetime.datetime(int(currentDate[0]), int(currentDate[1]), int(currentDate[2]))

        # Check to see if the file date has been exceeded
        if currentDateInFormat > fileDateInFormat:
            return "File > {} < expiration date is exceeded!".format(budgetTxtFile)

        # del budgetData[0]  # Delete the list element containing the date
        # del budgetData[0]  # Delete the list element containing the UOM

        # Get rid of all lines from the budget data which are not for performing the lookup
        for index, line_data in enumerate(budgetData):
            if not ">" in line_data:
                del budgetData[index]

        # Check to see if this budget format includes Power ranges
        tempList = budgetData[0].split(",")
        tempQty = len(tempList)
        if tempQty > 2:
            pRangePresent = True
        else:
            pRangePresent = False

        # Break out the elements of the uncertainty budget list
        freqList = []
        rangeList = []
        uncList = []
        for index, element in enumerate(budgetData):
            tempList = element.split(",")
            if pRangePresent == True:
                freqList.append(tempList[0])
                rangeList.append(tempList[1])
                uncList.append(float(tempList[2]))
            else:
                freqList.append(tempList[0])
                uncList.append(float(tempList[1]))

        # print(freqList)
        # print(rangeList)
        # print(uncList)

        # Find the current uncertainty frequency within the budget frequency list
        for index, element in enumerate(freqList):
            tempList = element.split(">")
            startFreq = float(tempList[0])
            stopFreq = float(tempList[1])
            uncFreq = float(uncFreq)

            if (uncFreq >= startFreq) and (uncFreq <= stopFreq):

                if pRangePresent == True:
                    tempList = rangeList[index].split(">")
                    startPow = float(tempList[0])
                    stopPow = float(tempList[1])

                    if (uncMsmt >= startPow) and (uncMsmt <= stopPow):
                        tempUncListVal = uncList[index]

                        if uncVal < tempUncListVal:
                            uncVal = tempUncListVal
                            return uncVal
                else:
                    tempUncListVal = uncList[index]
                    if uncVal < tempUncListVal:
                        uncVal = tempUncListVal
                        return uncVal

        return uncVal




# Comms Functions -----------------------------------
def queryVisa(instrument, command, sFunc="", retryQty=5, intervalTime=0.25, timeOutms=2_000):
    command = str(command)

    instrument.timeout = timeOutms

    i = 0
    while i < retryQty:
        try:
            msmt = (instrument.query(command))
            i = 6
        except:
            msmt = "No Data Received"
            time.sleep(intervalTime)
            i += 1

    if msmt.startswith('\"') and msmt.endswith('\"'):
        msmt = msmt[1:-1]
    # msmt = float(msmt)
    msmt = msmt.strip()

    if sFunc != "":
        sFunc = sFunc.lower()

        if sFunc == "float":
            msmt = float(msmt)

    return msmt


def writeVisa(instrument, command, opc=False, opc_cmd="*OPC?", response="+1", timeout=10,
              msg="Waiting for instrument to complete the operation..."):
    def send_command(command):
       e = 'No Error Received.'
       inst = instrument
       retry = True
       cnt = 0
       while retry:
           cnt += 1
           if cnt == 3:
               retry = False
           try:
               inst.write(command)
               retry = False
           except Exception as e:
               temp_msg = f'Check connections and address for resource:\n' \
                          f'{inst}\n\n' \
                          f'Received error: \n' \
                          f'{e}'

               msg_box_simple(temp_msg)
           if cnt == 3:
               temp_msg = f'Could not communicate with resource:\n' \
                          f'{inst}\n\n' \
                          f'Error: \n{e}'
               error_and_exit(temp_msg)

       temp_msg = f'Command Sent: {command}'

       if opc:
           inst_response = visa_OPC_handler(instrument, cmd=opc_cmd, response=response, timeout=timeout,
                                            msg=msg)
           temp_msg = f'Command Sent: {command}, Response: {inst_response}'

       return temp_msg


    cmd_list = command.split(";")

    for index, cmd in enumerate(cmd_list):
        cmd_list[index] = cmd.strip()


    temp_msg = ""
    for cmd in cmd_list:
        response = send_command(cmd)
        temp_msg += response

    return temp_msg


def visa_OPC_handler(visaResourceString, cmd="*OPC?", response="+1", timeout=10,
                     msg="Waiting for instrument to complete the operation..."):
    tempBool = False
    firstRunBool = False
    visaRX = ""
    counter = 0
    while tempBool == False:
        if firstRunBool == True:
            time.sleep(1)
            counter += 1
            printInLine("{}, completion request number {}".format(msg, counter))

        visaRX = queryVisa(visaResourceString, cmd)
        firstRunBool = True

        if (visaRX in response) or (response in visaRX):
            tempBool = True
            return visaRX

        if counter >= timeout:
            input("The Visa {} request has timed out; press enter to continue".format(cmd))
            tempBool = True
            return -1
    print("\n\n")
    clear()


def initialize_visa_get_list():
    import pyvisa as visa
    global rm
    global list
    global resources
    global inst

    # searchString = searchString.lower()
    print('Refreshing VISA resource list...')
    rm = visa.ResourceManager()
    list = rm.list_resources()  # Place the resources into tuple "List"
    resources = []  # Prep for the tuple to be converted "resources" from "list"

    for i, a in enumerate(list):  # Enumerate through the tuple "list"
        resources.append(a)  # Place the current enumeration into the indexed spot of "resources"

    return resources


def set_visa_resource(device_name, search_resource_string='', perform_idn=True, idn_string='*IDN?'):

    printLog(f'Getting {device_name} resource string...')
    tempBool = False
    not_listed_string = '- Enter Resource String Manually'
    refresh_list = '- Refresh VISA Resource List'
    resource_string_no_idn = '- Enter Resource String And Skip IDN Confirmation'

    while tempBool == False:
        visa_device_list = initialize_visa_get_list()
        visa_device_list.append(not_listed_string)
        visa_device_list.append(resource_string_no_idn)
        visa_device_list.append(refresh_list)

        if search_resource_string == '':
            selected_resource = list_selection_box(visa_device_list, field1='Detected VISA Resource List',
                                                   field2=f'Choose the appropriate resource string for device: {device_name}',
                                                   window_title='Resource List',
                                                   width=60)
        else:
            selected_resource = search_resource_string
            formatted_search_rsrc_string = search_resource_string.lower()

            for item in visa_device_list:
                tempString = item.lower()

                if formatted_search_rsrc_string in tempString or tempString in formatted_search_rsrc_string:
                    selected_resource = item
                    search_resource_string = ''
                    break

        if selected_resource == not_listed_string or selected_resource == resource_string_no_idn:

            perform_idn = False if selected_resource == resource_string_no_idn else True

            tempString = f'Please type in the full resource string associated with device {device_name}\n'
            tempString += '(e.g., GPIB0::13::INSTR)'
            selected_resource = text_entry_box(title='Manual Visa Resource Entry', field1=tempString, field2='Resource:')

        if selected_resource == refresh_list:
            time.sleep(1)
        else:
            # print(selected_resource)
            try:
                inst = rm.open_resource(selected_resource)
                if perform_idn:
                    response = queryVisa(inst, idn_string, sFunc="", retryQty=5)
                    printLog(f'Set and queried {device_name} - Resource: {inst}, Responded: {response}')
                    tempString = f'Verify the selected resource for device >{device_name}< is correct:\n\n' \
                                 f'Resource Address: {inst}\n\n' \
                                 f'Received: {response}'
                    if debug_flag == False:
                        tempBool = yes_no_popup_simple(tempString)
                    else:
                        tempBool = True
                else:
                    tempString = f'Verify the selected resource for device >{device_name}< is correct, and the ' \
                                 f'device is connected and powered on \n\n' \
                                 f'Resource: {selected_resource}'
                    if debug_flag == False:
                        tempBool = yes_no_popup_simple(tempString)
                    else:
                        tempBool = True

                    if not tempBool:
                        selected_resource = ''
                        search_resource_string = ''
                    else:
                        printLog(f'User manually confirmed {device_name} - Resource: {inst}')

            except:
                printLog(f'Failed to get open resource string: {selected_resource}', errorInfo=True, console=False)
                tempString = f'The selected resource for remote instrument >{device_name}< is invalid!' \
                             f'\n\nResource: {selected_resource}\n\nPlease try again.'
                msg_box_simple(tempString)
                selected_resource = ''
                search_resource_string = ''

    return inst


# Misc -------------------------------
def replacer(s, newstring, index, nofail=False):
    # Replaces a section of a string (s) with [newstring] at the specified index (index)

    # raise an error if index is outside of the string
    if not nofail and index not in range(len(s)):
        raise ValueError("index outside given string")

    # if not erroring, but the index is still not in the correct range..
    if index < 0:  # add it to the beginning
        return newstring + s
    if index > len(s):  # add it to the end
        return s + newstring

    # insert the new string between "slices" of the original
    return s[:index] + newstring + s[index + 1:]


def sanitize_variable(input_variable, default_response='', specified_class='', error_response='error', eval_operation='',
                      eval_threshold=''):

    def evaluate_variable(variable_to_evaluate, operation_type, limit_value, corrected_value):
        return_value = variable_to_evaluate
        variable_class_type = return_class_type(variable_to_evaluate)

        if not variable_class_type in ['int', 'float']:
            return corrected_value

        if operation_type == 'at least':
            if variable_to_evaluate < limit_value:
                return_value = corrected_value
        elif operation_type == 'at most':
            if variable_to_evaluate > limit_value:
                return_value = corrected_value

        return return_value

    def cast_int(variable):
        return int(variable)

    def cast_str(variable):
        return str(variable)

    def cast_float(variable):
        return float(variable)

    reclass_variable = {'int': cast_int,
                        'str': cast_str,
                        'float': cast_float}

    specified_class = specified_class.lower()
    eval_operation = eval_operation.lower()

    if specified_class == 'int' and return_class_type(error_response) != 'int':
        error_response = 999_999_999
    elif specified_class == 'float' and return_class_type(error_response) != 'float':
        error_response = 999_999_999.999

    new_value = input_variable

    class_type_list = ['str', 'int', 'float', 'list', 'tuple', '']
    eval_operation_list = ['at least', 'at most', '']

    if (specified_class not in class_type_list) or (eval_operation not in eval_operation_list):
        return error_response

    if specified_class != '':
        input_class_type = return_class_type(input_variable)

        if input_class_type != specified_class:
            try:
                new_value = reclass_variable[specified_class](input_variable)
            except:
                new_value = error_response

    if new_value == error_response and default_response != '':
        new_value = default_response
    elif new_value != error_response and eval_operation != '' and default_response != '' and eval_threshold != '':
        new_value = evaluate_variable(new_value, eval_operation, eval_threshold, default_response)

    return new_value


def check_in_bounds(value, upper_limit, lower_limit):
    try:
        value = float(value)
    except:
        temp_str = f"One of these is not an int or float, so cannot check in bounds!\n" \
                   f"value to check: {value}, lower_limit: {lower_limit}," \
                   f"upper_limit: {upper_limit}"
        printLog(temp_str)
        return False

    if value > upper_limit or value < lower_limit:
        return False
    else:
        return True


def return_class_type(variable):
    test = f'{type(variable)}'
    test = test.split()
    test = test[1]
    test = test[1:]
    test = test[:-2]
    return test


# def find_nth(haystack, needle, n=1):
#     start = haystack.find(needle)
#     while start >= 0 and n > 1:
#         start = haystack.find(needle, start + len(needle))
#         n -= 1
#     return start


def find_nth(haystack: str, needle: str, nth_occurrence=1, case_insensitive=False):
    # searches strings and lists (the haystack) for nth occurrence of the needle.
    # Will convert int and float to string

    def str_search(haystack, needle, nth_occurrence, case_insensitive):
        result = -1
        if case_insensitive == True:
            haystack = haystack.lower()
            needle = needle.lower()

        start = haystack.find(needle)
        while start >= 0 and nth_occurrence > 1:
            start = haystack.find(needle, start + len(needle))
            nth_occurrence -= 1
        result = start

        return result

    def list_search(haystack, needle, nth_occurrence, case_insensitive):
        result = -1
        if case_insensitive == True:
            needle = needle.lower()

            for index, item in enumerate(haystack):
                try:
                    haystack[index] = item.lower()
                except Exception as err:
                    printLog(err, console=False)

        occurrence_cntr = 0
        for index, item in enumerate(haystack):
            try:
                if item == needle:
                    occurrence_cntr += 1
                    if occurrence_cntr == nth_occurrence:
                        result = index
            except Exception as err:
                printLog(Exception, console=False)

        return result

    var_type = return_class_type(haystack)
    if (not var_type == 'str') and (not var_type == "list"):
        haystack = str(haystack)

    if (return_class_type(haystack)) == "str":
        needle = str(needle)

    var_type = return_class_type(haystack)
    if var_type == 'str':
        return str_search(haystack, needle, nth_occurrence, case_insensitive)
    elif var_type == "list":
        return list_search(haystack, needle, nth_occurrence, case_insensitive)
    else:
        return -1


def getTstampSeconds():
    from time import time

    return int(time())



class cache:
    # Used to create a variable cache, to allow for persistent variables outside of
    # program run-time
    @staticmethod
    def put(varname, var_value, variable_cache_file_path="./variable_cache.dat"):
        import os

        def find_line_index(list_var, search_value, split_character="="):
            return_index_found = -1
            for index, line in enumerate(list_var):

                if (search_value in line) and (split_character in line):
                    temp_list = line.split(split_character)
                    line_variable_name = temp_list[0].strip()
                    # input(f"Line var: >{line_variable_name}<")

                    if line_variable_name == search_value:
                        return_index_found = index
                        break

            return return_index_found

        def readTxtFile(filename):
            # Place contents of text files into variable
            f = open(filename, 'r')
            x = f.readlines()
            f.close()
            return x

        def writeListToFile(filename, my_list, write_type='w'):
            def ensure_file_exists(filepath):
                if not os.path.exists(filepath):
                    with open(filepath, 'w') as fp:
                        pass

            def write_list_normal(filename, write_type):
                with open(filename, write_type) as f:
                    for item in my_list:
                        f.write("%s\n" % item)

            def write_list_utf8(filename, write_type):
                with open(filename, write_type, encoding="utf-8") as f:
                    for item in my_list:
                        f.write("%s\n" % item)

            ensure_file_exists(filename)

            try:
                write_list_normal(filename, write_type)
            except Exception as e:
                error = f'{e}'
                error = error.lower()
                if 'permission denied' in error:
                    temp_str = f'Access Denied for file: {filename}\n\n' \
                               f'Please ensure the file is not in use by another program before proceeding!' \
                               f'\nPress Enter to continue...'
                    input(temp_str)
                    write_list_normal(filename, write_type)
                else:
                    write_list_utf8(filename, write_type)

        def write_item_to_file(filename, item_to_write, write_type='a'):
            def ensure_file_exists(filepath):
                if not os.path.exists(filepath):
                    with open(filepath, 'w') as fp:
                        pass

            def write_list_normal(filename, item_to_write, write_type):
                with open(filename, write_type) as f:
                    f.write("%s\n" % item_to_write)

            def write_list_utf8(filename, item_to_write, write_type):
                with open(filename, write_type, encoding="utf-8") as f:
                    f.write("%s\n" % item_to_write)

            ensure_file_exists(filename)

            item_to_write = f"{item_to_write}"

            try:
                write_list_normal(filename, item_to_write, write_type)
            except Exception as e:
                error = f'{e}'
                error = error.lower()
                if 'permission denied' in error:
                    temp_str = f'Access Denied for file: {filename}\n\n' \
                               f'Please ensure the file is not in use by another program before proceeding!' \
                               f'\nPress Enter to Continue... '
                    input(temp_str)
                    write_list_normal(filename, item_to_write, write_type)
                else:
                    write_list_utf8(filename, item_to_write, write_type)

        if not os.path.exists(variable_cache_file_path):
            with open(variable_cache_file_path, 'w') as fp:
                pass

        string_to_write = f"{varname}={var_value}"

        var_cache_contents = readTxtFile(variable_cache_file_path)

        for index, item in enumerate(var_cache_contents):
            item = item.strip()
            var_cache_contents[index] = item

        index_to_write = find_line_index(var_cache_contents, varname)

        if index_to_write < 0:

            write_item_to_file(variable_cache_file_path, string_to_write)
        else:
            var_cache_contents[index_to_write] = string_to_write
            writeListToFile(variable_cache_file_path, var_cache_contents, write_type='w')

    @staticmethod
    def get(varname, variable_cache_file_path="./variable_cache.dat", split_character="="):
        variable_content = ""

        if not os.path.exists(variable_cache_file_path):
            with open(variable_cache_file_path, 'w') as fp:
                pass

        # Open the file
        with open(variable_cache_file_path, "r") as filestream:
            # Loop through each line in the file

            # find_line_index(filestream, "verbose")
            for index, line in enumerate(filestream):

                if (varname in line) and (split_character in line):
                    temp_list = line.split(split_character)
                    line_variable_name = temp_list[0].strip()
                    # input(f"Line var: >{line_variable_name}<")

                    if (line_variable_name == varname) and (len(temp_list) > 1):
                        variable_content = temp_list[1]
                        variable_content = variable_content.strip()
                        break

        filestream.close()
        return variable_content


def timestampToDatetime(timestamp: int) -> str:
    from datetime import datetime
    return str(datetime.fromtimestamp(timestamp))


# Dependent Modules Inlcuded in Python
import time
import os


# Variables used by the module
debug_flag = False


# Check that required packages are installed prior to using this module


try:
    print("Checking for package PySimpleGUI...")
    import PySimpleGUI

    print(">>Found package PySimpleGUI!")
except ImportError as e:
    temp_str = ">> Warning - Package PySimpleGUI is not installed!"
    # error_and_exit(temp_str, pause_time=1, pause=True)
    printLog(temp_str)
print()

try:
    print("Checking for package pyvisa...")
    import pyvisa

    print(">> Found package pyvisa!")
except ImportError as e:
    temp_str = ">> Warning - Package pyvisa is not installed!"
    # error_and_exit(temp_str, pause_time=1, pause=True)
    printLog(temp_str)
print()

try:
    print("Checking for Python Imaging Library Package (Pillow)...")
    import PIL

    print(">> Found package Pillow!")
except ImportError as e:
    temp_str = ">> Warning -Python Imaging Library (Pillow) is not installed!"
    # error_and_exit(temp_str, pause_time=1, pause=True)
    printLog(temp_str)
print()





