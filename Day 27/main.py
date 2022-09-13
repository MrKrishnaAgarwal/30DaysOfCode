import subprocess

def main():
    file = open('Day27.js', 'w') # w = write
    file.write('console.log("Welcome to 30 Days of Code!");') # write to file
    file.close() # close file

    file = open('Day27.js', 'r') # r = read
    print(file.read()) # read file
    file.close() # close file

    subprocess.call(['node', 'Day27.js']) # run node Day27.js

if __name__ == '__main__':
    main() # run main function