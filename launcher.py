#!/usr/bin/env python3

# Skyfear Launch Script, written by @telekrex:
# The goal of this software is to accommodate the
# unpredictable state of any machine attempting to
# run Skyfear, outside of the Unreal Engine environment,
# due to limitations within the Unreal Engine environment.
# And for the future, this script allows a flexibile solution
# to any further pre-requisite and hardware issues that arise.

# Because this utility requires elevated priveledges and may
# interact with sensitive operating system information, I
# am publically sharing the source code so that
# 1) anyone can verify its function and trustworthyness,
# 2) better programmers than me can suggest improvements.
# The rest of the game, included in SKYFEAR.exe is made up
# of a source-built Unreal Engine 4.21, and contains no
# third party or custom software like this utility.

# Please submit any found issues or vulnerabilities to
# `protoriastudios@gmail.com`, or hit me up on Discord.


print('\n\n  Skyfear Launch Script')
print('  Source code: https://github.com/Protoria-Studios/skyfear-launch-script\n\n')


import sys, os, subprocess


print(f'  File: {os.path.realpath(__file__)}')
working_directory = os.getcwd()
print(f'  Running from: {working_directory}')


def verify_client():
    global working_directory
    expected_game_path = working_directory + '/SKYFEAR.exe'
    if os.path.isfile(expected_game_path):
        print(f'  Game client: {expected_game_path}')
        return True
    else:
        print('  No game client found.')
        return False


def platform():
    return sys.platform.lower()


def launch():
    input('  Going to run SKYFEAR.exe, continue?')
    print('\n\n  Launching Skyfear...')
    try:
        os.system('SKYFEAR.exe')
        # on exit,
        print('  Shutting down...')
        input('  Press any key to close...')
    except Exception as e:
        print('  Error:', {e})
        print('  Please report this issue to `protoriastudios@gmail.com`, discord, or Steam community discussions.')
        input('  Press any key to continue... 4')


def print_environment_variables():
    print('  Checking environment variables...')
    for key, value in os.environ.items():
        print(f"  {key} = {value}")
    print()


def env_var_exists_and_not_empty(var_name):
    return var_name in os.environ and bool(os.environ[var_name].strip())


def verify_variable():
    var_to_check = "OPENSSL_ia32cap"
    print(f'  Checking for {var_to_check}')
    result = env_var_exists_and_not_empty(var_to_check)
    if result:
        print(f"  {var_to_check} exists and is not empty")
        return True
    else:
        print(f"  {var_to_check} does not exist or is empty")
        return False


def set_env_variable(name, value, system=False):
    command = ["setx", name, value]
    if system:
        command.append("/M")
    try:
        result = subprocess.run(command, capture_output=True, text=True, shell=True)
        if result.returncode == 0:
            # Update the current process environment
            os.environ[name] = value
            print(f"  Successfully set {name} as a {'system' if system else 'user'} variable.")
            return True
        else:
            print(f"  Error setting variable: {result.stderr.strip()}")
            return False
    except Exception as e:
        print(f"  Exception: {e}")
        return False


def verify_env_variable(name, expected_value):
    actual_value = os.environ.get(name)
    return actual_value == expected_value


print('  Checking platform...', platform())
WINDOWS = True if 'win' in str(platform()).lower() else False


if WINDOWS:
    print('  Windows based platform detected.')
    if verify_client():
        print_environment_variables()
        if verify_variable():
            launch()
        else:
            var_name = "OPENSSL_ia32cap"
            var_value = "~0x200000200000000"
            if set_env_variable(var_name, var_value, system=False):
                if verify_env_variable(var_name, var_value):
                    print(f"  Verified: {var_name} is set correctly in current session.")
                    # then re-run the script
            else:
                print(f"  Verification failed: {var_name} is not correct in current session.")
            input('  Press any key to continue 1...')
    else:
        input('  Press any key to continue 2...')


else:
    print('  Non-Windows based platform detected.')
    if verify_client():
        launch()
    else:
        input('  Press any key to continue 3...')