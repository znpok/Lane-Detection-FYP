import os

def save_filenames_to_txt(folder_path, output_file):
    try:
        # Get a list of files in the folder
        filenames = os.listdir(folder_path)
        
        # Open the output file in write mode
        with open(output_file, 'w') as file:
            # Write each filename to the file
            for filename in filenames:
                file.write(f"frames/{filename}\n")
        
        print(f"File names written to {output_file}")
    
    except Exception as e:
        print(f"Error: {e}")

# Example usage:
folder_path = r'C:\Users\pokzh\Desktop\Lane Detection FYP\Ultra-Fast-Lane-Detection\MYCARRYDATA\frames'  # Replace with the path to your folder
output_file = r'C:\Users\pokzh\Desktop\Lane Detection FYP\Ultra-Fast-Lane-Detection\MYCARRYDATA\testest.txt'    # Replace with your desired output file name
save_filenames_to_txt(folder_path, output_file)
