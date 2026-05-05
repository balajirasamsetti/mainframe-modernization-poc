import os

def generate_data():
    # Define paths
    folder = 'mainframe'
    filename = 'CUSTOMER_EXTRACT.txt'
    path = os.path.join(folder, filename)

    # Ensure the 'mainframe' folder exists
    if not os.path.exists(folder):
        os.makedirs(folder)

    # Records: ID(8), LNAME(15), FNAME(15), BAL(10), FILLER(32) = 80 chars
    records = [
        "00000001SMITH          JOHN           0000125050                                ",
        "00000002DOE            JANE           0000099500                                ",
        "00000003GARCIA         CARLOS         0000500000                                "
    ]

    with open(path, 'w') as f:
        for line in records:
            f.write(line + '\n')
    
    print(f"SUCCESS: Created {path}")

if __name__ == "__main__":
    generate_data()